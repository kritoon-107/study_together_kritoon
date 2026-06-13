import streamlit as st


def show_sidebar():
    with st.sidebar:

        st.markdown(
            """
            # 🚀 Data Scientist Journey

            ### 👤 Explorer
            """
        )


        st.markdown("---")


        # Current stats
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "🔥 Streak",
                "0 Days"
            )

        with col2:
            st.metric(
                "📚 Day",
                "1"
            )


        st.markdown("### 📈 Your Progress")

        progress = 0.0

        st.progress(progress)

        st.caption("0% Complete")


        st.markdown("---")


        st.markdown(
            """
            ### 🎯 Today's Mission

            Complete today's lesson and finish the coding challenge.

            """
        )


        st.markdown("---")


        st.markdown(
            """
            ### 🧠 Daily Reminder

            > You don't need to know everything today.

            > Just become 1% better than yesterday.
            """
        )


        st.markdown("---")


        st.success(
            "🚀 Future Data Scientist Loading..."
        )