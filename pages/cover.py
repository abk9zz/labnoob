import streamlit as st

from components.navigation import go_to


def render():
    st.markdown(
        """
        <main class="app-shell cover-shell">
            <p class="eyebrow">Royal Appointment Ledger</p>
            <h1>Emberfall Custom Dragon Hatchery</h1>
            <p class="intro centered-subtitle">
                The forge is warm, the eggs are humming, and today's contracts are waiting.
                Match each client with a custom dragon design worthy of the Emberfall seal.
            </p>
        </main>
        """,
        unsafe_allow_html=True,
    )

    left, center, right = st.columns([1.4, 1, 1.4])
    with center:
        if st.button("Begin Assignment", use_container_width=True):
            go_to("clients")
