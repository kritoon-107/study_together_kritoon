import streamlit as st
import json
import os
import nbformat
from nbconvert import HTMLExporter
from utils.style_loader import load_css
from utils.sidebar import show_sidebar
from utils.mission import initialize_mission
import time


# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Today's Lesson",
    page_icon="📚",
    layout="wide"
)

load_css()
show_sidebar()
initialize_mission()
# -------------------------
# Load Lesson Data
# -------------------------
with open("data/lessons.json", "r", encoding="utf-8") as file:
    lessons = json.load(file)


# For now, always show Day 1
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

    with open(
        notebook_path,
        "r",
        encoding="utf-8"
    ) as f:
        notebook = nbformat.read(
            f,
            as_version=4
        )


    html_exporter = HTMLExporter()

    html_data, _ = html_exporter.from_notebook_node(
        notebook
    )


    st.components.v1.html(
        html_data,
        height=800,
        scrolling=True
    )

else:
    st.error(
        "Notebook file not found."
    )


# -------------------------
# End Message
# -------------------------

st.divider()

st.success(
    """
    🎉 Congratulations on completing today's lesson!

    Take a short break, then move to the Daily Task page.
    """
)

if st.button("📚 Mark Lesson Completed"):
    st.session_state.lesson_done = True
    
    st.success("🎉 Lesson completed! Great work 🚀")
    
    st.info("Redirecting to Home Page in 3 seconds...")
    
    time.sleep(3)
    
    st.switch_page("streamlit_app.py")