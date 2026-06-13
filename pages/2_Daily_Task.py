import streamlit as st
import json
import time
import os
import random
import nbformat
from nbconvert import HTMLExporter


from utils.style_loader import load_css
from utils.sidebar import show_sidebar
from utils.gamification import (
    initialize_gamification,
    add_xp,
    add_badge
)
from utils.mission import initialize_mission


# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="Daily Task",
    page_icon="📝",
    layout="wide"
)

load_css()
show_sidebar()
initialize_gamification()
initialize_mission()


# -------------------------
# Helper Function
# -------------------------

def show_notebook(path, height=600):
    if os.path.exists(path):

        with open(path, "r", encoding="utf-8") as file:
            notebook = nbformat.read(
                file,
                as_version=4
            )

        exporter = HTMLExporter()
        html, _ = exporter.from_notebook_node(notebook)

        st.components.v1.html(
            html,
            height=height,
            scrolling=True
        )

    else:
        st.error("Notebook not found.")


# -------------------------
# Load Task Data
# -------------------------

with open(
    "data/tasks.json",
    "r",
    encoding="utf-8"
) as file:
    tasks = json.load(file)


task = tasks[0]


# -------------------------
# Header
# -------------------------

st.title("📝 Today's Challenge")


st.success(
    f"""
    Day {task['day']} - {task['title']}

    Difficulty: {task['difficulty']}
    """
)


# -------------------------
# Problem
# -------------------------

st.subheader("🎯 Challenge")

# st.write(task["question"])


# -------------------------
# Task Notebook
# -------------------------

st.subheader("📓 Practice Notebook")


task_path = os.path.join(
    "notebooks",
    "tasks",
    task["task_notebook"]
)


show_notebook(task_path)


with open(task_path, "rb") as file:
    st.download_button(
        "⬇️ Download Practice Notebook",
        file,
        file_name=task["task_notebook"],
        mime="application/x-ipynb+json"
    )


# -------------------------
# Hint
# -------------------------

# with st.expander("💡 Need a Hint?"):
#     st.info(task["hint"])


# -------------------------
# Answer Notebook
# -------------------------

st.subheader("💻 Your Coding Workspace")

student_code = st.text_area(
    "Write your Python solution here:",
    height=250,
    placeholder="""
# Write your solution here

# Example:
numbers = [1, 2, 3, 4, 5]

print(numbers)
"""
)


if st.button("💾 Save My Code (Temporary)"):
    st.session_state.student_code = student_code

    st.success(
        "Your code has been saved for this session. Now you can See the Answers"
    )


with st.expander("📒 View Answer Notebook (Try First)"):
    
    answer_path = os.path.join(
        "notebooks",
        "answers",
        task["answer_notebook"]
    )

    show_notebook(answer_path)

    with open(answer_path, "rb") as file:
        st.download_button(
            "⬇️ Download Answer Notebook",
            file,
            file_name=task["answer_notebook"],
            mime="application/x-ipynb+json"
        )


# -------------------------
# Complete Task
# -------------------------

if st.button("✅ I Completed Today's Task"):

    add_xp(25)

    add_badge(
        f"📝 Day {task['day']} Challenge Completed"
    )

    st.session_state.task_done = True

    st.balloons()

    st.success(
        """
        🎉 Amazing work!

        ⭐ +25 XP earned.

        Keep showing up every day.
        """
    )

    st.info(
        "🏠 Redirecting to Home Page in 3 seconds..."
    )

    time.sleep(3)

    st.switch_page("streamlit_app.py")


# -------------------------
# Motivation
# -------------------------

st.divider()


quotes = [
    "Every expert Data Scientist was once a beginner.",
    "The best way to learn Data Science is by writing code.",
    "Do not fear errors; they are part of the learning process.",
    "Consistency beats intensity. Learn a little every day."
]


st.info(
    "🌱 Daily Motivation\n\n" +
    random.choice(quotes)
)