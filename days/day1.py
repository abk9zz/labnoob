import streamlit as st

from components.notebook import render_notebook
from components.postit import postit_hint


def render():
    left_content = """
    <h2>Day 1</h2>

    <p>First day in the lab.</p>

    <p>My PI asked me to investigate neural circuits involved in anxiety.</p>

    <p>From what I understand, I need a technique that helps identify relevant cells.</p>

    <p>RNA-seq measures gene expression across many cells, but it lacks temporal resolution.</p>

    <p>Calcium imaging allows observation of neural activity in real time.</p>

    <p>I need to decide what kind of data is most useful.</p>
    """

    right_content = """
    <h3>Options</h3>
    <p>RNA-seq</p>
    <p>Calcium Imaging</p>
    """

    with render_notebook(left_content, right_content):
        postit_hint(
            "RNA-seq vs. calcium imaging",
            "RNA-seq is useful for discovering cell types and gene expression patterns. "
            "Calcium imaging is better when the question is about activity changing in real time.",
        )

        with st.form("day1_form"):
            choice = st.radio("Choose a technique:", ["RNA-seq", "Calcium Imaging"])
            submitted = st.form_submit_button("Next Page ->")

        if submitted:
            if choice == "RNA-seq":
                st.session_state.score += 5
            else:
                st.session_state.score += 10

            st.session_state.day = 2
            st.rerun()
