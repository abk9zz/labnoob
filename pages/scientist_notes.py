import streamlit as st

from components.navigation import go_to
from components.scenarios import get_scenario
from components.ui import render_letter


def render():
    st.markdown(
        """
        <section class="app-shell">
            <p class="eyebrow">Lead Scientist Notes</p>
            <h1>Design Guidance</h1>
        </section>
        """,
        unsafe_allow_html=True,
    )
    render_letter(get_scenario(st.session_state.get("scenario_id"))["scientist_letter"])
    st.markdown(
        """
        <div class="transition-note">
            Next, you will construct your system.
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)
    with left:
        if st.button("Back to Client Letter", use_container_width=True):
            go_to("client_letter")
    with right:
        if st.button("Proceed to Genome Builder", use_container_width=True):
            go_to("builder")
