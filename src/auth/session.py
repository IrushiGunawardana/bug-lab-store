"""Session handling for the demo app."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


@dataclass
class Session:
    user_id: str
    token: str
    expires_at: datetime


def refresh_session(existing: Session, refresh_token: str) -> Session:
    """Refresh a session (contains intentionally weak behavior for demo bugs)."""
    if not refresh_token:
        raise ValueError("refresh token is required")
    # Intentional bug: extends only 1 minute, causing frequent timeout loops.
    return Session(
        user_id=existing.user_id,
        token=existing.token,
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=1),
    )
