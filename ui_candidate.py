import streamlit as st

def candidate_dashboard():

    st.title("🎯 Candidate Dashboard")
    st.markdown("---")

    name = st.text_input("Your Name")
    candidate_skills = st.text_input("Your Skills (comma separated)")

    if "candidate_results" not in st.session_state:
        st.session_state.candidate_results = {}

    st.subheader("Available Jobs")

    if not st.session_state.jobs:
        st.info("No jobs available yet.")
        return

    for job in st.session_state.jobs:

        st.write(f"### {job['title']}")
        st.write(f"Location: {job['location']}")
        st.write(f"Required Skills: {', '.join(job['skills'])}")

        apply_key = f"apply_{job['id']}"

        if st.button(f"Apply to {job['title']}", key=apply_key):

            if not name or not candidate_skills:
                st.warning("Please enter your name and skills before applying.")
            else:
                candidate_list = [s.strip().lower() for s in candidate_skills.split(",")]

                required = job["skills"]
                matched = len(set(candidate_list) & set(required))
                total = len(required)
                score = int((matched / total) * 100) if total > 0 else 0

                if score >= 75:
                    decision = "Schedule Interview"
                elif score >= 50:
                    decision = "Recruiter Review"
                else:
                    decision = "Not Selected"

                st.session_state.candidate_results[job['id']] = {
                    "score": score,
                    "decision": decision
                }

                st.session_state.applications.append({
                    "name": name,
                    "job_title": job["title"],
                    "score": score,
                    "decision": decision
                })

        # Always display result
        if job['id'] in st.session_state.candidate_results:
            result = st.session_state.candidate_results[job['id']]

            st.markdown("#### 🧠 Application Result")

            if result["decision"] == "Schedule Interview":
                st.success(f"🎉 {result['decision']} (Score: {result['score']}%)")
            elif result["decision"] == "Recruiter Review":
                st.warning(f"🕒 {result['decision']} (Score: {result['score']}%)")
            else:
                st.error(f"❌ {result['decision']} (Score: {result['score']}%)")

    if st.button("⬅ Back to Home"):
        st.session_state.role = None
