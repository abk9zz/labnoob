from components.scenarios import get_scenario


CONSTRAINT_LABELS = {
    "tissue_specific_promoter": "Use the laryngeal gland promoter to target the correct tissue.",
    "gene_present": "Add Pyroxin-A6 so combustion and heat generation are preserved.",
    "valid_construct_order": "Place the promoter before Pyroxin-A6 in the construct.",
    "has_pyroxin": "Add Pyroxin-A6 as the controlled fire effector.",
    "temperature_control": "Add the Heat-Responsive Promoter for high-temperature activation.",
    "tet_system_present": "Add the Tet-On control system: rtTA and TetO.",
    "requires_both_conditions": "Integrate heat control with Tet-On activation so both signals are required.",
    "avoids_constitutive_pyroxin": "Avoid constitutive CMV-driven Pyroxin-A6 expression.",
    "wing_specific_driver": "Use the wing-pattern promoter to drive GAL4 in wing pattern cells.",
    "gal4_driver_present": "Add GAL4 as the driver activator.",
    "uas_responder_present": "Add a UAS responder linked to a Lumina gene.",
    "blue_output_present": "Add Lumina-Blue for the requested blue glow.",
    "modular_library_ready": "Separate wing targeting from the color-producing gene with GAL4/UAS.",
    "glandular_driver_present": "Use the glandular promoter to drive GAL4 in secretory tissue.",
    "gal4_uas_system_present": "Add GAL4 and a UAS responder linked to Aureolin.",
    "aureolin_present": "Add Aureolin as the healing mist effector.",
    "airway_repression_present": "Use the airway promoter to drive GAL80 in lung and airway-associated cells.",
    "subtractive_specificity": "Preserve mist gland expression while excluding airway tissue with GAL80 repression.",
    "venom_gene_present": "Add Venom-X as the defensive output token.",
    "venom_gland_expression": "Use the Venom gland promoter with Venom-X.",
    "stop_blocks_juvenile_expression": "Place the STOP cassette before Venom-X in the same construct.",
    "loxp_sites_present": "Use two loxP site tokens around the safety lock.",
    "cre_maturity_trigger_present": "Use the Molting-stage promoter with Cre in a separate construct.",
    "permanent_unlock_logic": "Combine the locked defensive cassette with a separate maturity-triggered unlock construct.",
    "shadowmelanin_present": "Add Shadowmelanin as the night camouflage effector.",
    "circadian_control_present": "Place Shadowmelanin in a cassette with the Night-active promoter.",
    "approval_unlock_present": "Use Scale pigment promoter to drive Cre-ERT for handler-approved unlocking.",
    "stop_blocks_training_expression": "Place a STOP cassette upstream of Shadowmelanin.",
    "combined_logic_present": "Combine a locked night-active Shadowmelanin cassette with a separate Scale pigment promoter to Cre-ERT unlock construct.",
    "region_targeting_present": "Use the nucleus accumbens promoter to drive GAL4 in the target brain region.",
    "reward_neuron_targeting_present": "Use the Reward-neuron promoter to drive Cre recombinase in the relevant cell population.",
    "modulator_present": "Use Calm-Channel as the behavioral modulator.",
    "intersectional_logic_present": "Combine GAL4/UAS control with a Cre-removable loxP-STOP-loxP lock upstream of Calm-Channel.",
    "bonding_exclusion_present": "Use the Bonding-neuron promoter to drive GAL80 in bonding-related neurons.",
    "avoids_global_suppression": "Avoid CMV-driven neural control and use Calm-Channel instead of Neuro-Silencer.",
}

PYROXIN_A6 = {
    "id": "pyroxin_a6",
    "name": "Pyroxin-A6",
    "terms": ("pyroxin_a6", "pyroxin-a6", "pyroxin a6", "pyx-a6"),
}

LUMINA_GENES = {
    "lumina_blue",
    "lumina_green",
    "lumina_gold",
}

AUREOLIN = {
    "id": "aureolin",
    "name": "Aureolin",
    "terms": ("aureolin", "aur"),
}

VENOM_X = {
    "id": "venom_x",
    "name": "Venom-X",
    "terms": ("venom_x", "venom-x", "venom x", "ven-x"),
}

SHADOWMELANIN = {
    "id": "shadowmelanin",
    "name": "Shadowmelanin",
    "terms": ("shadowmelanin", "shadow melanin", "shd-mel", "shd_mel"),
}

CALM_CHANNEL = {
    "id": "calm_channel",
    "name": "Calm-Channel",
    "terms": ("calm_channel", "calm-channel", "calm channel", "calm-ch"),
}

NEURO_SILENCER = {
    "id": "neuro_silencer",
    "name": "Neuro-Silencer",
    "terms": ("neuro_silencer", "neuro-silencer", "neuro silencer", "neu-sil"),
}

TARGET_TERMS = {
    "larynx": ("larynx", "laryngeal", "combustion_gland", "combustion gland", "throat"),
}

SYSTEMIC_TERMS = (
    "cmv",
    "constitutive",
    "systemic",
    "bloodstream",
    "whole_body",
    "whole body",
    "ubiquitous",
    "always-on",
    "always on",
)

FIRE_TERMS = (
    "fire",
    "pyroxin",
    "pyroxin-a6",
    "combustion",
)

CONTROL_TERMS = (
    "inducible",
    "repressor",
    "repression",
    "switch",
    "external",
    "trigger",
)

TERMINATOR_BLOCKS_EFFECTOR_FEEDBACK = (
    "A terminator appears before the effector gene, so transcription would stop "
    "before the protein is produced."
)

SCENARIO_EFFECTORS = {
    "Frost Titan Trial": (PYROXIN_A6,),
    "Bioluminescent Display Library": (
        {
            "id": "lumina_blue",
            "name": "Lumina-Blue",
            "terms": ("lumina_blue", "lumina-blue", "lumina blue", "lum-b"),
        },
    ),
    "Medicinal Mist Dragon": (AUREOLIN,),
    "Forge Drake Control System": (PYROXIN_A6,),
    "Royal Guardian Dragon": (VENOM_X,),
    "Nightfall Certification Dragon": (SHADOWMELANIN,),
    "Compulsive Hoarding Research Model": (CALM_CHANNEL, NEURO_SILENCER),
}


def evaluate_construct(constructs, species="Frost Titan", scenario=None):
    active_scenario = scenario or get_scenario()
    requirements = active_scenario.get("requirements", [])
    constructs = normalize_constructs(constructs)
    constraints = evaluate_requirements(constructs, requirements)

    satisfied = sum(constraints.values())
    total = len(constraints) or 1
    score = int((satisfied / total) * 100)
    if is_bioluminescent_scenario(active_scenario) and has_direct_wing_blue_expression(constructs):
        score = max(score, 60)

    blocked_construct = terminator_blocks_effector(
        constructs,
        main_effectors_for_scenario(active_scenario),
    )
    has_blocked_effector = blocked_construct is not None
    if has_blocked_effector:
        score = min(score, 60)

    if score < 50:
        outcome = "failure"
    elif score < 80:
        outcome = "partial success"
    else:
        outcome = "success"

    issues = [
        label
        for constraint, label in constraint_labels(requirements).items()
        if not constraints[constraint]
    ]
    if has_blocked_effector:
        issues.append(terminator_feedback(blocked_construct))

    feedback = build_feedback(outcome, constraints, species, active_scenario, constructs)
    if has_blocked_effector:
        feedback = terminator_feedback(blocked_construct)

    return {
        "score": score,
        "outcome": outcome,
        "issues": issues,
        "feedback": feedback,
        "scenario": active_scenario["name"],
    }


def evaluate_requirements(construct, requirements):
    constructs = normalize_constructs(construct)
    return {
        requirement: CONSTRAINT_CHECKS.get(requirement, unsupported_requirement)(constructs)
        for requirement in requirements
    }


def main_effectors_for_scenario(scenario):
    if not scenario:
        return (PYROXIN_A6,)

    return SCENARIO_EFFECTORS.get(scenario.get("name"), (PYROXIN_A6,))


def terminator_blocks_effector(constructs, effector_names):
    for construct_index, construct in enumerate(normalize_constructs(constructs)):
        ids = construct_ids(construct)
        for effector in effector_names:
            effector_index = find_gene_index(construct, effector)
            if effector_index is None:
                continue

            upstream_ids = ids[:effector_index]
            if "terminator" in upstream_ids:
                return construct_index

    return None


def terminator_feedback(construct_index):
    return (
        f"A terminator appears before the expressed gene in Construct {construct_index + 1}, "
        "so transcription would stop before the protein is produced."
    )


def expression_cassette_start(construct, effector_index):
    for index in range(effector_index - 1, -1, -1):
        if is_promoter(construct[index]):
            return index
    return 0


def unsupported_requirement(_construct):
    return False


def constraint_labels(requirements):
    return {
        requirement: CONSTRAINT_LABELS.get(
            requirement,
            f"Requirement not yet implemented: {requirement}",
        )
        for requirement in requirements
    }


def has_tissue_specific_promoter(construct):
    ids = all_construct_ids(construct)
    return "laryngeal_gland_promoter" in ids


def has_gene(construct, gene):
    ids = all_construct_ids(construct)
    terms = all_construct_terms(construct)
    return gene["id"] in ids or contains_any(terms, gene["terms"])


def has_valid_construct_order(construct):
    return any(
        has_ordered_pair(cassette, "laryngeal_gland_promoter", PYROXIN_A6["id"])
        for cassette in normalize_constructs(construct)
    )


def has_temperature_control(construct):
    return "heat_responsive_promoter" in all_construct_ids(construct)


def has_tet_system(construct):
    ids = all_construct_ids(construct)
    return all(component in ids for component in ("rtta", "teto_promoter"))


def requires_both_conditions(construct):
    constructs = normalize_constructs(construct)
    if not has_temperature_control(constructs) or not has_tet_system(constructs):
        return False

    heat_controls_rtta = any(
        has_ordered_pair(cassette, "heat_responsive_promoter", "rtta")
        for cassette in constructs
    )
    tet_controls_pyroxin = any(
        has_ordered_pair(cassette, "teto_promoter", PYROXIN_A6["id"])
        for cassette in constructs
    )

    return heat_controls_rtta and tet_controls_pyroxin


def avoids_constitutive_pyroxin(construct):
    constructs = normalize_constructs(construct)
    if not has_gene(constructs, PYROXIN_A6):
        return False

    for cassette in constructs:
        pyroxin_index = find_gene_index(cassette, PYROXIN_A6)
        if pyroxin_index is None:
            continue
        upstream_promoters = [
            part.get("id")
            for part in cassette[:pyroxin_index]
            if part.get("type") == "Promoters" or "promoter" in str(part.get("id", "")).lower()
        ]
        if upstream_promoters and upstream_promoters[-1] == "cmv":
            return False
    return True


def has_wing_specific_driver(construct):
    return any(
        has_ordered_pair(cassette, "wing_pattern_promoter", "gal4")
        for cassette in normalize_constructs(construct)
    )


def has_gal4_driver(construct):
    return "gal4" in all_construct_ids(construct)


def has_uas_responder(construct):
    return any(
        has_uas_lumina_responder(cassette)
        for cassette in normalize_constructs(construct)
    )


def has_blue_output(construct):
    return "lumina_blue" in all_construct_ids(construct)


def is_modular_library_ready(construct):
    return (
        has_wing_specific_driver(construct)
        and has_gal4_driver(construct)
        and has_uas_responder(construct)
        and not has_direct_wing_blue_expression(construct)
    )


def has_glandular_gal4_driver(construct):
    return any(
        has_ordered_pair(cassette, "glandular_promoter", "gal4")
        for cassette in normalize_constructs(construct)
    )


def has_uas_aureolin_responder(construct):
    return any(
        has_ordered_pair(cassette, "uas", "aureolin")
        for cassette in normalize_constructs(construct)
    )


def has_gal4_uas_aureolin_system(construct):
    ids = all_construct_ids(construct)
    return "gal4" in ids and "uas" in ids and has_uas_aureolin_responder(construct)


def has_aureolin(construct):
    return has_gene(construct, AUREOLIN)


def has_airway_gal80_repression(construct):
    return any(
        has_ordered_pair(cassette, "airway_promoter", "gal80")
        for cassette in normalize_constructs(construct)
    )


def has_subtractive_specificity(construct):
    return (
        has_glandular_gal4_driver(construct)
        and has_gal4_uas_aureolin_system(construct)
        and has_airway_gal80_repression(construct)
    )


def has_venom_gene(construct):
    return has_gene(construct, VENOM_X)


def venom_cassettes(construct):
    return [
        cassette
        for cassette in normalize_constructs(construct)
        if first_index(construct_ids(cassette), VENOM_X["id"]) is not None
    ]


def has_venom_gland_expression(construct):
    return any(
        has_ordered_pair(cassette, "venom_gland_promoter", VENOM_X["id"])
        for cassette in venom_cassettes(construct)
    )


def has_stop_before_venom(construct):
    for cassette in venom_cassettes(construct):
        ids = construct_ids(cassette)
        stop_index = first_index(ids, "stop_cassette")
        venom_index = first_index(ids, VENOM_X["id"])
        if stop_index is not None and venom_index is not None and stop_index < venom_index:
            return True
    return False


def has_two_loxp_sites_in_venom_cassette(construct):
    return any(
        construct_ids(cassette).count("loxp") >= 2
        for cassette in venom_cassettes(construct)
    )


def has_two_loxp_sites_in_locked_effector_cassette(construct):
    return (
        has_two_loxp_sites_in_venom_cassette(construct)
        or has_two_loxp_sites_in_shadowmelanin_cassette(construct)
    )


def has_locked_venom_cassette(construct):
    for cassette in venom_cassettes(construct):
        ids = construct_ids(cassette)
        venom_index = first_index(ids, VENOM_X["id"])
        if venom_index is None:
            continue

        for first_loxp in range(0, venom_index):
            if ids[first_loxp] != "loxp":
                continue
            for stop_index in range(first_loxp + 1, venom_index):
                if ids[stop_index] != "stop_cassette":
                    continue
                for second_loxp in range(stop_index + 1, venom_index):
                    if ids[second_loxp] == "loxp":
                        return True
    return False


def has_maturity_cre_construct(construct):
    return any(
        has_ordered_pair(cassette, "molting_stage_promoter", "cre")
        for cassette in normalize_constructs(construct)
    )


def has_separate_maturity_cre_construct(construct):
    constructs = normalize_constructs(construct)
    for cre_index, cre_cassette in enumerate(constructs):
        if not has_ordered_pair(cre_cassette, "molting_stage_promoter", "cre"):
            continue
        for venom_index, venom_cassette in enumerate(constructs):
            if venom_index == cre_index:
                continue
            if first_index(construct_ids(venom_cassette), VENOM_X["id"]) is not None:
                return True
    return False


def has_permanent_unlock_logic(construct):
    return has_locked_venom_cassette(construct) and has_separate_maturity_cre_construct(construct)


def has_broad_cre_unlock(construct):
    return any(
        has_ordered_pair(cassette, "cmv", "cre")
        for cassette in normalize_constructs(construct)
    )


def has_direct_venom_expression(construct):
    for cassette in venom_cassettes(construct):
        ids = construct_ids(cassette)
        venom_index = first_index(ids, VENOM_X["id"])
        if venom_index is None:
            continue
        if (
            has_ordered_pair(cassette, "venom_gland_promoter", VENOM_X["id"])
            and "stop_cassette" not in ids[:venom_index]
        ):
            return True
    return False


def shadowmelanin_cassettes(construct):
    return [
        cassette
        for cassette in normalize_constructs(construct)
        if first_index(construct_ids(cassette), SHADOWMELANIN["id"]) is not None
    ]


def has_shadowmelanin(construct):
    return has_gene(construct, SHADOWMELANIN)


def has_night_active_shadowmelanin_cassette(construct):
    return any(
        "night_active_promoter" in construct_ids(cassette)
        for cassette in shadowmelanin_cassettes(construct)
    )


def has_scale_cre_ert_construct(construct):
    return any(
        has_ordered_pair(cassette, "scale_pigment_promoter", "cre_ert")
        for cassette in normalize_constructs(construct)
    )


def has_stop_before_shadowmelanin(construct):
    for cassette in shadowmelanin_cassettes(construct):
        ids = construct_ids(cassette)
        stop_index = first_index(ids, "stop_cassette")
        shadowmelanin_index = first_index(ids, SHADOWMELANIN["id"])
        if (
            stop_index is not None
            and shadowmelanin_index is not None
            and stop_index < shadowmelanin_index
        ):
            return True
    return False


def has_two_loxp_sites_in_shadowmelanin_cassette(construct):
    return any(
        construct_ids(cassette).count("loxp") >= 2
        for cassette in shadowmelanin_cassettes(construct)
    )


def has_locked_nightfall_cassette(construct):
    for cassette in shadowmelanin_cassettes(construct):
        ids = construct_ids(cassette)
        if has_ordered_sequence(
            ids,
            [
                "night_active_promoter",
                "loxp",
                "stop_cassette",
                "loxp",
                SHADOWMELANIN["id"],
            ],
        ):
            return True
    return False


def has_combined_nightfall_logic(construct):
    constructs = normalize_constructs(construct)
    for unlock_index, unlock_cassette in enumerate(constructs):
        if not has_ordered_pair(unlock_cassette, "scale_pigment_promoter", "cre_ert"):
            continue
        for locked_index, locked_cassette in enumerate(constructs):
            if locked_index == unlock_index:
                continue
            if has_locked_nightfall_cassette([locked_cassette]):
                return True
    return False


def has_direct_night_shadowmelanin_expression(construct):
    for cassette in shadowmelanin_cassettes(construct):
        ids = construct_ids(cassette)
        shadowmelanin_index = first_index(ids, SHADOWMELANIN["id"])
        night_index = first_index(ids, "night_active_promoter")
        if night_index is None or shadowmelanin_index is None or night_index > shadowmelanin_index:
            continue
        if "stop_cassette" not in ids[:shadowmelanin_index]:
            return True
    return False


def has_constitutive_shadowmelanin_expression(construct):
    return any(
        has_ordered_pair(cassette, "cmv", SHADOWMELANIN["id"])
        for cassette in shadowmelanin_cassettes(construct)
    )


def calm_channel_cassettes(construct):
    return [
        cassette
        for cassette in normalize_constructs(construct)
        if first_index(construct_ids(cassette), CALM_CHANNEL["id"]) is not None
    ]


def has_nucleus_accumbens_gal4_driver(construct):
    return any(
        has_ordered_pair(cassette, "nucleus_accumbens_promoter", "gal4")
        for cassette in normalize_constructs(construct)
    )


def has_reward_neuron_cre_driver(construct):
    return any(
        has_ordered_pair(cassette, "reward_neuron_promoter", "cre")
        for cassette in normalize_constructs(construct)
    )


def has_calm_channel(construct):
    return has_gene(construct, CALM_CHANNEL)


def has_uas_calm_channel_responder(construct):
    return any(
        has_ordered_pair(cassette, "uas", CALM_CHANNEL["id"])
        for cassette in calm_channel_cassettes(construct)
    )


def has_locked_calm_channel_cassette(construct):
    for cassette in calm_channel_cassettes(construct):
        ids = construct_ids(cassette)
        calm_index = first_index(ids, CALM_CHANNEL["id"])
        if calm_index is None:
            continue

        for uas_index in range(0, calm_index):
            if ids[uas_index] != "uas":
                continue
            for first_loxp in range(uas_index + 1, calm_index):
                if ids[first_loxp] != "loxp":
                    continue
                for stop_index in range(first_loxp + 1, calm_index):
                    if ids[stop_index] != "stop_cassette":
                        continue
                    for second_loxp in range(stop_index + 1, calm_index):
                        if ids[second_loxp] == "loxp":
                            return True
    return False


def has_separate_nacc_gal4_and_reward_cre_constructs(construct):
    constructs = normalize_constructs(construct)
    for gal4_index, gal4_cassette in enumerate(constructs):
        if not has_ordered_pair(gal4_cassette, "nucleus_accumbens_promoter", "gal4"):
            continue
        for cre_index, cre_cassette in enumerate(constructs):
            if cre_index == gal4_index:
                continue
            if has_ordered_pair(cre_cassette, "reward_neuron_promoter", "cre"):
                return True
    return False


def has_compulsive_intersectional_logic(construct):
    ids = all_construct_ids(construct)
    return (
        "uas" in ids
        and has_uas_calm_channel_responder(construct)
        and has_locked_calm_channel_cassette(construct)
        and has_separate_nacc_gal4_and_reward_cre_constructs(construct)
    )


def has_bonding_gal80_exclusion(construct):
    return any(
        has_ordered_pair(cassette, "bonding_neuron_promoter", "gal80")
        for cassette in normalize_constructs(construct)
    )


def has_neuro_silencer(construct):
    return has_gene(construct, NEURO_SILENCER)


def has_cmv_driven_behavioral_component(construct):
    unsafe_targets = ("gal4", "cre", CALM_CHANNEL["id"], NEURO_SILENCER["id"])
    return any(
        has_ordered_pair(cassette, "cmv", target)
        for cassette in normalize_constructs(construct)
        for target in unsafe_targets
    )


def avoids_global_behavioral_suppression(construct):
    return (
        has_calm_channel(construct)
        and not has_neuro_silencer(construct)
        and not has_cmv_driven_behavioral_component(construct)
    )


CONSTRAINT_CHECKS = {
    "tissue_specific_promoter": has_tissue_specific_promoter,
    "gene_present": lambda construct: has_gene(construct, PYROXIN_A6),
    "valid_construct_order": has_valid_construct_order,
    "has_pyroxin": lambda construct: has_gene(construct, PYROXIN_A6),
    "temperature_control": has_temperature_control,
    "tet_system_present": has_tet_system,
    "requires_both_conditions": requires_both_conditions,
    "avoids_constitutive_pyroxin": avoids_constitutive_pyroxin,
    "wing_specific_driver": has_wing_specific_driver,
    "gal4_driver_present": has_gal4_driver,
    "uas_responder_present": has_uas_responder,
    "blue_output_present": has_blue_output,
    "modular_library_ready": is_modular_library_ready,
    "glandular_driver_present": has_glandular_gal4_driver,
    "gal4_uas_system_present": has_gal4_uas_aureolin_system,
    "aureolin_present": has_aureolin,
    "airway_repression_present": has_airway_gal80_repression,
    "subtractive_specificity": has_subtractive_specificity,
    "venom_gene_present": has_venom_gene,
    "venom_gland_expression": has_venom_gland_expression,
    "stop_blocks_juvenile_expression": has_stop_before_venom,
    "loxp_sites_present": has_two_loxp_sites_in_locked_effector_cassette,
    "cre_maturity_trigger_present": has_separate_maturity_cre_construct,
    "permanent_unlock_logic": has_permanent_unlock_logic,
    "shadowmelanin_present": has_shadowmelanin,
    "circadian_control_present": has_night_active_shadowmelanin_cassette,
    "approval_unlock_present": has_scale_cre_ert_construct,
    "stop_blocks_training_expression": has_stop_before_shadowmelanin,
    "combined_logic_present": has_combined_nightfall_logic,
    "region_targeting_present": has_nucleus_accumbens_gal4_driver,
    "reward_neuron_targeting_present": has_reward_neuron_cre_driver,
    "modulator_present": has_calm_channel,
    "intersectional_logic_present": has_compulsive_intersectional_logic,
    "bonding_exclusion_present": has_bonding_gal80_exclusion,
    "avoids_global_suppression": avoids_global_behavioral_suppression,
}


def first_index(items, target):
    try:
        return items.index(target)
    except ValueError:
        return None


def has_ordered_sequence(items, sequence):
    search_start = 0
    for target in sequence:
        try:
            found_index = items.index(target, search_start)
        except ValueError:
            return False
        search_start = found_index + 1
    return True


def find_gene_index(construct, gene):
    for index, part in enumerate(construct):
        part_id = str(part.get("id", "")).lower()
        part_terms = " ".join(
            str(value).lower().replace("-", "_") for value in part.values()
        )
        part_terms = f"{part_terms} {' '.join(str(value).lower().replace('_', ' ') for value in part.values())}"
        if part_id == gene["id"] or contains_any(part_terms, gene["terms"]):
            return index
    return None


def first_lumina_index(construct):
    for index, part in enumerate(construct):
        if str(part.get("id", "")).lower() in LUMINA_GENES:
            return index
    return None


def has_uas_lumina_responder(construct):
    ids = construct_ids(construct)
    uas_index = first_index(ids, "uas")
    lumina_index = first_lumina_index(construct)
    if uas_index is None or lumina_index is None or uas_index > lumina_index:
        return False

    return not has_intervening_promoter(construct, uas_index, lumina_index)


def has_intervening_promoter(construct, start, end):
    return any(
        is_promoter(part)
        for part in construct[start + 1 : end]
    )


def has_ordered_pair(construct, upstream_id, downstream_id):
    ids = construct_ids(construct)
    for upstream_index, part_id in enumerate(ids):
        if part_id != upstream_id:
            continue
        for downstream_index in range(upstream_index + 1, len(ids)):
            if ids[downstream_index] == downstream_id:
                return not has_intervening_promoter(
                    construct,
                    upstream_index,
                    downstream_index,
                )
    return False


def has_direct_wing_blue_expression(construct):
    for cassette in normalize_constructs(construct):
        ids = construct_ids(cassette)
        wing_index = first_index(ids, "wing_pattern_promoter")
        blue_index = first_index(ids, "lumina_blue")
        uas_index = first_index(ids, "uas")
        if wing_index is None or blue_index is None or wing_index > blue_index:
            continue

        uas_controls_blue = uas_index is not None and uas_index < blue_index
        if not uas_controls_blue and not has_intervening_promoter(cassette, wing_index, blue_index):
            return True
    return False


def has_broad_gal4_driver(construct):
    return any(
        has_ordered_pair(cassette, "cmv", "gal4")
        for cassette in normalize_constructs(construct)
    )


def has_targeted_expression(construct, target="larynx"):
    terms = all_construct_terms(construct)
    target_terms = TARGET_TERMS.get(target, (target,))
    has_target_signal = contains_any(terms, target_terms)
    has_expression_driver = any(has_promoter(cassette) for cassette in normalize_constructs(construct)) or contains_any(
        terms,
        ("gal4", "uas", "cre", "activator", "promoter"),
    )

    return has_target_signal and has_expression_driver


def avoids_systemic_expression(construct):
    terms = all_construct_terms(construct)
    has_systemic_driver = contains_any(terms, SYSTEMIC_TERMS)
    has_local_or_gated_design = has_targeted_expression(construct) or has_control_mechanism(construct)

    return has_local_or_gated_design and not has_systemic_driver


def preserves_fire_function(construct):
    terms = all_construct_terms(construct)
    has_fire_effector = contains_any(terms, FIRE_TERMS)
    has_activation_path = any(has_promoter(cassette) for cassette in normalize_constructs(construct)) or contains_any(terms, ("gal4", "uas", "cre", "activator"))

    return has_fire_effector and has_activation_path


def has_control_mechanism(construct):
    ids = all_construct_ids(construct)
    terms = all_construct_terms(construct)

    has_cre_switch = "cre" in ids and "stop_cassette" in ids and ids.count("loxp") >= 2
    has_gal4_switch = "gal4" in ids and "uas" in ids and ("gal80" in ids or has_targeted_expression(construct))
    has_inducible_signal = contains_any(terms, CONTROL_TERMS) or "heat_shock_promoter" in ids
    has_termination = "terminator" in ids

    return has_cre_switch or has_gal4_switch or has_inducible_signal or (
        has_targeted_expression(construct) and has_termination
    )


def build_feedback(outcome, constraints, species="Frost Titan", scenario=None, construct=None):
    if is_bioluminescent_scenario(scenario):
        return build_bioluminescent_feedback(outcome, constraints, construct or [])

    if is_gal80_repression_scenario(scenario):
        return build_gal80_repression_feedback(outcome, constraints, construct or [])

    if scenario and scenario.get("name") == "Forge Drake Control System":
        return build_forge_drake_feedback(outcome, constraints)

    if is_royal_guardian_scenario(scenario):
        return build_royal_guardian_feedback(outcome, constraints, construct or [])

    if is_nightfall_certification_scenario(scenario):
        return build_nightfall_certification_feedback(outcome, constraints, construct or [])

    if is_compulsive_hoarding_scenario(scenario):
        return build_compulsive_hoarding_feedback(outcome, constraints, construct or [])

    if outcome == "success":
        return (
            "The introductory design places Pyroxin-A6 expression under laryngeal gland control "
            f"for the {species}."
        )

    if outcome == "partial success":
        if constraints["gene_present"] and not constraints["tissue_specific_promoter"]:
            return "Pyroxin-A6 is present, but it needs the laryngeal gland promoter for this trial."
        if constraints["tissue_specific_promoter"] and not constraints["gene_present"]:
            return "Your dragon lacks Pyroxin-A6 expression and cannot produce fire."
        return "This trial design is close. Check that the promoter comes before Pyroxin-A6."

    return f"The {species} trial construct needs a laryngeal gland promoter followed by Pyroxin-A6."


def is_bioluminescent_scenario(scenario):
    return scenario and scenario.get("name") == "Bioluminescent Display Library"


def is_gal80_repression_scenario(scenario):
    return scenario and scenario.get("name") == "Medicinal Mist Dragon"


def is_royal_guardian_scenario(scenario):
    return scenario and scenario.get("name") == "Royal Guardian Dragon"


def is_nightfall_certification_scenario(scenario):
    return scenario and scenario.get("name") == "Nightfall Certification Dragon"


def is_compulsive_hoarding_scenario(scenario):
    return scenario and scenario.get("name") == "Compulsive Hoarding Research Model"


def build_bioluminescent_feedback(outcome, constraints, construct):
    if outcome == "success":
        return "The GAL4/UAS system separates wing targeting from Lumina-Blue output, creating a reusable color-library design."

    if has_direct_wing_blue_expression(construct):
        return "The dragon may glow correctly, but the design is not modular. Direct promoter-to-gene expression would require rebuilding the construct for every future color variant."
    if has_uas_responder(construct) and not has_gal4_driver(construct):
        return "The responder construct is present, but no GAL4 driver is available to activate UAS-linked expression."
    if has_broad_gal4_driver(construct) and has_uas_responder(construct):
        return "The binary system is present, but GAL4 expression is too broad, causing glow outside the intended wing pattern."
    if not constraints.get("blue_output_present"):
        return "The modular system may be present, but the requested blue output is missing."

    return "The bioluminescent display system needs a wing-specific GAL4 driver and a UAS-linked Lumina-Blue responder."


def build_gal80_repression_feedback(outcome, constraints, construct):
    if outcome == "success":
        return "The design uses glandular GAL4 to activate UAS-linked Aureolin while airway GAL80 blocks expression in respiratory tissue."

    if has_glandular_gal4_driver(construct) and has_uas_aureolin_responder(construct) and has_ordered_pair(construct, "cmv", "gal80"):
        return "GAL80 is too broad and may repress the desired healing mist expression."

    if has_glandular_gal4_driver(construct) and has_uas_aureolin_responder(construct) and not has_airway_gal80_repression(construct):
        return "The healing mist system is active, but expression is not excluded from airway tissue. This may damage the dragon's lungs."

    if has_airway_gal80_repression(construct) and has_uas_aureolin_responder(construct) and not has_gal4_driver(construct):
        return "GAL80 repression is present, but there is no GAL4 driver to activate Aureolin expression."

    if has_broad_gal4_driver(construct) and has_uas_aureolin_responder(construct) and has_airway_gal80_repression(construct):
        return "The repression system is present, but the GAL4 driver is too broad. Aureolin may be expressed in unintended tissues outside the airway."

    if has_ordered_pair(construct, "glandular_promoter", "aureolin"):
        return "The dragon may produce healing mist, but the design does not use GAL80 repression and cannot exclude airway expression."

    if constraints.get("airway_repression_present") and not constraints.get("gal4_uas_system_present"):
        return "GAL80 repression is present, but the Aureolin responder still needs a GAL4 activation path."

    if constraints.get("gal4_uas_system_present") and not constraints.get("airway_repression_present"):
        return "The healing mist responder can be activated, but airway-specific GAL80 repression is missing."

    return "The Medicinal Mist Dragon design needs a glandular GAL4 driver, a UAS-Aureolin responder, and airway-specific GAL80 repression."


def build_forge_drake_feedback(outcome, constraints):
    if outcome == "success":
        return "The design uses an inducible system that can be activated by handler-administered Dox Feed, while still requiring forge heat."

    if outcome == "partial success":
        if not constraints.get("avoids_constitutive_pyroxin"):
            return "CMV-driven Pyroxin-A6 expression is unsafe because it can bypass the required control conditions."
        if constraints.get("tet_system_present") and not constraints.get("temperature_control"):
            return "The handler-triggered inducible system is present, but forge heat is not required."
        if constraints.get("temperature_control") and not constraints.get("tet_system_present"):
            return "Fire production is still triggered by heat alone, indicating insufficient control."
        if constraints.get("tet_system_present") and constraints.get("temperature_control"):
            return "Inducible system is present, but not properly integrated with temperature control."
        return "The Forge Drake design includes some required parts, but still lacks full dual-signal control."

    if not constraints.get("avoids_constitutive_pyroxin"):
        return "CMV-driven Pyroxin-A6 expression is unsafe because it can bypass the required control conditions."
    if constraints.get("temperature_control") and not constraints.get("tet_system_present"):
        return "Fire production is still triggered by heat alone, indicating insufficient control."

    return "The Forge Drake control system must require both high forge temperature and handler-administered Dox Feed activation."


def build_royal_guardian_feedback(outcome, constraints, construct):
    if outcome == "success":
        return "The design locks the defensive trait during youth, then uses the maturity trigger to permanently unlock the adult guardian state."

    if has_direct_venom_expression(construct):
        return "The defensive trait is in the correct tissue, but there is no juvenile safety lock. The dragon would not be safe to raise with the princess."

    if has_venom_gland_expression(construct) and has_stop_before_venom(construct) and not has_two_loxp_sites_in_venom_cassette(construct):
        return "The safety lock is present, but there is no matching unlock system after maturity."

    if has_maturity_cre_construct(construct) and not has_locked_venom_cassette(construct):
        return "The maturity trigger is present, but there is no locked defensive cassette for it to unlock."

    if has_broad_cre_unlock(construct):
        return "The unlock signal is too broad and could occur outside the intended maturity event."

    if has_locked_venom_cassette(construct) and not has_maturity_cre_construct(construct):
        return "The defensive cassette is locked correctly, but there is no maturity trigger to unlock it."

    if constraints.get("cre_maturity_trigger_present") and not constraints.get("venom_gland_expression"):
        return "The maturity unlock is present, but the defensive trait is not restricted to the intended tissue."

    return "This royal guardian design needs a locked defensive cassette and a separate maturity-triggered unlock construct."


def build_nightfall_certification_feedback(outcome, constraints, construct):
    if outcome == "success":
        return "The design keeps camouflage unavailable during training, then uses handler-approved Cre-ERT unlocking so Shadowmelanin follows the night cycle afterward."

    if has_direct_night_shadowmelanin_expression(construct):
        return "The camouflage follows the night cycle, but it is available before certification. The approval lock is missing."

    if has_scale_cre_ert_construct(construct) and has_constitutive_shadowmelanin_expression(construct):
        return "The approval unlock is present, but Shadowmelanin expression is not controlled by the night cycle."

    if has_locked_nightfall_cassette(construct) and not has_scale_cre_ert_construct(construct):
        return "The camouflage cassette is locked, but there is no handler-activated unlock system."

    if has_scale_cre_ert_construct(construct) and not has_shadowmelanin(construct):
        return "The handler approval system is present, but there is no locked camouflage cassette for it to activate."

    if has_constitutive_shadowmelanin_expression(construct):
        return "Shadowmelanin would be expressed too broadly and without certification or circadian control."

    if constraints.get("approval_unlock_present") and not constraints.get("circadian_control_present"):
        return "The approval unlock is present, but Shadowmelanin expression is not controlled by the night cycle."

    if constraints.get("circadian_control_present") and not constraints.get("approval_unlock_present"):
        return "The camouflage follows the night cycle, but it is available before certification. The approval lock is missing."

    return "The Nightfall Drake design needs a handler-approved Cre-ERT unlock construct and a locked night-active Shadowmelanin cassette."


def build_compulsive_hoarding_feedback(outcome, constraints, construct):
    if has_neuro_silencer(construct):
        return "Neuro-Silencer is too strong for this behavioral study. The goal is modulation, not broad suppression."

    if has_nucleus_accumbens_gal4_driver(construct) and has_uas_calm_channel_responder(construct) and not has_reward_neuron_cre_driver(construct):
        return "The intervention is restricted to the correct brain region, but it is not limited to the reward-sensitive neuron subtype."

    if has_reward_neuron_cre_driver(construct) and has_locked_calm_channel_cassette(construct) and not has_nucleus_accumbens_gal4_driver(construct):
        return "The reward-neuron condition is present, but there is no nucleus accumbens targeting. The intervention may affect reward-sensitive neurons outside the intended brain region."

    if (
        has_nucleus_accumbens_gal4_driver(construct)
        and has_reward_neuron_cre_driver(construct)
        and has_locked_calm_channel_cassette(construct)
        and not has_bonding_gal80_exclusion(construct)
    ):
        return "The core intersectional design is present, but there is no exclusion system to protect bonding-related neurons."

    if has_cmv_driven_behavioral_component(construct):
        return "The intervention is too broad and may suppress behavior globally rather than selectively reducing compulsive hoarding."

    if has_bonding_gal80_exclusion(construct) and not (
        has_nucleus_accumbens_gal4_driver(construct)
        or has_reward_neuron_cre_driver(construct)
        or has_uas_calm_channel_responder(construct)
    ):
        return "The exclusion system is present, but there is no targeted intervention to modify hoarding behavior."

    if outcome == "success":
        return "The design layers nucleus accumbens GAL4, reward-neuron Cre, UAS-linked Calm-Channel, and bonding-neuron GAL80 to modulate the pathological circuit without broad behavioral suppression."

    if constraints.get("modulator_present") and not constraints.get("intersectional_logic_present"):
        return "Calm-Channel is present, but the design needs layered GAL4/UAS and Cre-lox logic to restrict modulation to the intended neural intersection."

    if constraints.get("intersectional_logic_present") and not constraints.get("bonding_exclusion_present"):
        return "The intersectional targeting logic is present, but bonding-related neurons still need GAL80 protection."

    return "The compulsive hoarding model needs nucleus accumbens targeting, reward-neuron targeting, Calm-Channel modulation, loxP-STOP-loxP gating, and bonding-neuron exclusion."


def construct_ids(construct):
    return [str(part.get("id", "")).lower() for part in construct]


def all_construct_ids(construct):
    return [
        part_id
        for cassette in normalize_constructs(construct)
        for part_id in construct_ids(cassette)
    ]


def construct_terms(construct):
    values = []
    for part in construct:
        for value in part.values():
            values.append(str(value).lower().replace("-", "_"))
            values.append(str(value).lower().replace("_", " "))
    return " ".join(values)


def all_construct_terms(construct):
    return " ".join(
        construct_terms(cassette)
        for cassette in normalize_constructs(construct)
    )


def normalize_constructs(constructs):
    if not constructs:
        return [[]]
    if isinstance(constructs, list) and all(isinstance(item, dict) for item in constructs):
        return [constructs]
    return [
        cassette
        for cassette in constructs
        if isinstance(cassette, list)
    ] or [[]]


def contains_any(text, terms):
    return any(term in text for term in terms)


def has_promoter(construct):
    return any(is_promoter(part) for part in construct)


def is_promoter(part):
    return part.get("type") == "Promoters" or "promoter" in str(part.get("id", "")).lower()
