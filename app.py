import streamlit as st
from ui_home import home_page
from ui_candidate import candidate_dashboard
from ui_recruiter import recruiter_dashboard

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Fair Hiring Network", layout="wide")

# ---------------- SESSION STATE INIT ----------------
if "role" not in st.session_state:
    st.session_state.role = None

if "jobs" not in st.session_state:
    st.session_state.jobs = []

if "applications" not in st.session_state:
    st.session_state.applications = []

# ---------------- ROUTING ----------------
if st.session_state.role is None:
    home_page()

elif st.session_state.role == "candidate":
    candidate_dashboard()

elif st.session_state.role == "recruiter":
    recruiter_dashboard()
