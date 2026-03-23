from typing import List, Dict, Any
from .core import AssetLifecycleManager

class JiraTicketGovernance(AssetLifecycleManager):
    """
    Identifies tickets that require triage based on real-world Jira conditions.
    """

    def get_abandoned_tickets(self, tickets: List[Dict[str, Any]]) -> List[str]:
        abandoned = []

        for ticket in tickets:
            if not ticket.get('updated') or not ticket.get('key'):
                continue

            if ticket.get('resolution') is not None:
                continue

            if ticket.get('statusCategory') != 'To Do':
                continue

            if ticket.get('in_active_sprint'):
                continue

            if ticket.get('priority') in ['High', 'Blocker']:
                continue

            if self.is_stale(ticket['updated']):
                abandoned.append(ticket['key'])

        return abandoned