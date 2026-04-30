from contextlib import contextmanager

import streamlit as st


@contextmanager
def render_notebook(left_content, right_content, show_spine=True):
    left_col, spine_col, right_col = st.columns([1, 0.05, 1])

    with left_col:
        st.markdown(f'<div class="page notebook-page">{left_content}</div>', unsafe_allow_html=True)

    with spine_col:
        if show_spine:
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    with right_col:
        st.markdown(f'<div class="page notebook-page">{right_content}</div>', unsafe_allow_html=True)
        yield
