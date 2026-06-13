import streamlit as st


def initialize_gamification():
    if "xp" not in st.session_state:
        st.session_state.xp = 0

    if "level" not in st.session_state:
        st.session_state.level = "🌱 Beginner"

    if "badges" not in st.session_state:
        st.session_state.badges = []


def add_xp(points):

    st.session_state.xp += points


    # Level system
    if st.session_state.xp >= 500:
        st.session_state.level = "🚀 Data Scientist"

    elif st.session_state.xp >= 300:
        st.session_state.level = "🤖 ML Explorer"

    elif st.session_state.xp >= 150:
        st.session_state.level = "📊 Data Analyst"

    elif st.session_state.xp >= 50:
        st.session_state.level = "🐍 Python Explorer"


def add_badge(badge):

    if badge not in st.session_state.badges:
        st.session_state.badges.append(badge)