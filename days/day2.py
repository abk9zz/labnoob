import streamlit as st

from components.notebook import render_notebook
from components.postit import postit_hint


def render():
    left_content = """
    <h2>Day 2</h2>

    <p>The data suggests certain neurons are active during anxiety behavior.</p>

    <p>However, correlation is not enough.</p>

    <p>I need to determine whether these neurons <em>cause</em> the behavior.</p>

    <p>This requires direct manipulation.</p>
    """

    right_content = """
    <h3>Options</h3>
    <p>Optogenetics</p>
    <p>Pharmacology</p>
    """

    with render_notebook(left_content, right_content):
        postit_hint(
            "Causation",
            "To test causation, the experiment needs a way to manipulate neural activity "
            "and then observe whether behavior changes.",
        )

        with st.form("day2_form"):
            choice = st.radio("Choose a manipulation:", ["Optogenetics", "Pharmacology"])
            submitted = st.form_submit_button("Next Page ->")

        if submitted:
            if choice == "Optogenetics":
                st.session_state.score += 15
            else:
                st.session_state.score += 8

            st.session_state.day = 3
            st.rerun()
