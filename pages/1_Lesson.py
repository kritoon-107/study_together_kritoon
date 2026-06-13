import streamlit as st
import json
import os
import time

from utils.style_loader import load_css
from utils.sidebar import show_sidebar
from utils.mission import initialize_mission
from utils.notebook_reader import display_notebook


# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Today's Lesson",
    page_icon="📚",
    layout="wide"
)


# -------------------------
# Load Custom Style & Sidebar
# -------------------------
load_css()
show_sidebar()
initialize_mission()


# -------------------------
# Load Lesson Data
# -------------------------
with open(
    "data/lessons.json",
    "r",
    encoding="utf-8"
) as file:
    lessons = json.load(file)


# For now always show Day 1
lesson = lessons[0]


# -------------------------
# Header
# -------------------------
st.title("📚 Today's Lesson")


st.success(
    f"""
    Day {lesson['day']} - {lesson['title']}

    ⏱ Estimated Time: {lesson['time']}
    """
)


# -------------------------
# Mentor Message
# -------------------------
st.info(
    f"""
    👨‍🏫 Mentor Message

    {lesson['mentor_message']}
    """
)


# -------------------------
# Notebook Viewer
# -------------------------
st.subheader("📓 Learning Notebook")


notebook_path = os.path.join(
    "notebooks",
    lesson["notebook"]
)


if os.path.exists(notebook_path):

    display_notebook(
        notebook_path
    )

else:
    st.error(
        "❌ Notebook file not found."
    )


# -------------------------
# Learning Tip
# -------------------------
st.divider()


st.warning(
    """
    💡 Learning Tip

    Do not just read the notebook.
    
    Open Jupyter Notebook or Google Colab,
    type the code yourself, experiment with it,
    and try changing the examples.
    """
)


# -------------------------
# Completion Section
# -------------------------
st.success(
    """
    🎉 Congratulations on finishing today's lesson!

    You are one step closer to becoming a Data Scientist.
    """
)


if st.button(
    "📚 Mark Lesson Completed",
    use_container_width=True
):

    st.session_state.lesson_done = True

    st.balloons()

    st.success(
        "🎉 Lesson completed! Great work 🚀"
    )

    st.info(
        "Redirecting to Home Page in 3 seconds..."
    )

    time.sleep(3)

    st.switch_page(
        "streamlit_app.py"
    )