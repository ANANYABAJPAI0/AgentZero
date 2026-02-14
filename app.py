import streamlit as st

st.set_page_config(
    page_title="Fair Hiring Network",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from ui_home import home_page
from ui_candidate import candidate_dashboard
from ui_recruiter import recruiter_dashboard

# Session state
if "role" not in st.session_state:
    st.session_state.role = None

if "jobs" not in st.session_state:
    st.session_state.jobs = [
        {
            "title": "Software Engineer (Fresher)",
            "location": "Remote",
            "skills": ["Python", "DSA", "Git", "HTML"],
            "desc": "Resume-blind, skill-first hiring for early talent."
        },
        {
            "title": "ML Engineer Intern",
            "location": "Hybrid",
            "skills": ["Python", "ML", "Pandas", "Sklearn"],
            "desc": "Work on ethical AI and real-world ML pipelines."
        }
    ]

# Routing
if st.session_state.role is None:
    home_page()
elif st.session_state.role == "candidate":
    candidate_dashboard()
elif st.session_state.role == "recruiter":
    recruiter_dashboard()
