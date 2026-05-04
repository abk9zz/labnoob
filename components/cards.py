import streamlit as st

from components.client import get_client
from components.scenarios import SCENARIOS


def get_clients():
    return [
        {
            **scenario["client"],
            "scenario_id": scenario_id,
            "difficulty": scenario["difficulty"],
        }
        for scenario_id, scenario in SCENARIOS.items()
    ]


def get_selected_client():
    if not st.session_state.get("selected_client"):
        return None
    return get_client(st.session_state.get("scenario_id"))


def render_client_card(client):
    st.markdown(
        f"""
        <article class="contract-card">
            <span class="trial-badge">{client["difficulty"]}</span>
            <h3>{client["name"]}</h3>
            <p class="client-role">{client["title"]}</p>
            <p>{client["short_description"]}</p>
        </article>
        """,
        unsafe_allow_html=True,
    )
