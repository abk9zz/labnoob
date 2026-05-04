import streamlit as st

from components.cards import get_clients, render_client_card
from components.navigation import go_to


def render():
    st.markdown(
        """
        <section class="app-shell">
            <p class="eyebrow">Contract Board</p>
            <h1>Choose a Client</h1>
            <p class="intro small centered-subtitle">
                Review the waiting contracts and select one hatchery commission to begin.
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    clients = get_clients()
    rows = [clients[index : index + 2] for index in range(0, len(clients), 2)]
    for row in rows:
        columns = st.columns(2)
        for column, client in zip(columns, row):
            with column:
                render_client_card(client)
                if st.button(
                    "Select Client",
                    key=f"select_client_{client['scenario_id']}",
                    use_container_width=True,
                ):
                    st.session_state.selected_client = client["name"]
                    st.session_state.scenario_id = client["scenario_id"]
                    st.session_state.species = None
                    st.session_state.constructs = [[]]
                    st.session_state.current_construct_index = 0
                    st.session_state.construct = st.session_state.constructs[0]
                    st.session_state.builder_result = None
                    go_to("client_letter")
