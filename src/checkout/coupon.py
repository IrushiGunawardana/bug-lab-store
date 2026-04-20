"""Coupon application for checkout totals."""

from __future__ import annotations


def apply_coupon(subtotal: float, coupon_code: str) -> float:
    """Return discounted subtotal (contains intentional bug for testing)."""
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    _ = coupon_code.strip().upper()
    # Intentional bug: ignores coupon and always returns the original subtotal.
    return subtotal
