import pytest
import datetime
from src.confluence import ConfluenceArchiver
from src.jira import JiraTicketGovernance

# --- Fixtures ---
@pytest.fixture
def conf_archiver():
    return ConfluenceArchiver(expiry_days=30)

@pytest.fixture
def jira_gov():
    return JiraTicketGovernance(expiry_days=30)

# --- Core & Confluence Tests ---
def test_confluence_happy_path(conf_archiver):
    """Happy Path: Identify a stale page."""
    stale_date = datetime.datetime.now() - datetime.timedelta(days=35)
    pages = [{"title": "Old Project", "last_updated": stale_date}]
    assert "Old Project" in conf_archiver.get_archivable_pages(pages)

def test_confluence_active_page_ignored(conf_archiver):
    """Edge Case: Stale date but marked as active project page."""
    stale_date = datetime.datetime.now() - datetime.timedelta(days=35)
    pages = [{
        "title": "Important Docs", 
        "last_updated": stale_date, 
        "is_active_project_page": True
    }]
    assert len(conf_archiver.get_archivable_pages(pages)) == 0

def test_confluence_invalid_data_handling(conf_archiver):
    """Negative Test: Missing keys should be skipped, not crash."""
    pages = [{"title": "Broken Page"}, {"last_updated": datetime.datetime.now()}]
    assert conf_archiver.get_archivable_pages(pages) == []

# --- Jira Specific Tests ---
def test_jira_abandoned_backlog_ticket(jira_gov):
    """Happy Path: Stale 'To Do' ticket is abandoned."""
    stale_date = datetime.datetime.now() - datetime.timedelta(days=40)
    tickets = [{
        "key": "GD-1", 
        "updated": stale_date, 
        "statusCategory": "To Do", 
        "resolution": None
    }]
    assert "GD-1" in jira_gov.get_abandoned_tickets(tickets)

def test_jira_high_priority_ignored(jira_gov):
    """Edge Case: Stale but High Priority/Blocker should be ignored."""
    stale_date = datetime.datetime.now() - datetime.timedelta(days=40)
    tickets = [{
        "key": "GD-911", 
        "updated": stale_date, 
        "statusCategory": "To Do", 
        "priority": "Blocker",
        "resolution": None
    }]
    assert jira_gov.get_abandoned_tickets(tickets) == []

def test_jira_resolved_tickets_ignored(jira_gov):
    """Negative Test: Already resolved tickets are never abandoned."""
    stale_date = datetime.datetime.now() - datetime.timedelta(days=40)
    tickets = [{
        "key": "GD-2", 
        "updated": stale_date, 
        "statusCategory": "To Do", 
        "resolution": "Done"
    }]
    assert jira_gov.get_abandoned_tickets(tickets) == []

# --- Shared Core Logic ---
def test_core_future_date(conf_archiver):
    """Edge Case: Future dates are not stale."""
    future = datetime.datetime.now() + datetime.timedelta(days=1)
    assert conf_archiver.is_stale(future) is False