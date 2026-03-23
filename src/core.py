import datetime
from typing import Optional

class AssetLifecycleManager:
    """
    Shared utility for lifecycle decisions (e.g. stale tickets, outdated pages).

    Designed to be simple and configurable rather than overly abstract.
    """

    def __init__(self, expiry_days: int):
        self.expiry_days = expiry_days

    def is_stale(self, last_updated: Optional[datetime.datetime]) -> bool:
        """
        Determines whether an asset is considered stale.

        Rules:
        - None values are treated as invalid → not stale
        - Future dates are ignored
        - Uses configurable expiry threshold
        """
        if not last_updated:
            return False

        now = datetime.datetime.now()

        # Ignore invalid future timestamps
        if last_updated > now:
            return False

        delta = now - last_updated
        return delta.days > self.expiry_days