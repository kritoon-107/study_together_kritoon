import streamlit as st
from utils.style_loader import load_css
from utils.sidebar import show_sidebar


# -----------------------------
# Page Setup
# -----------------------------

st.set_page_config(
    page_title="Learning Path",
    page_icon="🗺️",
    layout="centered"
)

load_css()
show_sidebar()


# -----------------------------
# Roadmap Data
# -----------------------------

journey = [
    {
        "icon": "🐍",
        "title": "Python Fundamentals",
        "status": "current"
    },
    {
        "icon": "📊",
        "title": "NumPy & Pandas",
        "status": "locked"
    },
    {
        "icon": "📈",
        "title": "Data Visualization",
        "status": "locked"
    },
    {
        "icon": "📐",
        "title": "Statistics",
        "status": "locked"
    },
    {
        "icon": "🤖",
        "title": "Machine Learning",
        "status": "locked"
    },
    {
        "icon": "🚀",
        "title": "Real World Projects",
        "status": "locked"
    }
]


# -----------------------------
# Header
# -----------------------------

st.markdown("""
<div class="path-header">
<h1>🗺️ Your Data Science Journey</h1>
<p>
Every expert was once a beginner.
Keep climbing one step at a time.
</p>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Journey Nodes
# -----------------------------

for i, step in enumerate(journey):

    if step["status"] == "completed":
        badge = "✅ COMPLETED"
        css_class = "completed"

    elif step["status"] == "current":
        badge = "🎯 YOU ARE HERE"
        css_class = "current"

    else:
        badge = "🔒 LOCKED"
        css_class = "locked"


    st.markdown(
        f"""
        <div class="roadmap-card {css_class}">
            <h2>{step["icon"]}</h2>
            <h3>{step["title"]}</h3>
            <p>{badge}</p>
        </div>

        {"<div class='road-line'></div>" if i != len(journey)-1 else ""}
        """,
        unsafe_allow_html=True
    )


st.success(
    "🔥 Keep going. One lesson every day will transform your future."
)