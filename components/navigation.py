import streamlit as st


def go_to(page):
    st.session_state.page = page
    st.rerun()
