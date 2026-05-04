import streamlit as st
import streamlit.components.v1 as components


def go_to(page):
    st.session_state.page = page
    st.session_state.scroll_to_top = True
    st.rerun()


def scroll_to_top_if_needed():
    if not st.session_state.pop("scroll_to_top", False):
        return

    components.html(
        """
        <script>
        const scrollTop = () => {
            const doc = window.parent.document;
            window.parent.scrollTo(0, 0);
            doc.documentElement.scrollTop = 0;
            doc.body.scrollTop = 0;

            const targets = [
                doc.scrollingElement,
                doc.querySelector('[data-testid="stAppViewContainer"]'),
                doc.querySelector('[data-testid="stMain"]'),
                doc.querySelector('section.main'),
                ...doc.querySelectorAll('div, section, main')
            ];

            targets.forEach((element) => {
                if (!element) return;
                element.scrollTop = 0;
            });
        };

        let attempts = 0;
        const interval = setInterval(() => {
            scrollTop();
            attempts += 1;
            if (attempts >= 12) clearInterval(interval);
        }, 50);
        </script>
        """,
        height=0,
    )
