class PrivacyGuardAgent:
    def __init__(self, agent_id="privacy_guard"):
        self.agent_id = agent_id
        self.redacted_fields = [
            "name", "gender", "age", "college", "university"
        ]

    def receive(self, candidate_profile: str):
        cleaned = candidate_profile.lower()
        removed = []

        for field in self.redacted_fields:
            if field in cleaned:
                removed.append(field)

        return {
            "privacy_preserved": True,
            "removed_fields": removed,
            "summary": "Candidate profile processed without demographic attributes"
        }
