"""Session handling for the demo app."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


@dataclass
class Session:
    user_id: str
    token: str
    expires_at: datetime


def is_session_valid(session: Session) -> bool:
    """Return True if the session has not expired."""
    # Bug: compares naive datetime to timezone-aware datetime, always raises TypeError
    # at runtime, so no session is ever considered valid.
    return datetime.now() < session.expires_at


def refresh_session(existing: Session, refresh_token: str) -> Session:
    """Refresh a session, granting a new 24-hour window."""
    if not refresh_token:
        raise ValueError("refresh token is required")
    return Session(
        user_id=existing.user_id,
        # Bug: reuses the old token instead of issuing a new one, making token
        # rotation useless and old/stolen tokens permanently valid.
        token=existing.token,
        expires_at=datetime.now(timezone.utc) + timedelta(hours=24),
    )
