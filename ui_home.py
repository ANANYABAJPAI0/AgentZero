import streamlit as st

def home_page():
    st.markdown("""
        <div class="hero">
            <h1>Fair <span style="color:#044a8f;">Hiring</span> Network</h1>
            <p>Skill-first matching, bias-free hiring experiences for all.</p>
            <button class="btn-main" onclick="window.location.href='#candidate'">I'm a Candidate</button>
            <button class="btn-main" onclick="window.location.href='#recruiter'" style="margin-left:12px;">I'm a Recruiter</button>
        </div>
        <style>
            html { scroll-behavior: smooth; }
        </style>
    """, unsafe_allow_html=True)

    # Hidden anchors for navigation
    if st.button("I'm a Candidate", key="cand"):
        st.session_state.role = "candidate"
        st.rerun()
    if st.button("I'm a Recruiter", key="rech"):
        st.session_state.role = "recruiter"
        st.rerun()
