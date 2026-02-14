from zynd.channel import ZyndChannel
from agents.bias_detection_agent import BiasDetectionAgent
from agents.skill_verification_agent import SkillVerificationAgent
from agents.privacy_guard_agent import PrivacyGuardAgent
from agents.audit_log_agent import AuditLogAgent

class FairHiringAgent:
    def __init__(self, agent_id="hiring_agent"):
        self.agent_id = agent_id
        self.zynd = ZyndChannel()

        self.bias_agent = BiasDetectionAgent()
        self.skill_agent = SkillVerificationAgent()
        self.privacy_agent = PrivacyGuardAgent()
        self.audit_agent = AuditLogAgent()

    def extract_skills(self, text: str):
        skills = ["python", "sql", "machine learning", "ml", "flask"]
        text = text.lower()
        return {s for s in skills if s in text}

    def evaluate(self, candidate_profile: str, job_description: str):

        privacy_report = self.zynd.send(
            self.agent_id, self.privacy_agent, candidate_profile
        )

        candidate_skills = self.extract_skills(candidate_profile)
        job_skills = self.extract_skills(job_description)

        matched = candidate_skills & job_skills
        score = int((len(matched) / len(job_skills)) * 100) if job_skills else 0

        bias_report = self.zynd.send(
            self.agent_id, self.bias_agent, job_description
        )

        verification = self.zynd.send(
            self.agent_id, self.skill_agent, candidate_profile
        )

        self.zynd.send(
            self.agent_id,
            self.audit_agent,
            f"Evaluation complete | score={score} | decision={'Recommended' if score >= 60 else 'Needs Review'}"
        )

        decision = "Recommended" if score >= 60 else "Needs Review"

        explanation = (
            f"Matched {len(matched)} of {len(job_skills)} required skills. "
            f"{bias_report['summary']}. "
            f"Skill verification confidence: {verification['confidence']}%. "
            "Demographic attributes were excluded by design."
        )

        return {
            "score": score,
            "matched": list(matched),
            "missing": list(job_skills - matched),
            "bias": bias_report,
            "verification": verification,
            "privacy": privacy_report,
            "decision": decision,
            "explanation": explanation,
            "zynd_logs": self.zynd.logs
        }
