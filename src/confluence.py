from typing import List, Dict, Any
from .core import AssetLifecycleManager


class ConfluenceArchiver(AssetLifecycleManager):
    """
    Identifies outdated Confluence pages for archiving or review.
    """

    def get_archivable_pages(self, pages: List[Dict[str, Any]]) -> List[str]:
        archivable = []

        for page in pages:
            title = page.get("title")
            last_updated = page.get("last_updated")

            if not title or not last_updated:
                continue

            if page.get("is_active_project_page"):
                continue

            if self.is_stale(last_updated):
                archivable.append(title)

        return archivable