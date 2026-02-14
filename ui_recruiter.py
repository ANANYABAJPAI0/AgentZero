import streamlit as st

def recruiter_dashboard():

    st.title("🧑‍💼 Recruiter Dashboard")
    st.markdown("---")

    # ---------------- POST JOB ----------------
    with st.form("post_job"):
        title = st.text_input("Job Title")
        location = st.text_input("Location")
        skills = st.text_input("Required Skills (comma separated)")

        submitted = st.form_submit_button("Post Job")

        if submitted:
            if title and skills:
                st.session_state.jobs.append({
                    "id": len(st.session_state.jobs),
                    "title": title,
                    "location": location,
                    "skills": [s.strip().lower() for s in skills.split(",")]
                })
                st.success("Job Posted Successfully!")
            else:
                st.warning("Please fill all required fields.")

    st.markdown("---")

    # ---------------- VIEW POSTED JOBS ----------------
    st.subheader("📄 Your Posted Jobs")

    if not st.session_state.jobs:
        st.info("No jobs posted yet.")

    for job in st.session_state.jobs:
        st.write(f"### {job['title']}")
        st.write(f"Location: {job['location']}")
        st.write(f"Skills: {', '.join(job['skills'])}")
        st.markdown("---")

    # ---------------- VIEW APPLICATIONS ----------------
    st.subheader("📥 Applications Received")

    if not st.session_state.applications:
        st.info("No applications yet.")

    for app in st.session_state.applications:

        st.write(f"### 👤 {app['name']}")
        st.write(f"Applied For: {app['job_title']}")
        st.write(f"Match Score: {app['score']}%")

        if app["decision"] == "Schedule Interview":
            st.success(f"🎉 {app['decision']}")
        elif app["decision"] == "Recruiter Review":
            st.warning(f"🕒 {app['decision']}")
        else:
            st.error(f"❌ {app['decision']}")

        st.markdown("---")

    # ---------------- BACK ----------------
    if st.button("⬅ Back to Home"):
        st.session_state.role = None
