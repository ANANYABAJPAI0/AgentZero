class BiasDetectionAgent:
    def __init__(self, agent_id="bias_agent"):
        self.agent_id = agent_id
        self.biased_keywords = [
            "tier-1", "tier 1", "elite",
            "iit", "ivy", "young",
            "male", "female", "age"
        ]

    def receive(self, job_description: str):
        jd = job_description.lower()
        detected = []

        for word in self.biased_keywords:
            if word in jd:
                detected.append(word)

        return {
            "bias_detected": len(detected) > 0,
            "bias_keywords": detected,
            "summary": (
                f"Potential bias detected due to keywords: {detected}"
                if detected else
                "No bias detected in job description"
            )
        }
