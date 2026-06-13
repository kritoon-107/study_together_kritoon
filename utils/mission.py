import streamlit as st


def initialize_mission():

    if "lesson_done" not in st.session_state:
        st.session_state.lesson_done = False

    if "task_done" not in st.session_state:
        st.session_state.task_done = False

    # if "review_done" not in st.session_state:
    #     st.session_state.review_done = False

    if "mission_reward_claimed" not in st.session_state:
        st.session_state.mission_reward_claimed = False


def show_mission():

    st.markdown("## 🎯 Today's Mission")


    st.checkbox(
        "📚 Complete today's lesson",
        value=st.session_state.lesson_done,
        disabled=True
    )


    st.checkbox(
        "📝 Finish today's challenge",
        value=st.session_state.task_done,
        disabled=True
    )


    # st.checkbox(
    #     "🧠 Review today's concepts",
    #     value=st.session_state.review_done,
    #     disabled=True
    # )


    completed = (
        st.session_state.lesson_done
        + st.session_state.task_done
        # + st.session_state.review_done
    )


    progress = completed / 2


    st.progress(progress)


    st.caption(
        f"{completed}/2 missions completed"
    )