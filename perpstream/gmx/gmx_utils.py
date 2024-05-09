from gmx_python_sdk.scripts.v2.gmx_utils import Config
from typing import Dict, Any, List
from perpstream.gmx import ARBITRUM_RPC_URL, AVAX_RPC_URL
from perpstream.base.models import Position
from perpstream.base import SUPPORTED_MARKETS
from datetime import datetime

def configure(arb_url: str = ARBITRUM_RPC_URL, avax_url : str = AVAX_RPC_URL ):
    config_data ={
        "arbitrum": {
            "rpc": arb_url,
            "chain_id": "42161"
        },
        "avalanche": {
            "rpc": avax_url,
            "chain_id": "43114"
        },

        "private_key": "",
        "user_wallet_address": ""
    }

    config_object = Config()

    new_config = config_object.load_config()

    for key in config_data:
        new_config[key] = config_data[key]

    config_object.set_config(new_config)


def return_positions_from_call(data : Dict[str, Dict[str, Any]]) -> List[Position]:
    positions = []
    for (position_id, value) in data.items():
        parts = position_id.split("_")

        ticker = parts[0]
        if ticker in SUPPORTED_MARKETS:
            is_long = parts[1] == "long"

            leverage_amount = value['leverage']
            collateral_token = value['collateral_token']
            entry_price = value['entry_price']
            mark_price = value['mark_price']
            size = value['position_size']
            collateral_amount = value['inital_collateral_amount']
            collateral_amount_usd = value['inital_collateral_amount_usd'][0]
            pnl = value['percent_profit'] * collateral_amount_usd

            if collateral_token not in ["USDC", "DAI", "USDC.e"]:
                collateral_amount_usd = collateral_amount_usd * entry_price


            position = Position(
                ticker=ticker,
                leverage_amount=leverage_amount,
                collateral_token=collateral_token,
                collateral_amount=collateral_amount,
                collateral_amount_usd=collateral_amount_usd, # Assuming this is a single-element tuple
                entry_price=entry_price,
                mark_price=mark_price,
                pnl=pnl,
                is_long=is_long,
                size=size
            )

            positions.append(position)

    return positions
