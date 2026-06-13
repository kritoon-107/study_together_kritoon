import streamlit as st
import json
import time
import os
import random

from utils.style_loader import load_css
from utils.sidebar import show_sidebar
from utils.gamification import (
    initialize_gamification,
    add_xp,
    add_badge
)
from utils.mission import initialize_mission
from utils.notebook_reader import display_notebook


# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="Daily Task",
    page_icon="📝",
    layout="wide"
)


# -------------------------
# Load Theme & Features
# -------------------------

load_css()
show_sidebar()

initialize_gamification()
initialize_mission()


# -------------------------
# Load Task Data
# -------------------------

with open(
    "data/tasks.json",
    "r",
    encoding="utf-8"
) as file:
    tasks = json.load(file)


# Currently showing Day 1
task = tasks[0]


# -------------------------
# Header
# -------------------------

st.title("📝 Today's Challenge")


# st.success(
#     f"""
#     Day {task['day']} - {task['title']}

#     Difficulty: {task['difficulty']}
#     """
# )


# -------------------------
# Challenge Description
# -------------------------

# if "question" in task:
#     st.subheader("🎯 Challenge")

#     st.write(
#         task["question"]
#     )


# -------------------------
# Practice Notebook
# -------------------------

st.subheader(
    "📓 Practice Notebook"
)


task_path = os.path.join(
    "notebooks",
    "tasks",
    task["task_notebook"]
)


if os.path.exists(task_path):

    display_notebook(
        task_path
    )

    # Download notebook
    with open(
        task_path,
        "rb"
    ) as file:

        st.download_button(
            "⬇️ Download Practice Notebook",
            data=file,
            file_name=task["task_notebook"],
            mime="application/x-ipynb+json"
        )

else:

    st.error(
        "❌ Practice notebook not found."
    )


# -------------------------
# Hint Section
# -------------------------

# if "hint" in task:

#     with st.expander(
#         "💡 Need a Hint?"
#     ):
#         st.info(
#             task["hint"]
#         )


# -------------------------
# Student Coding Workspace
# -------------------------

st.subheader(
    "💻 Your Coding Workspace"
)


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


if st.button(
    "💾 Save My Code (Temporary)"
):

    st.session_state.student_code = (
        student_code
    )

    st.success(
        """
        Your code has been saved for this session.

        You can now compare your solution with the answer notebook.
        """
    )


# -------------------------
# Answer Notebook
# -------------------------

with st.expander(
    "📒 View Answer Notebook (Try First)"
):

    answer_path = os.path.join(
        "notebooks",
        "answers",
        task["answer_notebook"]
    )


    if os.path.exists(answer_path):

        display_notebook(
            answer_path
        )


        with open(
            answer_path,
            "rb"
        ) as file:

            st.download_button(
                "⬇️ Download Answer Notebook",
                data=file,
                file_name=task["answer_notebook"],
                mime="application/x-ipynb+json"
            )

    else:

        st.error(
            "❌ Answer notebook not found."
        )


# -------------------------
# Complete Task
# -------------------------

if st.button(
    "✅ I Completed Today's Task",
    use_container_width=True
):

    add_xp(
        25
    )

    add_badge(
        f"📝 Day {task['day']} Challenge Completed"
    )

    st.session_state.task_done = True


    st.balloons()


    st.success(
        """
        🎉 Amazing work!

        ⭐ +25 XP earned.

        Keep showing up every day and your skills will grow.
        """
    )


    st.info(
        "🏠 Redirecting to Home Page in 3 seconds..."
    )


    time.sleep(
        3
    )


    st.switch_page(
        "streamlit_app.py"
    )


# -------------------------
# Daily Motivation
# -------------------------

st.divider()


quotes = [

    "Every expert Data Scientist was once a beginner.",

    "The best way to learn Data Science is by writing code.",

    "Do not fear errors; they are part of the learning process.",

    "Consistency beats intensity. Learn a little every day.",

    "Small daily improvements lead to massive long-term growth."
]


st.info(
    "🌱 Daily Motivation\n\n"
    + random.choice(
        quotes
    )
)