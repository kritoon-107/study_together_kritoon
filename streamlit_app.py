import streamlit as st
from utils.style_loader import load_css
from utils.sidebar import show_sidebar
from utils.gamification import initialize_gamification
from utils.mission import initialize_mission, show_mission

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="Data Science Journey",
    page_icon="🚀",
    layout="wide"
)
load_css()
show_sidebar()
initialize_gamification()
initialize_mission()
# -------------------------
# Hero Section
# -------------------------

st.markdown(
    """
    <div class="custom-card">

    <h2>🚀 Welcome to Data Science Journey</h2>

    <p>
    Learn Data Science one small step every day.
    No pressure. No rushing.
    Just consistent growth.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)
show_mission()




st.subheader(
    "Learn Data Science one small step every day."
)


st.write(
    """
    A guided journey designed to take you from
    complete beginner to building real Data Science projects.
    """
)


col1, col2 = st.columns([1, 1])


with col1:
    if st.button(
        "📚 Start Today's Lesson",
        use_container_width=True
    ):
        st.switch_page(
            "pages/1_Lesson.py"
        )


with col2:
    if st.button(
        "📝 Go To Today's Task",
        use_container_width=True
    ):
        st.switch_page(
            "pages/2_Daily_Task.py"
        )



st.divider()


# -------------------------
# Learning Journey
# -------------------------

st.header("🗺️ Your Journey")


journey = [
    ("🐍", "Python Programming"),
    ("📊", "NumPy & Pandas"),
    ("📈", "Data Visualization"),
    ("📐", "Statistics"),
    ("🤖", "Machine Learning"),
    ("🚀", "Projects")
]


cols = st.columns(len(journey))


for col, item in zip(cols, journey):
    icon, title = item

    with col:
        st.markdown(
            f"""
            ### {icon}

            {title}
            """
        )


st.divider()


# -------------------------
# Course Features
# -------------------------

st.header("✨ What Makes This Journey Different")


st.markdown(
    """
    - 📚 One focused lesson each day  
    - 🧠 Small exercises that build confidence  
    - 💡 Hints whenever you feel stuck  
    - 🎯 No overwhelming content  
    - 🚀 Learn by doing, not memorizing  
    """
)


st.divider()


# -------------------------
# Motivation
# -------------------------

st.success(
    """
    🌱 Remember:

    You don't become a Data Scientist in one day.
    You become one by showing up every day.
    """
)


# -------------------------
# Footer
# -------------------------

st.caption(
    "Built with ❤️ for consistent learners"
)



# -------------------------
# XP Page
# -------------------------

st.header("🏆 Your Profile")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "⭐ XP",
        st.session_state.xp
    )


with col2:
    st.metric(
        "🎖 Level",
        st.session_state.level
    )


st.progress(
    min(st.session_state.xp / 500, 1.0)
)

st.caption("Keep learning to reach Data Scientist level 🚀")

st.header("🏅 Achievements")

if st.session_state.badges:

    for badge in st.session_state.badges:
        st.success(badge)

else:
    st.info(
        "Complete your first challenge to unlock badges!"
    )