import streamlit as st

from components.navigation import go_to
from components.scenarios import get_scenario
from components.ui import render_letter


def get_client_letter():
    return get_scenario(st.session_state.get("scenario_id"))["client_letter"]


def render():
    st.markdown(
        """
        <section class="app-shell">
            <p class="eyebrow">Client Letter</p>
            <h1>Contract Request</h1>
        </section>
        """,
        unsafe_allow_html=True,
    )
    render_letter(get_client_letter())

    left, right = st.columns(2)
    with left:
        if st.button("Back to Clients", use_container_width=True):
            st.session_state.selected_client = None
            go_to("clients")
    with right:
        if st.button("Review Notes from Lead Scientist", use_container_width=True):
            go_to("scientist_letter")
