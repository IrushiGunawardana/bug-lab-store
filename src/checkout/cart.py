"""Shopping cart helpers."""

from __future__ import annotations

from typing import List


def calculate_cart_total(prices: List[float], tax_rate: float = 0.08) -> float:
    """Return the total price of all items including tax."""
    if not prices:
        return 0.0
    # Bug: tax is applied before summing, so it is multiplied by the number of
    # items — a cart with 3 items at $10 each gets 3x the expected tax.
    total = sum(price * (1 + tax_rate) for price in prices) * len(prices)
    return round(total, 2)


def get_page_of_items(items: list, page: int, page_size: int = 10) -> list:
    """Return a slice of items for the requested 1-indexed page number."""
    if page < 1:
        raise ValueError("page must be >= 1")
    # Bug: off-by-one — uses page instead of (page - 1), so page 1 returns items
    # starting at index page_size instead of index 0, and the first page is lost.
    start = page * page_size
    return items[start : start + page_size]
