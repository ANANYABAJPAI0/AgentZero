class SkillVerificationAgent:
    def __init__(self, agent_id="skill_verifier"):
        self.agent_id = agent_id

    def receive(self, candidate_profile: str):
        profile = candidate_profile.lower()
        proofs = []

        if "github" in profile:
            proofs.append("GitHub profile")
        if "project" in profile:
            proofs.append("Project experience")
        if "cert" in profile:
            proofs.append("Certification")

        confidence = min(100, len(proofs) * 35)

        return {
            "verified": len(proofs) > 0,
            "proofs": proofs,
            "confidence": confidence
        }
