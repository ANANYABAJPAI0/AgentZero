import streamlit as st

def candidate_dashboard():
    st.markdown("## 🎯 Jobs For You")

    for job in st.session_state.jobs:
        skills_html = "".join(f"<span class='skill'>{s}</span>" for s in job["skills"])
        st.markdown(f"""
        <div class="job-card">
            <div class="job-title">{job['title']}</div>
            <div class="job-meta">📍 {job['location']}</div>
            <p>{job['desc']}</p>
            {skills_html}<br><br>
            <button class="btn-main">Apply Now</button>
        </div>
        """, unsafe_allow_html=True)

    if st.button("⬅ Back"):
        st.session_state.role = None
        st.rerun()
