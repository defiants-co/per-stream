import datetime
from json.decoder import JSONDecoder
from urllib import parse
import requests
from urllib.parse import urlparse
from .models import Position
from .errors import ClientNotImplemented, InvalidUrl, RequestError
from .utils import verify_position_sets_are_equal, is_url_valid
from typing import List, Iterator, Dict, Any, Tuple, Callable, Optional
from time import sleep


class BaseClient:
    """
    Base client for handling connections and operations against a cryptocurrency service.

    Attributes:
        url (str): The base URL for the cryptocurrency service.
        auth_token (str): Authentication token for the service.

    Raises:
        ClientNotImplemented: If any method is not implemented by a subclass.
    """

    def __init__(self, url: str, auth_token: Optional[str]):
        """
        Initialize the BaseClient with the service URL and authentication token.

        Args:
            url (str): The base URL for the cryptocurrency service.
            auth_token (str): Authentication token for the service.

        Raises:
            ClientNotImplemented: Indicates that the constructor is not implemented.
        """
        if not is_url_valid(url=url):
            raise InvalidUrl

        if not url.endswith('/'):
            url = url + '/'

        self.url = url
        self.auth_token = auth_token

    def name(self) -> str:
        return "base_client"

    def _request(
        self,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        path: str = "",
        method: str = "GET"
    ) -> Dict[str, Any]:
        """
        Perform a request to the cryptocurrency service.

        Args:
            params (Dict[str, Any]): Parameters to be sent in the request.
            headers (Dict[str, Any]): Headers to be sent in the request.
            path (str): The specific path to append to the base URL for the request.

        Returns:
            Dict[str, Any]: The response from the service as a dictionary.
        """

        try:
            response = requests.request(
                method=method,
                url=self.url + path,
                params=params,
                headers=headers,
            )

            response.raise_for_status()

            return response.json()

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            raise RequestError()

        except requests.exceptions.JSONDecodeError:
            raise RequestError(message="JSON decode error")

        except requests.exceptions.HTTPError as e:
            print(e.response.text)
            raise RequestError(status_code=e.response.status_code, message=e.response.text)

    def fetch_positions(self, user_id: str) -> List[Position]:
        """
        Fetch the current positions for a given user.

        Args:
            user_id (str): The ID of the user whose positions are to be fetched.

        Returns:
            List[Position]: A list of Position objects for the user.

        Raises:
            ClientNotImplemented: Indicates that the fetch_positions method is not implemented.
        """
        raise ClientNotImplemented("fetch_positions")

    def poll_positions(
        self, user_id: str,
        callback: Callable[[List[Position], List[Position], str, str], None],
        init_with_callback : bool = False,
        time_wait_seconds: float = 0,
        debug: bool = False,

    ):
        """
        Continuously poll for the user's positions and invoke a callback with the new and old positions.

        Args:
            user_id (str): The ID of the user whose positions are to be polled.
            time_wait_seconds (float): The time interval, in seconds, between polls.
            debug (bool): If True, additional debug information will be printed.
            callback (Callable[[List[Position], List[Position], str, str]]): A callback function that takes two arguments:
                a list of new positions and a list of old positions, as well as the user_id and data source
        """
        count = 0
        if debug: print("starting stream")

        last_positions, fetched = [], False

        while not fetched:
            try:
                last_positions = self.fetch_positions(user_id=user_id)
                fetched = True

            except RequestError:
                if debug:
                    print('failed to fetch the data, trying again')

        if init_with_callback:
            try:
                callback(last_positions, [], user_id, self.name())
            except Exception as e:
                if debug: print('initial callback failed with: ' + str(e))


        while True:
            start = datetime.datetime.now()
            try:
                new_positions = self.fetch_positions(user_id=user_id)
                count += 1
                if not verify_position_sets_are_equal(last_positions, new_positions):
                    if debug:
                        print("detected change, calling callback")
                    try:
                        callback(last_positions, new_positions, user_id, self.name())
                    except Exception as e:
                        if debug: print('callback failed with: ' + str(e))
                    if debug:
                        print("called callback")

                    last_positions = new_positions

            except RequestError as e:
               if debug: print(e.__str__())

            except Exception as e:
                if debug: print(e)

            end = datetime.datetime.now()
            if debug:
                print(f"round {count} - took {(end-start).total_seconds()} sec")
            if time_wait_seconds : sleep(time_wait_seconds)
