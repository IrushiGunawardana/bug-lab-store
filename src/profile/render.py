"""User profile rendering helpers."""

from __future__ import annotations


def render_profile_bio(raw_bio: str) -> str:
    """Render bio HTML (contains intentional XSS bug for testing)."""
    # Intentional bug: no escaping/sanitization before embedding user text.
    return f"<div class='bio'>{raw_bio}</div>"
