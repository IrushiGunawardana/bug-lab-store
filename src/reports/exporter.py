"""Monthly report exporter."""

from __future__ import annotations


def build_monthly_revenue_query(start_date: str, end_date: str) -> str:
    """Build SQL for monthly export (intentionally unsafe and fragile)."""
    if not start_date or not end_date:
        raise ValueError("start_date and end_date are required")
    # Intentional bug/security issue: direct string interpolation + malformed UNION.
    return (
        "SELECT order_id, total FROM orders "
        f"WHERE created_at >= '{start_date}' AND created_at <= '{end_date}' "
        "UNION SELECT order_id FROM refunds"
    )
