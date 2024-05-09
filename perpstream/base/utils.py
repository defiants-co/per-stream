from .models import Position
from urllib.parse import urlparse
from typing import List, Dict
from json import dumps

def verify_position_sets_are_equal(
    positions_1 : List[Position],
    positions_2 : List[Position]
) -> bool:

    if len(positions_2) != len(positions_1):
        return False

    for position in positions_1:
        if position not in positions_2:
            return False

    return True


def is_url_valid(url: str) -> bool:
    """
    Checks if the given string is a valid URL.

    Args:
        url (str): The URL string to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    try:
        parsed_url = urlparse(url)
        # A valid URL has both a scheme (e.g., http, https) and netloc (domain name)
        return bool(parsed_url.scheme) and bool(parsed_url.netloc)
    except Exception:
        return False
