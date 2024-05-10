from perpstream.base.client import BaseClient
from perpstream.base.models import Position
from perpstream.base.errors import RequestError
from .dydx_utils import return_positions_from_call
from typing import Optional, List
from . import INDEXER_URL

class DydxClient(BaseClient):

    def __init__(self, url: str = INDEXER_URL, auth_token: Optional[str] = None):
        super().__init__(url, auth_token)

    def fetch_positions(self, user_id: str) -> List[Position]:
        try:
            response = self._request(path="/addresses/" + user_id)
            return return_positions_from_call(response)
        except RequestError as e:
            raise e

    def name(self) -> str:
        return "dydx-v4"

    # def poll_positions(self, user_id: str, callback: Callable[[List[Position], List[Position], str, str], None], init_with_callback: bool = False, time_wait_seconds: float = 0, debug: bool = False):
        # TODO: add websocket support to override polling
