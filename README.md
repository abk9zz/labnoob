# Emberforge Hatchery

Emberforge Hatchery is a modular Streamlit learning game about synthetic biology design. Players read client requests, review guidance from the hatchery scientist, then assemble genetic constructs from scenario-specific components.

Each scenario teaches a different design idea, from simple tissue-specific expression to modular GAL4/UAS systems, repression, conditional unlocking, and intersectional neural targeting.

## Run the App

```bash
streamlit run apptest.py
```

The app starts on the cover page and routes between screens through Streamlit session state.

## Current Scenarios

1. Trial client, Frost Titan Trial
2. Aurelia Veyne, Bioluminescent Display Library
3. Sister Maela Vire, Medicinal Mist Dragon
4. Master Ivar Thorne, Forge Drake Control System
5. Lady Seraphine Valoryn, Royal Guardian Dragon
6. Commander Elric Vayne, Nightfall Certification Dragon
7. Dr. Mireya Caldus, Compulsive Hoarding Research Model

## Project Structure

```text
apptest.py                  Streamlit entry point and page router
pages/                      Page-level rendering for cover, clients, letters, notes, and builder
components/scenarios.py     Scenario data, client letters, scientist letters, goals, and requirements
components/genome_builder.py Component catalog, scenario-specific component filters, and builder state
components/evaluator.py     Construct evaluation, scoring, constraints, and scenario-specific feedback
components/cards.py         Client card data and rendering helpers
components/navigation.py    Page navigation helpers
components/ui.py            Shared UI rendering helpers
styles/css.py               App styling
```

## Design Notes

- Scenarios are data-driven and selected by `scenario_id`.
- Component lists are restricted per scenario so each case has its own toolset.
- Evaluation is constraint-based: each requirement maps to a detector in `components/evaluator.py`.
- Scoring uses satisfied constraints divided by total constraints, with outcome tiers for failure, partial success, and success.
- Scenario-specific feedback is handled in evaluator branches so new cases can be added without rewriting the builder.

## Development

Keep new scenarios modular:

- Add scenario copy and requirement names in `components/scenarios.py`.
- Add any new components and scenario filters in `components/genome_builder.py`.
- Add evaluator checks, labels, and feedback in `components/evaluator.py`.
- Preserve existing scenario behavior when extending the app.
