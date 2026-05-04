import streamlit as st


def hint(title, content):
    with st.expander(title):
        st.markdown(f"<div class='postit-note'>{content}</div>", unsafe_allow_html=True)
