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
