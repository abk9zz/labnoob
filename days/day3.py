import streamlit as st

from components.notebook import render_notebook
from components.postit import postit_hint


def render():
    left_content = """
    <h2>Day 5</h2>

    <p>I present tomorrow.</p>

    <p>I'm reviewing everything and realizing something important:</p>

    <p>Without proper controls, my results may not be valid.</p>

    <p>This might be the most critical decision.</p>
    """

    right_content = """
    <h3>Options</h3>
    <p>Include controls</p>
    <p>Skip controls</p>
    """

    with render_notebook(left_content, right_content):
        postit_hint(
            "Controls",
            "Controls help show whether the result comes from the experimental variable "
            "instead of a confound, artifact, or expectation.",
        )

        with st.form("day3_form"):
            choice = st.radio("Choose a control plan:", ["Include controls", "Skip controls"])
            submitted = st.form_submit_button("Next Page ->")

        if submitted:
            if choice == "Include controls":
                st.session_state.score += 15
            else:
                st.session_state.score -= 20

            st.session_state.day = 4
            st.rerun()
