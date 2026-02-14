import streamlit as st

def recruiter_dashboard():
    st.markdown("## 🧑‍💼 Post a New Job")

    with st.form("post_job"):
        st.text_input("Job Title")
        st.text_input("Location")
        st.text_input("Skills (comma separated)")
        st.text_area("Description")
        if st.form_submit_button("Post Job"):
            st.success("Job posted!")

    st.markdown("---")
    st.markdown("### 📄 Your Posted Jobs")
    for job in st.session_state.jobs:
        st.markdown(f"""
        <div class="job-card">
            <div class="job-title">{job['title']}</div>
            <div class="job-meta">{job['location']}</div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("⬅ Back"):
        st.session_state.role = None
        st.rerun()
