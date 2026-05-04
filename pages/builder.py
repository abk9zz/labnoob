import streamlit as st

from components.client import get_client
from components.evaluator import evaluate_construct
from components.genome_builder import run_builder
from components.library import render_library
from components.navigation import go_to
from components.scenarios import get_scenario


def render_request():
    scenario = get_scenario(st.session_state.get("scenario_id"))
    client = get_client(st.session_state.get("scenario_id"))
    species = st.session_state.get("species") or scenario["species"]["name"]
    st.session_state.species = species
    st.markdown(
        f"""
        <section class="app-shell detail-panel">
            <div class="species-pill">Species: {species}</div>
            <div class="trial-assignment">
                <strong>{scenario["assignment_label"]}</strong>
                <p>{scenario["assignment_description"]}</p>
            </div>
            <p class="eyebrow">Active Contract</p>
            <h1>{scenario["builder_title"]}</h1>
            <h2>{client["name"]} -- {client["title"]}</h2>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_scientist_guidance():
    scenario = get_scenario(st.session_state.get("scenario_id"))
    guidance = "".join(f"<li>{item}</li>" for item in scenario["guidance"])
    goal = f"<strong>{scenario['goal']}</strong>" if scenario.get("goal") else ""
    st.markdown(
        f"""
        <div class="scientist-guidance">
            <ul>{guidance}</ul>
            {goal}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_submission():
    st.markdown("<h3 class='section-heading'>Submit Design</h3>", unsafe_allow_html=True)
    submit_col, status_col = st.columns([1, 2])

    with submit_col:
        if st.button("Submit construct", type="primary", use_container_width=True):
            st.session_state.builder_result = evaluate_construct(
                st.session_state.constructs,
                species=st.session_state.get("species"),
                scenario=get_scenario(st.session_state.get("scenario_id")),
            )
            st.rerun()

    with status_col:
        constructs = st.session_state.get("constructs", [[]])
        part_count = sum(len(construct) for construct in constructs)
        st.markdown(
            f"<div class='submission-status'><strong>{part_count}</strong> components across {len(constructs)} construct(s)</div>",
            unsafe_allow_html=True,
        )


def render_results():
    result = st.session_state.get("builder_result")
    if result is None:
        return

    score = result["score"]
    if score >= 80:
        st.success(f"Score: {score}/100")
    elif score >= 50:
        st.warning(f"Score: {score}/100")
    else:
        st.error(f"Score: {score}/100")

    issue_items = "".join(f"<li>{issue}</li>" for issue in result["issues"])
    if not issue_items:
        issue_items = f"<li>No issues detected. The construct satisfies {result.get('scenario', 'the active scenario')}.</li>"

    st.markdown(
        f"""
        <div class="result-panel">
            <h3>Evaluation</h3>
            <p><strong>{result["outcome"].title()}</strong></p>
            <p>{result["feedback"]}</p>
            <ul>{issue_items}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render():
    render_request()
    render_scientist_guidance()

    if "show_component_library" not in st.session_state:
        st.session_state.show_component_library = False

    if st.button("📚 View Available Components", use_container_width=True):
        st.session_state.show_component_library = not st.session_state.show_component_library

    if st.session_state.show_component_library:
        render_library()

    st.divider()
    run_builder()
    st.divider()
    render_submission()
    render_results()

    st.divider()
    left, right = st.columns([1, 1])
    with left:
        if st.button("Back to Scientist Notes", use_container_width=True):
            go_to("scientist_letter")
    with right:
        if st.button("New Client", use_container_width=True):
            st.session_state.selected_client = None
            st.session_state.species = None
            go_to("clients")
