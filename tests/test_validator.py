import pytest
from src.validator import OpsFlowValidator

@pytest.fixture
def validator():
    return OpsFlowValidator()

def test_validator_happy_path_clean(validator):
    """Happy Path: Standard business text passes."""
    text = "Please review the Jira workflow for the new sprint."
    assert validator.verify_payload(text) is True

def test_validator_detects_forbidden_terms(validator):
    """Negative Test: Detects secrets regardless of case."""
    assert validator.verify_payload("My PASSWORD is secret123") is False
    assert validator.verify_payload("Found an api_key in the logs") is False

def test_validator_substring_match(validator):
    """Edge Case: Detects terms even when part of a string."""
    assert validator.verify_payload("the_token_is_here") is False

def test_validator_empty_handling(validator):
    """Edge Case: None or empty strings should pass (nothing to leak)."""
    assert validator.verify_payload("") is True
    assert validator.verify_payload(None) is True