from json import load
from perpstream.base.models import Position
from typing import Optional, List

def load_positions_from_json(filename) -> List[Position]:
    """
    Reads a JSON file containing position data and returns a list of Position objects.

    Args:
    filename (str): The path to the JSON file.

    Returns:
    List[Position]: A list of Position objects.
    """
    with open(filename, 'r') as file:
        positions_data = load(file)

        positions = []
        for data in positions_data:
            position = Position(
                ticker=data['ticker'],
                leverage_amount=data['leverage_amount'],
                collateral_token=data['collateral_token'],
                collateral_amount=data['collateral_amount'],
                collateral_amount_usd=data['collateral_amount_usd'],
                entry_price=data['entry_price'],
                mark_price=data['mark_price'],
                pnl=data['pnl'],
                is_long=data['is_long'],
                size=data['size']
            )
            positions.append(position)

        return positions


positions = (load_positions_from_json('positions.json'))

num_short_list = ([position for position in positions if not position.is_long])

num_long_list = ([position for position in positions if  position.is_long])

avg_profit_short = sum([x.pnl for x in num_short_list]) / len(num_short_list)
avg_profit_long = sum([x.pnl for x in num_long_list]) / len(num_long_list)

print(avg_profit_short)
print(avg_profit_long)
