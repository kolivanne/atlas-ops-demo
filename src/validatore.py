class OpsFlowValidator:
    """
    Basic Data Loss Prevention (DLP) layer for AI-related workflows.

    Prevents sensitive information from being passed into external AI tools.
    """

    def __init__(self):
        self.forbidden_terms = {
            "api_key",
            "password",
            "secret",
            "token",
            "player_id",
            "email",
        }

    def verify_payload(self, text: str) -> bool:
        """
        Returns False if sensitive terms are detected.
        """

        if not text:
            return True

        normalized = text.lower()

        for term in self.forbidden_terms:
            if term in normalized:
                return False

        return True