import streamlit as st

from days import day1, day2, day3, final
from styles.css import get_css


def initialize_state():
    if "day" not in st.session_state:
        st.session_state.day = 0
    if "score" not in st.session_state:
        st.session_state.score = 0


def render_sidebar():
    st.sidebar.title("Notebook Progress")
    st.sidebar.write(f"Day: {st.session_state.day}")
    st.sidebar.progress(min(st.session_state.day / 4, 1.0))

    if st.sidebar.button("Restart"):
        st.session_state.day = 0
        st.session_state.score = 0
        st.rerun()


def render_cover():
    st.markdown(
        """
        <div class="page cover-page">
            <h1>Lab Notebook</h1>

            <p>Name: ______________________</p>
            <p>Course: Biomedical Science Techniques</p>

            <hr>

            <p>This notebook documents my first attempt at designing an experiment.</p>
            <p>My PI expects results in one week.</p>
            <p>I don't fully understand what I'm doing yet... but I guess that's the point.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Open Notebook ->"):
        st.session_state.day = 1
        st.rerun()


def route_day():
    if st.session_state.day == 0:
        render_cover()
    elif st.session_state.day == 1:
        day1.render()
    elif st.session_state.day == 2:
        day2.render()
    elif st.session_state.day == 3:
        day3.render()
    else:
        final.render()


def main():
    st.set_page_config(layout="wide")
    st.markdown(get_css(), unsafe_allow_html=True)

    initialize_state()
    render_sidebar()
    route_day()


if __name__ == "__main__":
    main()
