import streamlit as st


def render():
    score = st.session_state.score

    if score >= 25:
        text = """
        <h2>Final Entry</h2>

        <p>He looked through everything carefully.</p>

        <p>Then he nodded.</p>

        <p>"This is solid work."</p>

        <p>He paused.</p>

        <p>"But next time... maybe make your notebook less emotional."</p>

        <p>I think that's a success.</p>
        """
    else:
        text = """
        <h2>Final Entry</h2>

        <p>He flipped through my notebook.</p>

        <p>Then he asked about my controls.</p>

        <p>I didn't have a good answer.</p>

        <p>"You need to rethink your experimental design."</p>

        <p>Also... he said my notebook was unprofessional.</p>

        <p>Fair.</p>
        """

    st.markdown(f'<div class="page final-page">{text}</div>', unsafe_allow_html=True)
