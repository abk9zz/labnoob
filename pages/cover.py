import base64
from pathlib import Path

import streamlit as st

from components.navigation import go_to


LOGO_PATH = Path(__file__).resolve().parent.parent / "assets/images/logo.png"


def get_logo_data_uri():
    if not LOGO_PATH.exists():
        return ""

    encoded = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def render():
    logo_data_uri = get_logo_data_uri()
    logo_markup = f'<img class="cover-logo" src="{logo_data_uri}" alt="Emberfall logo">' if logo_data_uri else ""

    st.markdown(
        f"""
        <main class="app-shell cover-shell">
            {logo_markup}
            <p class="eyebrow">Royal Appointment Ledger</p>
            <h1>Emberfall Custom Dragon Hatchery</h1>
            <p class="intro centered-subtitle">
                The nests are warm, the eggs are humming, and today’s contracts are waiting.
                As an apprentice of Emberfall, your task is to match each client with a custom dragon design worthy of the Emberfall seal.
            </p>
        </main>
        """,
        unsafe_allow_html=True,
    )

    left, center, right = st.columns([1.4, 1, 1.4])
    with center:
        if st.button("Begin Assignment", use_container_width=True):
            go_to("clients")
