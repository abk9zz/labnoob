import streamlit as st


COMPONENT_GROUPS = {
    "Promoters": [
        {
            "id": "constitutive_promoter",
            "label": "Constitutive promoter",
            "display": "Constitutive promoter",
            "symbol": "pCON",
            "role": "Constitutive promoter",
            "description": "Constitutive promoter that drives broad gene expression across many cell types.",
        },
        {
            "id": "wing_pattern_promoter",
            "label": "Wing pattern promoter",
            "display": "Wing pattern promoter",
            "symbol": "pWING",
            "role": "Tissue-specific promoter",
            "description": "Tissue-specific promoter active only in wing pattern cells.",
        },
        {
            "id": "laryngeal_gland_promoter",
            "label": "Laryngeal gland promoter",
            "display": "Laryngeal gland promoter",
            "symbol": "pLAR",
            "role": "Tissue-specific promoter",
            "description": "Tissue-specific promoter active in laryngeal combustion glands.",
        },
        {
            "id": "glandular_promoter",
            "label": "Glandular promoter",
            "display": "Glandular promoter",
            "symbol": "pGLAND",
            "role": "Broad secretory promoter",
            "description": "Broad secretory promoter active in mist-producing glands and other secretory cells.",
        },
        {
            "id": "airway_promoter",
            "label": "Airway promoter",
            "display": "Airway promoter",
            "symbol": "pAIR",
            "role": "Tissue-specific promoter",
            "description": "Tissue-specific promoter active in respiratory epithelial cells.",
        },
        {
            "id": "heat_responsive_promoter",
            "label": "Heat-responsive promoter",
            "display": "Heat-responsive promoter",
            "symbol": "pHEAT",
            "role": "Temperature-sensitive promoter",
            "description": "Temperature-sensitive promoter that activates transcription under high-temperatures.",
        },
        {
            "id": "teto_promoter",
            "label": "TetO promoter",
            "display": "TetO promoter",
            "symbol": "TetO",
            "role": "Inducible promoter",
            "description": "Inducible promoter activated by rtTA when doxycycline is present.",
        },
        {
            "id": "venom_gland_promoter",
            "label": "Venom gland promoter",
            "display": "Venom gland promoter",
            "symbol": "pVEN",
            "role": "Tissue-specific promoter",
            "description": "Tissue-specific promoter active in venom-producing glands.",
        },
        {
            "id": "molting_stage_promoter",
            "label": "Molting-stage promoter",
            "display": "Molting-stage promoter",
            "symbol": "pMOLT",
            "role": "Developmental promoter",
            "description": "Developmental promoter active during the first maturity molt, regulated by hormone-driven transcriptional changes.",
        },
        {
            "id": "night_active_promoter",
            "label": "Night-active promoter",
            "display": "Night-active promoter",
            "symbol": "pNIGHT",
            "role": "Circadian promoter",
            "description": "Circadian promoter that drives gene expression during the night phase of the internal biological clock.",
        },
        {
            "id": "scale_pigment_promoter",
            "label": "Scale pigment promoter",
            "display": "Scale pigment promoter",
            "symbol": "pSCALE",
            "role": "Tissue-specific promoter",
            "description": "Tissue-specific promoter active in pigment-producing scale cells.",
        },
        {
            "id": "nucleus_accumbens_promoter",
            "label": "Nucleus accumbens promoter",
            "display": "Nucleus accumbens promoter",
            "symbol": "pNAcc",
            "role": "Region-specific promoter",
            "description": "Region-specific promoter active in nucleus accumbens neurons.",
        },
        {
            "id": "reward_neuron_promoter",
            "label": "Reward-neuron promoter",
            "display": "Reward-neuron promoter",
            "symbol": "pREWARD",
            "role": "Cell-type promoter",
            "description": "Cell-type promoter active in reward-sensitive neuron populations.",
        },
        {
            "id": "oxytocin_neuron_promoter",
            "label": "Oxytocin-neuron promoter",
            "display": "Oxytocin-neuron promoter",
            "symbol": "pOXY",
            "role": "Cell-type exclusion promoter",
            "description": "Promoter active in oxytocin-producing neurons involved in social bonding and attachment behaviors.",
        },
    ],
    "Control Systems": [
        {
            "id": "rtta",
            "label": "rtTA activator",
            "display": "rtTA activator",
            "symbol": "rtTA",
            "role": "Tet-On transcription factor",
            "description": "Doxycycline-responsive transcriptional activator. It activates TetO-controlled expression only when doxycycline is present.",
        },
        {
            "id": "gal4",
            "label": "GAL4",
            "display": "GAL4",
            "symbol": "GAL4",
            "role": "Transcriptional activator",
            "description": "Transcriptional activator that binds UAS and turns on UAS-linked genes.",
        },
        {
            "id": "uas",
            "label": "UAS",
            "display": "UAS",
            "symbol": "UAS",
            "role": "Upstream activating sequence",
            "description": "Upstream activating sequence that requires GAL4 to drive expression.",
        },
        {
            "id": "gal80",
            "label": "GAL80 repressor",
            "display": "GAL80 repressor",
            "symbol": "GAL80",
            "role": "GAL4 repression",
            "description": "Repressor that binds GAL4 and prevents GAL4 from activating UAS-linked genes.",
        },
        {
            "id": "cre",
            "label": "Cre recombinase",
            "display": "Cre recombinase",
            "symbol": "Cre",
            "role": "Recombinase switch",
            "description": "Site-specific recombinase that recognizes loxP sequences.",
        },
        {
            "id": "loxp",
            "label": "loxP site",
            "display": "loxP site",
            "symbol": "loxP",
            "role": "Cre recognition site",
            "description": "DNA recognition sequence targeted by Cre recombinase.",
        },
        {
            "id": "cre_ert",
            "label": "Cre-ERT",
            "display": "Cre-ERT",
            "symbol": "Cre-ERT",
            "role": "Drug-activated recombinase",
            "description": "Drug-activated recombinase system that becomes active only after handler-administered activation.",
        },
        {
            "id": "flp",
            "label": "FLP recombinase",
            "display": "FLP recombinase",
            "symbol": "FLP",
            "role": "Recombinase switch",
            "description": "Site-specific recombinase that recognizes FRT sequences.",
        },
        {
            "id": "frt",
            "label": "FRT site",
            "display": "FRT site",
            "symbol": "FRT",
            "role": "FLP recognition site",
            "description": "DNA recognition sequence targeted by FLP recombinase.",
        },
    ],
    "Genes": [
        {
            "id": "pyroxin_a6",
            "label": "Pyroxin-A6",
            "display": "Pyroxin-A6",
            "symbol": "PYX-A6",
            "role": "Effector gene",
            "description": "Thermogenic effector protein responsible for combustion and heat generation.",
        },
        {
            "id": "pyroxin_a23",
            "label": "Pyroxin-A23",
            "display": "Pyroxin-A23",
            "symbol": "PYX-A23",
            "role": "Effector gene",
            "description": "Thermogenic effector protein that drives high-intensity combustion and extreme heat output. Functional variant of Pyroxin-A6 with enhanced activity.",
        },
        {
            "id": "lumina_blue",
            "label": "Lumina-Blue",
            "display": "Lumina-Blue",
            "symbol": "LUM-B",
            "role": "Bioluminescent protein",
            "description": "Bioluminescent protein that produces blue glow.",
        },
        {
            "id": "lumina_green",
            "label": "Lumina-Green",
            "display": "Lumina-Green",
            "symbol": "LUM-G",
            "role": "Bioluminescent protein",
            "description": "Bioluminescent protein that produces green glow.",
        },
        {
            "id": "lumina_gold",
            "label": "Lumina-Gold",
            "display": "Lumina-Gold",
            "symbol": "LUM-AU",
            "role": "Bioluminescent protein",
            "description": "Bioluminescent protein that produces gold glow.",
        },
        {
            "id": "aureolin",
            "label": "Aureolin",
            "display": "Aureolin",
            "symbol": "AUR",
            "role": "Therapeutic protein",
            "description": "Therapeutic protein that supports wound repair when secreted as healing mist.",
        },
        {
            "id": "virexin",
            "label": "Virexin",
            "display": "Virexin",
            "symbol": "VEN-X",
            "role": "Effector protein",
            "description": "Effector protein responsible for venom production.",
        },
        {
            "id": "nyxmelanin",
            "label": "Nyxmelanin",
            "display": "Nyxmelanin",
            "symbol": "NYX-MEL",
            "role": "Pigment effector",
            "description": "Pigment effector responsible for dark, light-absorbing scale coloration.",
        },
        {
            "id": "girk_channel",
            "label": "GIRK channel",
            "display": "GIRK channel",
            "symbol": "GIRK",
            "role": "Neural modulator",
            "description": "Neural effector that reduces overactivation by increasing inhibitory potassium channel signaling without damaging neurons.",
        },
        {
            "id": "gaba_amplifier",
            "label": "GABA-Amplifier",
            "display": "GABA-Amplifier",
            "symbol": "GABA-AMP",
            "role": "Strong neural inhibitor",
            "description": "Strong inhibitory effector that broadly suppresses neural activity through enhanced inhibitory signaling.",
        },
    ],
    "Special Elements": [
        {
            "id": "stop_cassette",
            "label": "STOP cassette",
            "display": "STOP cassette",
            "symbol": "STOP",
            "role": "Transcriptional block",
            "description": "Transcriptional blocking sequence that prevents expression of downstream genes.",
        },
        {
            "id": "polya_terminator",
            "label": "PolyA terminator",
            "display": "PolyA terminator",
            "symbol": "PolyA",
            "role": "Transcription terminator",
            "description": "Sequence that signals the end of transcription and adds a polyadenylation tail.",
        },
    ],
}


ORIENTATIONS = ["Forward", "Reverse"]

ALL_COMPONENTS = {
    group: [component["id"] for component in components]
    for group, components in COMPONENT_GROUPS.items()
}

COMPONENT_BY_ID = {
    group: {component["id"]: component for component in components}
    for group, components in COMPONENT_GROUPS.items()
}

SCENARIO_COMPONENTS = {
    "trial": {
        "Promoters": ["laryngeal_gland_promoter", "constitutive_promoter"],
        "Control Systems": [],
        "Genes": ["pyroxin_a6"],
        "Special Elements": ["polya_terminator"],
    },
    "scenario_1": {
        "Promoters": ["laryngeal_gland_promoter", "constitutive_promoter"],
        "Control Systems": [],
        "Genes": ["pyroxin_a6"],
        "Special Elements": ["polya_terminator"],
    },
    "gal4": {
        "Promoters": ["wing_pattern_promoter", "constitutive_promoter"],
        "Control Systems": ["gal4", "uas"],
        "Genes": ["lumina_blue", "lumina_green", "lumina_gold"],
        "Special Elements": ["polya_terminator"],
    },
    "scenario_gal4_uas": {
        "Promoters": ["wing_pattern_promoter", "constitutive_promoter"],
        "Control Systems": ["gal4", "uas"],
        "Genes": ["lumina_blue", "lumina_green", "lumina_gold"],
        "Special Elements": ["polya_terminator"],
    },
    "gal80": {
        "Promoters": ["glandular_promoter", "airway_promoter", "constitutive_promoter"],
        "Control Systems": ["gal4", "uas", "gal80"],
        "Genes": ["aureolin"],
        "Special Elements": ["polya_terminator"],
    },
    "scenario_gal80_repression": {
        "Promoters": ["glandular_promoter", "airway_promoter", "constitutive_promoter"],
        "Control Systems": ["gal4", "uas", "gal80"],
        "Genes": ["aureolin"],
        "Special Elements": ["polya_terminator"],
    },
    "forge": {
        "Promoters": [
            "heat_responsive_promoter",
            "teto_promoter",
            "laryngeal_gland_promoter",
        ],
        "Control Systems": ["rtta"],
        "Genes": ["pyroxin_a6"],
        "Special Elements": ["polya_terminator"],
    },
    "scenario_2": {
        "Promoters": [
            "heat_responsive_promoter",
            "teto_promoter",
            "laryngeal_gland_promoter",
        ],
        "Control Systems": ["rtta"],
        "Genes": ["pyroxin_a6"],
        "Special Elements": ["polya_terminator"],
    },
    "scenario_royal_guardian": {
        "Promoters": ["venom_gland_promoter", "molting_stage_promoter", "constitutive_promoter"],
        "Control Systems": ["cre", "loxp"],
        "Genes": ["virexin"],
        "Special Elements": ["stop_cassette", "polya_terminator"],
    },
    "scenario_nightfall_certification": {
        "Promoters": ["night_active_promoter", "scale_pigment_promoter", "constitutive_promoter"],
        "Control Systems": ["cre_ert", "loxp"],
        "Genes": ["nyxmelanin"],
        "Special Elements": ["stop_cassette", "polya_terminator"],
    },
    "scenario_compulsive_hoarding": ALL_COMPONENTS,
    "scenario_3": {
        "Promoters": [
            "heat_responsive_promoter",
            "teto_promoter",
            "laryngeal_gland_promoter",
        ],
        "Control Systems": ["rtta"],
        "Genes": ["pyroxin_a6"],
        "Special Elements": ["polya_terminator"],
    },
    "scenario_5": ALL_COMPONENTS,
    "final": ALL_COMPONENTS,
}


def get_component_groups():
    scenario_filter = SCENARIO_COMPONENTS.get(st.session_state.get("scenario_id"))
    if not scenario_filter:
        return COMPONENT_GROUPS

    return {
        group: [
            COMPONENT_BY_ID[group][component_id]
            for component_id in allowed_components
            if component_id in COMPONENT_BY_ID[group]
        ]
        for group, allowed_components in scenario_filter.items()
        if allowed_components
    }


def initialize_builder_state():
    if "constructs" not in st.session_state:
        existing_construct = st.session_state.get("construct", [])
        st.session_state.constructs = [existing_construct] if existing_construct else [[]]
    if not st.session_state.constructs:
        st.session_state.constructs = [[]]
    if "current_construct_index" not in st.session_state:
        st.session_state.current_construct_index = 0
    if st.session_state.current_construct_index >= len(st.session_state.constructs):
        st.session_state.current_construct_index = len(st.session_state.constructs) - 1
    st.session_state.construct = st.session_state.constructs[st.session_state.current_construct_index]
    if "builder_result" not in st.session_state:
        st.session_state.builder_result = None


def find_component(group, component_id):
    for component in COMPONENT_GROUPS[group]:
        if component["id"] == component_id:
            return component
    return None


def add_component(group, component_id, orientation):
    component = find_component(group, component_id)
    if component is None:
        return

    current_construct().append(
        {
            "id": component["id"],
            "type": group,
            "name": component["display"],
            "symbol": component["symbol"],
            "role": component["role"],
            "description": component["description"],
            "orientation": orientation,
        }
    )
    sync_legacy_construct()
    st.session_state.builder_result = None


def remove_last_component():
    construct = current_construct()
    if construct:
        construct.pop()
        sync_legacy_construct()
        st.session_state.builder_result = None


def clear_construct():
    initialize_builder_state()
    st.session_state.constructs[st.session_state.current_construct_index] = []
    sync_legacy_construct()
    st.session_state.builder_result = None


def remove_current_construct():
    initialize_builder_state()
    if not st.session_state.constructs:
        st.session_state.constructs = [[]]
        st.session_state.current_construct_index = 0
    elif len(st.session_state.constructs) == 1:
        st.session_state.constructs[0] = []
        st.session_state.current_construct_index = 0
    else:
        remove_index = st.session_state.current_construct_index
        st.session_state.constructs.pop(remove_index)
        st.session_state.current_construct_index = min(
            remove_index,
            len(st.session_state.constructs) - 1,
        )
    sync_legacy_construct()
    st.session_state.builder_result = None


def add_new_construct():
    st.session_state.constructs.append([])
    st.session_state.current_construct_index = len(st.session_state.constructs) - 1
    sync_legacy_construct()
    st.session_state.builder_result = None


def switch_construct(index):
    st.session_state.current_construct_index = index
    sync_legacy_construct()
    st.session_state.builder_result = None


def current_construct():
    return st.session_state.constructs[st.session_state.current_construct_index]


def sync_legacy_construct():
    st.session_state.construct = current_construct()


def move_component(index, direction):
    target = index + direction
    construct = current_construct()
    if target < 0 or target >= len(construct):
        return

    construct[index], construct[target] = construct[target], construct[index]
    sync_legacy_construct()
    st.session_state.builder_result = None


def render_component_picker():
    st.markdown("<h3 class='section-heading'>Build Construct</h3>", unsafe_allow_html=True)
    st.info(
        "Many genetic systems require multiple expression cassettes. Use separate constructs when different proteins need to be expressed independently."
    )
    st.caption("Available tools for this assignment")
    left, middle, right, action = st.columns([1.35, 1.65, 1, 0.9])
    component_groups = get_component_groups()

    with left:
        group = st.radio("Component type", list(component_groups.keys()), horizontal=False)

    with middle:
        selected_label = st.selectbox(
            "Biological component",
            [component["label"] for component in component_groups[group]],
        )
        selected_component = next(
            component for component in component_groups[group] if component["label"] == selected_label
        )
        st.caption(f"{selected_component['role']}: {selected_component['description']}")

    with right:
        orientation = st.radio("Orientation", ORIENTATIONS, horizontal=False)

    with action:
        st.write("")
        st.write("")
        if st.button("Add component", type="primary", use_container_width=True):
            add_component(group, selected_component["id"], orientation)
            st.rerun()


def render_construct_selector():
    constructs = st.session_state.constructs
    selector_col, add_col = st.columns([2, 1])

    with selector_col:
        selected_label = st.selectbox(
            "Current construct",
            [f"Construct {index + 1}" for index in range(len(constructs))],
            index=st.session_state.current_construct_index,
        )
        selected_index = int(selected_label.split()[-1]) - 1
        if selected_index != st.session_state.current_construct_index:
            switch_construct(selected_index)
            st.rerun()

    with add_col:
        st.write("")
        if st.button("Add new construct", use_container_width=True):
            add_new_construct()
            st.rerun()


def render_construct_visual():
    st.markdown("<h3 class='section-heading'>Construct Sequences</h3>", unsafe_allow_html=True)
    render_construct_selector()
    construct = current_construct()

    if not construct:
        st.info("The current construct is empty. Add parts from left to right to assemble this expression cassette.")
    else:
        for index, part in enumerate(construct):
            label_col, up_col, down_col = st.columns([5.8, 0.8, 0.8])
            with label_col:
                st.markdown(
                    f"""
                    <div class="construct-row">
                        <strong>{index + 1}. {part["name"]}</strong>
                        <span>{part["type"]} | {part["orientation"]} | {part["role"]}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with up_col:
                if st.button("Up", key=f"move_up_{st.session_state.current_construct_index}_{index}", disabled=index == 0, use_container_width=True):
                    move_component(index, -1)
                    st.rerun()
            with down_col:
                if st.button(
                    "Down",
                    key=f"move_down_{st.session_state.current_construct_index}_{index}",
                    disabled=index == len(construct) - 1,
                    use_container_width=True,
                ):
                    move_component(index, 1)
                    st.rerun()

    utility_left, utility_middle, utility_right = st.columns([1, 1, 1])
    with utility_left:
        if st.button("Remove last component", use_container_width=True):
            remove_last_component()
            st.rerun()
    with utility_middle:
        if st.button("Clear current construct", use_container_width=True):
            clear_construct()
            st.rerun()
    with utility_right:
        if st.button("Remove current construct", use_container_width=True):
            remove_current_construct()
            st.rerun()


def render_all_constructs():
    st.markdown("<h4>Full Design</h4>", unsafe_allow_html=True)
    arrow = ' <span class="construct-arrow">&rarr;</span> '

    for construct_index, construct in enumerate(st.session_state.constructs):
        if construct:
            labels = []
            for part in construct:
                direction = ">" if part["orientation"] == "Forward" else "<"
                labels.append(f"<span class='construct-token'>{direction} {part['symbol']}</span>")
            sequence = arrow.join(labels)
        else:
            sequence = "<span class='construct-token'>Empty cassette</span>"

        st.markdown(
            f"<div class='construct-preview'><strong>Construct {construct_index + 1}:</strong><br>{sequence}</div>",
            unsafe_allow_html=True,
        )


def run_builder():
    initialize_builder_state()
    render_all_constructs()
    render_component_picker()
    render_construct_visual()


def render_builder(_client=None):
    run_builder()
