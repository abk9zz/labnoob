import html

import streamlit as st


def render_letter(content: str):
    escaped = html.escape(content.strip())
    paragraphs = escaped.split("\n\n")
    formatted = "".join(f"<p>{paragraph.replace(chr(10), '<br>')}</p>" for paragraph in paragraphs)

    st.markdown(
        f"""
        <section class="letter-wrap">
            <article class="letter-paper">
                {formatted}
            </article>
        </section>
        """,
        unsafe_allow_html=True,
    )
