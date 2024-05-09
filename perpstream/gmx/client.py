from typing import Optional, Dict, Any, List
from perpstream.base.client import BaseClient
from perpstream.base.errors import InvalidUrl, RequestError
from perpstream.base.models import Position
import requests
from perpstream.gmx import ARBITRUM_RPC_URL, AVAX_RPC_URL
from .gmx_utils import configure, return_positions_from_call
from gmx_python_sdk.scripts.v2.get.get_open_positions import GetOpenPositions
from web3 import Web3

class GmxClient(BaseClient):

    def __init__(self, url : str, auth_token : Optional[str] = None, chain : str = "arbitrum"):
        super().__init__(url=url, auth_token=auth_token)
        configure(
            arb_url=url if chain == "arbitrum" else ARBITRUM_RPC_URL,
            avax_url=url if chain == "avalanche" else AVAX_RPC_URL
        )
        self.web3_client = Web3(Web3.HTTPProvider(url))
        if not self.web3_client.is_connected():
            raise InvalidUrl

        self.chain = chain

    def fetch_positions(self, user_id: str) -> List[Position]:
        try:
            positions = GetOpenPositions(chain=self.chain, address=user_id).get_data()
            return return_positions_from_call(data=positions)

        except NameError as e:
            return []

        except requests.exceptions.RequestException as e:
            if e.response:
                raise RequestError(e.response.status_code, e.response.text)
            else:
                raise RequestError(0, e.__str__())

    def name(self) -> str:
        return "gmx"

class GmxArbitrumClient(GmxClient):

    def __init__(self, url: str = ARBITRUM_RPC_URL, auth_token: str | None = ""):
        super().__init__(url, auth_token, chain="arbitrum")

    def name(self) -> str:
        return "gmx-arbitrum"
