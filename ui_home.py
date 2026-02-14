import streamlit as st

def home_page():

    st.title("Fair Hiring Network")
    st.markdown("---")

    st.header("Redefining Hiring with Trust & Skills")
    st.write("AI-powered evaluation using Zynd Agent Network")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("I'm a Recruiter"):
            st.session_state.role = "recruiter"

    with col2:
        if st.button("I'm a Candidate"):
            st.session_state.role = "candidate"
