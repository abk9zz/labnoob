import streamlit as st

from components.genome_builder import get_component_groups


def render_library():
    st.markdown("<h3 class='section-heading'>Component Reference Panel</h3>", unsafe_allow_html=True)

    for section, items in get_component_groups().items():
        with st.expander(section, expanded=section == "Promoters"):
            for component in items:
                st.markdown(
                    f"""
                    <div class="library-item">
                        <strong>{component["label"]}</strong>
                        <p>{component["description"]}</p>
                        <span>{component["role"]}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
