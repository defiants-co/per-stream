from datetime import datetime
from typing import List, Optional

class Position:
    """
    Represents a trading position with various attributes relevant to market positions.
    Additionally, it includes a boolean indicating if the position is long or short.

    Attributes:
        ticker (str): The ticker symbol of the asset.
        leverage_amount (float): The amount of leverage used in the position.
        collateral_token (str): The token used as collateral.
        collateral_amount (float): The amount of collateral token used.
        entry_price (float): The entry price of the position.
        mark_price (float): The current market price of the asset.
        pnl (float): The current profit and loss of the position.
        is_long (bool): True if the position is long, False if it is short.
    """

    def __init__(
        self,
        ticker: str,
        leverage_amount: float,
        collateral_token: str,
        collateral_amount: float,
        collateral_amount_usd : float,
        entry_price: float,
        mark_price: float,
        pnl: float,
        is_long: bool,
        size : float
    ):
        self.ticker = ticker
        self.leverage_amount = leverage_amount
        self.collateral_token = collateral_token
        self.collateral_amount = collateral_amount
        self.collateral_amount_usd = collateral_amount_usd
        self.entry_price = entry_price
        self.mark_price = mark_price
        self.pnl = pnl
        self.is_long = is_long
        self.size = size


    def __repr__(self):
        return (f"Position(ticker={self.ticker}, "
                f"leverage_amount={self.leverage_amount}, "
                f"collateral_token={self.collateral_token}, "
                f"collateral_amount={self.collateral_amount}, "
                f"collateral_amount_usd={self.collateral_amount_usd}, "
                f"entry_price={self.entry_price}, "
                f"mark_price={self.mark_price}, "
                f"pnl={self.pnl}, "
                f"is_long={self.is_long},"
                f"size={self.size})")

    def __sub__(self, other):
        return PositionDelta(self, other)

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented

        return (
            self.ticker == other.ticker and
            self.leverage_amount == other.leverage_amount and
            self.collateral_token == other.collateral_token and
            self.collateral_amount == other.collateral_amount and
            abs(self.entry_price - other.entry_price) < (0.01 * self.entry_price) and
            self.is_long == other.is_long and
            abs(self.size - other.size) < (0.01 * self.size)

        )

    def json(self):
            """Serialize the object to a JSON-formatted str."""
            return {
                'ticker': self.ticker,
                'leverage_amount': self.leverage_amount,
                'collateral_token': self.collateral_token,
                'collateral_amount': self.collateral_amount,
                'collateral_amount_usd': self.collateral_amount_usd,
                'entry_price': self.entry_price,
                'mark_price': self.mark_price,
                'pnl': self.pnl,
                'is_long': self.is_long,
                'size': self.size
            }


class PositionDelta:
    """
    Represents the difference between two trading positions.
    Attributes are prefixed with 'delta' to denote the change.

    Attributes:
        delta_ticker (str): The ticker symbol of the asset.
        delta_leverage_amount (float): The change in leverage amount.
        delta_collateral_amount (float): The change in collateral amount used.
        delta_entry_price (float): The change in entry price of the position.
        delta_mark_price (float): The change in current market price of the asset.
        delta_pnl (float): The change in profit and loss of the position.
        delta_time (timedelta): The difference in last update times of the positions.
        direction_has_changed (bool): Returns true if the direction of the position has changed
    """

    def __init__(self, position1: Position, position2: Position):
        if position1.ticker != position2.ticker:
            raise ValueError("Positions must have the same ticker to compare")

        self.ticker = position1.ticker
        self.delta_leverage_amount = position1.leverage_amount - position2.leverage_amount
        self.delta_collateral_amount = position1.collateral_amount - position2.collateral_amount
        self.delta_collateral_amount_usd = round(position1.collateral_amount_usd - position2.collateral_amount_usd, 2)
        self.delta_entry_price = position1.entry_price - position2.entry_price
        self.delta_mark_price = position1.mark_price - position2.mark_price
        self.delta_pnl = position1.pnl - position2.pnl
        self.direction_has_changed = position1.is_long != position2.is_long

    def __repr__(self):
        return f"PositionDelta(delta_ticker={self.ticker}, delta_leverage_amount={self.delta_leverage_amount}, " \
               f"delta_collateral_amount={self.delta_collateral_amount}, delta_entry_price={self.delta_entry_price}, " \
               f"delta_mark_price={self.delta_mark_price}, delta_pnl={self.delta_pnl}" \
               f"delta_collateral_amount_usd={self.delta_collateral_amount_usd})"
