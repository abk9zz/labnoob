import streamlit as st


def postit_hint(title, content):
    with st.expander(title):
        st.markdown(f'<div class="postit">{content}</div>', unsafe_allow_html=True)
