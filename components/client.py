from components.scenarios import DEFAULT_SCENARIO_ID, get_scenario


def get_client(scenario_id=DEFAULT_SCENARIO_ID):
    return get_scenario(scenario_id)["client"]
