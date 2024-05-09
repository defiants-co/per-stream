from perpstream.base.models import Position
from perpstream.base import SUPPORTED_MARKETS
from perpstream.dydx import MAX_LEVERAGE_MAP
from typing import Dict, Any, List
import json

def return_positions_from_call(data : Dict[str, List[Dict[str, Dict[str,Any]]]]) -> List[Position]:
    positions = []
    if data['subaccounts']:
        account_positions = data['subaccounts'][0]['openPerpetualPositions']
        for position in account_positions:
            p = account_positions[position]
            ticker = p['market'].split('-')[0]
            if ticker in SUPPORTED_MARKETS and p['status'] == "OPEN":
                size = abs(float(p['size']))
                is_long = p['side'] == "LONG"
                entry_price = float(p['entryPrice'])
                pnl = float(p['unrealizedPnl'])
                mark_price = (
                    (pnl + (size*entry_price)) / size
                    if is_long else
                    ((size * entry_price) - pnl) / size
                )

                positions.append(Position(
                    ticker=ticker,
                    size=size,
                    is_long=is_long,
                    entry_price=entry_price,
                    pnl=pnl, # todo - figure out how to find relative to collateral size
                    leverage_amount=0,
                    collateral_token="USDC",
                    collateral_amount=0,
                    collateral_amount_usd=0,
                    mark_price=mark_price
                ))

    return positions
