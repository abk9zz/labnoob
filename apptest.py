import streamlit as st

from components.navigation import scroll_to_top_if_needed
from components.scenarios import DEFAULT_SCENARIO_ID
from pages import builder, client_detail, clients, cover, scientist_notes
from styles.css import get_css


def initialize_state():
    if "page" not in st.session_state:
        st.session_state.page = "cover"
    if "selected_client" not in st.session_state:
        st.session_state.selected_client = None
    if "species" not in st.session_state:
        st.session_state.species = None
    if "scenario_id" not in st.session_state:
        st.session_state.scenario_id = DEFAULT_SCENARIO_ID


def route_page():
    routes = {
        "cover": cover.render,
        "clients": clients.render,
        "client_letter": client_detail.render,
        "scientist_letter": scientist_notes.render,
        "scientist_notes": scientist_notes.render,
        "builder": builder.render,
    }

    page = st.session_state.page
    if page not in routes:
        st.session_state.page = "cover"
        st.rerun()

    routes[page]()


def main():
    st.set_page_config(
        page_title="Emberfall Hatchery",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.markdown(get_css(), unsafe_allow_html=True)
    initialize_state()
    scroll_to_top_if_needed()
    route_page()


if __name__ == "__main__":
    main()
