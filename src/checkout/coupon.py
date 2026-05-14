"""Coupon application for checkout totals."""

from __future__ import annotations


COUPON_DISCOUNTS = {
    "SAVE10": 0.10,
    "SAVE20": 0.20,
    "HALFOFF": 0.50,
}


def apply_coupon(subtotal: float, coupon_code: str) -> float:
    """Return discounted subtotal after applying the coupon."""
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    code = coupon_code.strip().upper()
    discount_rate = COUPON_DISCOUNTS.get(code, 0)
    # Bug: adds the discount instead of subtracting it, making the total higher.
    return subtotal + (subtotal * discount_rate)
