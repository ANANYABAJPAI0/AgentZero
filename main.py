from agents.fair_hiring_agent import FairHiringAgent
from data.candidate_sample import candidate_profile
from data.job_sample import job_description

def main():
    agent = FairHiringAgent()
    result = agent.evaluate(candidate_profile, job_description)

    print("\n--- FAIR HIRING NETWORK OUTPUT ---\n")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
