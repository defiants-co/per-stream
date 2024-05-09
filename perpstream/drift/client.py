# from typing import Optional, List
# import asyncio
# from solders.keypair import Keypair
# from perpstream.base.models import Position
# from perpstream.drift import SOLANA_RPC_URL
# from perpstream.base.client import BaseClient
# from solana.rpc.async_api import AsyncClient
# from driftpy.drift_client import DriftClient as Client
# from driftpy.drift_user import DriftUser, Pubkey


# class DriftClient(BaseClient):

#     def __init__(self, url: str = SOLANA_RPC_URL, auth_token: Optional[str] = None):
#         self.drift_client = Client(
#             connection=AsyncClient(url),
#             wallet=Keypair()
#         )

#     def fetch_positions(self, user_id: str) -> List[Position]:
#         return []
