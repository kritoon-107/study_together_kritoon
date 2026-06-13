import streamlit as st


def load_css():
    with open(
        "assets/style.css",
        "r",
        encoding="utf-8"
    ) as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True
        )