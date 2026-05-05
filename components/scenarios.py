SCENARIOS = {
    "scenario_1": {
        "name": "Frost Titan Trial",
        "difficulty": "Trial",
        "species": {
            "name": "Frost Titan",
            "summary": "Arctic-adapted species with systemic Pyroxin-A6 expression",
            "description": "Large, cold-adapted dragons that rely on internal thermogenesis for survival.",
            "badge": "Selected for Trial",
        },
        "client": {
            "name": "Draven Halvyr",
            "title": "Northern War-Beast Breeder",
            "short_description": "Breeds Frost Titans for military use.",
            "request_summary": "Modify Frost Titans to prevent overheating while preserving fire ability",
        },
        "client_letter": """
From: Draven Halvyr
Northern War-Beast Breeder

To the Hatchery Specialists,

I specialize in breeding Frost Titans, a species of dragon native to extreme arctic climates. These creatures are massive, resilient, and highly sought after for military use due to their durability and sheer size.

However, their physiology presents a significant limitation. In temperate or warm environments, these dragons are prone to dangerous overheating, often leading to organ failure.

I have attempted crossbreeding with a more heat-resistant lineage, but none of the resulting eggs were viable. I suspect the issue lies deeper than simple inheritance.

I would like to put in a request for a modified Frost Titan egg that prevents overheating while preserving fire ability.

These dragons must remain stable under battlefield conditions.

If such a modification is possible, I would like to proceed with contract negotiations immediately to include a clutch of five of these eggs.

I hope to hear from you soon.

-- Draven Halvyr
""",
        "scientist_letter": """
From: Dr. Elara Voss
Lead Geneticist, Emberfall Hatchery

To the Apprentice,

Let’s take a moment to think through what we are actually dealing with before you begin assembling a construct.

Frost Titans rely on a thermogenic protein, Pyroxin-A6, to survive in extreme cold environments. This protein serves two critical functions: it enables fire production, and it maintains systemic body heat.

The problem is not the protein itself, but where it is active.

At present, Pyroxin-A6 is expressed throughout the organism, including within the bloodstream. This systemic distribution is what leads to overheating when the dragon is placed in warmer climates.

We are not looking to remove this protein. Doing so would eliminate the dragon’s ability to produce fire entirely.

Pyroxin-A6 must remain active where it is needed, but absent everywhere else.

In practical terms, this means restricting its activity to the laryngeal combustion glands, while eliminating its presence in the rest of the body.

Be mindful of this distinction as you design your system.

- Dr. Elara Voss
""",
        "requirements": [
            "tissue_specific_promoter",
            "gene_present",
            "valid_construct_order",
        ],
        "assignment_label": "Trial Assignment - Introductory Design",
        "assignment_description": (
            "This is a simplified scenario designed to introduce basic genome construction concepts. "
            "Future assignments will require more precise control and complex systems."
        ),
        "builder_title": "Modify Frost Titans to prevent overheating while preserving fire ability.",
        "guidance": [
            "Restrict expression to laryngeal combustion glands",
            "Avoid expression in bloodstream and non-combustion tissues",
            "Preserve fire production",
        ],
        "goal": "",
        "description": (
            "Introductory Frost Titan assignment focused on spacial control of Pyroxin-A6 "
        ),
    },
    "scenario_gal4_uas": {
        "name": "Bioluminescent Display Library",
        "difficulty": "Beginner",
        "species": {
            "name": "Southern Bannerwings",
            "summary": "Performance lineage suited for visible wing pattern traits",
            "description": "Display dragons are bred for safe visual traits during choreographed flight.",
            "badge": "Selected for Beginner Contract",
        },
        "client": {
            "name": "Aurelia Veyne",
            "title": "Director of the Celestial Menagerie",
            "short_description": "Wants a reusable wing-color library for performance dragons.",
            "request_summary": "Create a reusable modular expression system for wing-color variants",
        },
        "client_letter": """
From: Aurelia Veyne
Director of the Celestial Menagerie

Emberfall’s Design Team,

I oversee the Celestial Menagerie, a performance hall known for rare and visually striking magical creatures.

Our newest attraction is intended to be a line of Southern Bannerwings, among the most elegant and visually captivating dragons in our collection. Their wings are broad and expressive, and in motion they create a natural canvas for display.

For the night peformances I was wanting to present a line of bioluminescent display dragons. These dragons must glow in elegant patterns along the wings during flight, creating visible trails for night performances.

However, I do not want a single fixed design.

The Menagerie changes its shows seasonally. One month may require blue wing patterns, while another may require gold, violet, or green. I need a design system that allows Emberfall to create multiple wing-color variants without redesigning the entire dragon each time.

The first dragon should display blue bioluminescence in the wings only.

If this can become the foundation for a reusable color library, I would like to commission additional variants in the future, maybe we can even build a partnership, my dragons are beautiful and I am certain they would make excelent advertisement for your Hatchery.

Sincerely, 

- Aurelia Veyne
""",
        "scientist_letter": """
From: Dr. Elara Voss
Lead Geneticist, Emberfall Hatchery

To the Apprentice,

This request is not difficult because of the trait itself. Bioluminescence is relatively safe compared with combustion, venom secretion, or behavioral modification.

The important part is the client’s long-term goal.

She does not simply want one dragon with glowing wings. She wants a system that can be reused to generate multiple wing-color variants in the future.

A direct design could place a bioluminescent protein under a wing-specific promoter. That would likely produce the requested blue wing glow, but it would be a one-off solution. If the client later requested green, gold, or violet wings, the entire expression system would need to be redesigned.

Instead, think about how to separate two questions:

Where should expression occur?

What trait should be expressed?

A modular system should allow the “where” component to remain the same while the visible output can be swapped. The wing pattern should be controlled independently from the color-producing protein.

For this assignment, the first dragon must show blue bioluminescence in the wings. But the stronger design is one that could later support an entire library of color variants.

Remember, sometimes a successful design is not just the one that works today. It is the one that can be reused tomorrow.

- Dr. Elara Voss
""",
        "requirements": [
            "wing_specific_driver",
            "gal4_driver_present",
            "uas_responder_present",
            "blue_output_present",
            "modular_library_ready",
        ],
        "assignment_label": "Scenario 1 - Beginner Design",
        "assignment_description": (
            "This contract introduces modular expression by separating "
            "where expression happens from what gene is expressed."
        ),
        "builder_title": "Build a reusable bioluminescent wing-color system",
        "guidance": [
            "Restrict expression to wing pattern cells",
            "Ensure activation only under specific controls",
            "Preserve reusable color swapping for future variants",
        ],
        "goal": "",
        "description": (
            "Beginner assignment focused on modular expression for reusable "
            "wing-color variants."
        ),
    },
    "scenario_gal80_repression": {
        "name": "Mistwardens",
        "difficulty": "Intermediate",
        "species": {
            "name": "Mistwardens",
            "summary": "Hospice lineage that secretes therapeutic mist from skin-associated glands",
            "description": (
                "Medicinal Mist Dragons produce healing vapor from specialized skin glands, "
                "but airway expression can compromise breathing."
            ),
            "badge": "Selected for Intermediate Contract",
        },
        "client": {
            "name": "Sister Maela Vire",
            "title": "Warden of the Verdant Hospice",
            "short_description": "Provides palliative care using therapeutic mist dragons and requires strict control of mist secretion.",
            "request_summary": "Create healing mist expression while blocking harmful airway expression.",
        },
        "client_letter": """
From: Sister Maela Vire
Warden of the Verdant Hospice

Dear Emberfall Hatchery specialists, 

I oversee a hospice that treats wounded riders, burned handlers, and injured field beasts.

For years, we have used medicinal mist dragons to calm pain and support wound recovery. When properly bred, these dragons release a soft healing vapor from specialized glands along the skin. The mist is gentle, portable, and useful in places where ordinary treatment is difficult.

Recently, however, several of our hatchlings from a promising line developed severe breathing problems. The mist was produced, but the dragons became weak after repeated use. Some could no longer fly for more than a few minutes.

I need a modified Mistwarden that can still produce healing mist from the skin glands, but does not damage its own lungs or airway tissue.

The dragon must remain healthy enough to work near patients for long periods.

If Emberfall can solve this safely, our hospice would be deeply grateful.

May the Gods be with you,

- Sister Maela Vire
""",
        "scientist_letter": """
From: Dr. Elara Voss
Lead Geneticist, Emberfall Hatchery

To the Apprentice,

This assignment is about precision.

The client is not asking us to create an entirely new healing trait. Medicinal Mist Dragons already produce a useful therapeutic protein, Aureolin, which supports tissue repair when released as a vapor from specialized skin-associated glands.

The challenge is that the promoter we normally use for this type of secretory tissue is not perfectly specific.

The glandular promoter is useful because it activates expression in mist-producing skin glands. However, previous work has shown that it can also become active in airway-associated secretory cells.

Aureolin is beneficial when released from external mist glands, but it can be harmful if produced in lung or airway tissue. In that location, it may thicken respiratory surfaces and interfere with breathing.

So the design problem is not simply turning Aureolin on.

We need expression in the useful glandular tissue, while preventing expression in the respiratory tissue where it becomes dangerous.

Think about whether there is a way to keep the broad usefulness of the glandular driver, while blocking its activity in one unsafe tissue.

- Dr. Elara Voss
""",
        "requirements": [
            "glandular_driver_present",
            "gal4_uas_system_present",
            "aureolin_present",
            "airway_repression_present",
            "subtractive_specificity",
        ],
        "assignment_label": "Scenario 2 - Intermediate Design",
        "assignment_description": (
            "This contract introduces strategies for subtractive tissue specificity."
        ),
        "builder_title": "Create a safe medicinal mist expression system",
        "guidance": [
            "Restrict expression to mist-producing skin glands",
            "Avoid expression in lung and airway-associated cells",
            "Preserve therapeutic Aureolin mist production",
        ],
        "goal": "",
        "description": (
            "Intermediate assignment focused on using GAL80 repression to preserve broad "
            "glandular expression while excluding airway tissue."
        ),
    },
    "scenario_2": {
        "name": "Forge Drake Control System",
        "difficulty": "Intermediate",
        "species": {
            "name": "Forge Drake",
            "summary": "Industrial species with highly reactive Pyroxin-A23 flame output",
            "description": (
                "Industrial dragons capable of producing extremely high-temperature flame. "
                "Their Pyroxin-A23 variant is highly reactive and dangerous if misregulated."
            ),
            "badge": "Selected for Intermediate Contract",
        },
        "client": {
            "name": "Master Ivar Thorne",
            "title": "Industrial Forge Operator",
            "short_description": "Requires strict control over dragon fire activation in forge environments.",
            "request_summary": "Modify Forge Drakes so fire production requires both forge heat and handler activation.",
        },
        "requirements": [
            "has_pyroxin",
            "temperature_control",
            "tet_system_present",
            "requires_both_conditions",
            "avoids_constitutive_pyroxin",
        ],
        "assignment_label": "Scenario 2 - Intermediate Design",
        "assignment_description": (
            "This contract introduces dual-signal control using temperature-dependent activation "
            "and handler-triggered inducible control."
        ),
        "builder_title": "Create a dual-signal Forge Drake fire control system",
        "guidance": [
            "Restrict expression to laryngeal combustion glands",
            "Avoid expression from heat alone or handler activation alone",
            "Ensure activation only under both forge heat and deliberate handler control",
            "Preserve full Pyroxin-A23 fire output when both conditions are met",
        ],
        "goal": "",
        "client_letter": """
From: Master Ivar Thorne
Industrial Forge Operator

Dear Dr. Voss,

I operate a series of high-temperature forges and have long relied on Forge Drakes for metalwork. Their fire output is unmatched, hot enough to handle alloys that no conventional system can process.

However, they are proving increasingly difficult to manage.

The heat of the forge itself seems to excite them. Once inside, they grow restless, agitated, almost eager, and will often release bursts of flame without command. I have lost multiple workstations to these incidents. The last nearly cost me my entire workplace.

I need a modified variant that maintains their full fire-producing capability, but only under strict control.

These are my requests:

- The dragon must only produce fire within the forge environment
- It must not activate spontaneously, even when exposed to heat
- It must require deliberate action from the handler before ignition is possible

I cannot afford another uncontrolled release. The system must be reliable under working conditions.

If this can be done, I am prepared to move forward immediately.

- Master Ivar Thorne
""",
        "scientist_letter": """
From: Dr. Elara Voss
Lead Geneticist, Emberfall Hatchery

To the Apprentice,

This is a more nuanced problem, so take your time before assembling anything.

Forge Drakes already possess a highly efficient combustion system. Pyroxin-A23 is expressed in the correct tissue, and its output is not the issue. The problem lies in how easily that system is activated.

From the client’s description, it is clear that environmental heat alone is enough to push the system into activation. The forge provides a naturally high-temperature environment, and the dragons are responding to it directly.

That gives us our first useful constraint.

If fire production is already sensitive to temperature, we can use that to our advantage. The forge itself can act as one of the conditions required for activation.

However, as we have seen, temperature alone is not sufficient control. The dragons are activating spontaneously simply by being in the environment. That is exactly what we need to prevent.

The system should only activate when the dragon is both in the correct environment and has received an additional, deliberate trigger from the handler.

Think in terms of multiple requirements. The biological system you design should require more than a single signal before it becomes active. If either condition occurs on its own, nothing should happen.

Be careful with this. It is easy to create a system that responds to one signal or the other, but much harder to ensure that both are required simultaneously.

As always, consider what happens when the system is only partially satisfied. That is where most designs fail.

- Dr. Elara Voss
""",
        "description": (
            "Intermediate Forge Drake assignment focused on AND-gated Pyroxin-A23 expression "
            "through heat-responsive and handler control."
        ),
    },
    "scenario_royal_guardian": {
        "name": "Royal Guardian Dragon",
        "difficulty": "Advanced",
        "species": {
            "name": "Velaryn Court Drake",
            "summary": "Calm violet-scaled royal dragon breed",
            "description": (
                "A calm, violet-scaled royal dragon breed known for strong bonding behavior, "
                "steady temperament, and safe development in palace environments."
            ),
            "badge": "Selected for Advanced Teaching Case",
        },
        "client": {
            "name": "Lady Seraphine Valoryn",
            "title": "Royal Steward of the Inner Court",
            "short_description": "Needs a royal guardian dragon with a defensive trait locked until maturity.",
            "request_summary": "Create a royal guardian dragon whose defensive trait unlocks only after maturity.",
        },
        "client_letter": """
From: Lady Seraphine Valoryn
Royal Steward of the Inner Court

To the Lead Scientists of Emberfall Hatchery,

I write on behalf of Her Majesty’s household regarding a private commission of considerable importance.

The Crown requires a bonded guardian dragon for the young Princess. This dragon will be raised alongside her from an early age so that the two may form a lasting bond. It must grow within the palace itself, in close proximity to attendants, tutors, and the royal family.

For this reason, its defensive traits must remain completely inactive during early development.

At maturity, however, the dragon must be capable of defending the princess against any threat. In such circumstances, that traits are not optional. They are necessary safeguards for the Princess' life.

This presents a clear constraint. The dragon must not activate its defensive traits at any point during juvenile development and it must remain entirely safe to raise within the palace environment.

That being said, the defensive traits must become available only after the dragon reaches maturity and once active, the system must remain reliable for the remainder of its life.

This creature must be both companion and protector. It must grow beside the princess without posing a danger, and later stand as her final defense.

I trust Emberfall understands the importance of this request.

The Court awaits your response for approval.

-- Lady Seraphine Valoryn
""",
        "scientist_letter": """
From: Dr. Elara Voss
Lead Geneticist, Emberfall Hatchery

To the Apprentice,

This commission has already been completed.

Given the stakes involved, I handled the design personally. What you are receiving here is not an active assignment, but a teaching case.

And it is an excellent one.

The client’s requirements are not unusual in isolation. What makes this problem interesting is how absolute those requirements are.

The defensive trait must not be available at any point during early development. Not reduced, not suppressed, not conditionally avoided. It must be entirely inaccessible.

At the same time, the system must become available later in the dragon’s life. Once that transition occurs, it must remain stable and reliable. There is no tolerance for reversion.

This is not a question of simply controlling activity. It is a question of whether the system itself can change state.

You are looking for a way to block access to the defensive traits entirely at first, and then, following a specific developmental event, allow that access to be permanently restored.

If your design allows even minimal activity before that transition, or if it can revert afterward, it does not meet the requirements.

In terms of developmental timing, I think relying on the first moulting season is a reasonable trigger. The first moult is a clear, discrete event that happens at a predictable time in development.

As for the base animal, I would suggest working from a Velaryn Court Drake. They are known for their calm temperament, strong bonding behavior, and stable development in enclosed environments. Aditionally, posess very potent venom, which I believe will be satisfactory for defending the Princess. The royal line is also traditionally bred with deep violet scaling, which aligns with the expectations of the court.

Treat this as practice, but do not treat it lightly. I will be evaluating your reasoning.

-- Dr. Elara Voss
""",
        "requirements": [
            "venom_gene_present",
            "venom_gland_expression",
            "stop_blocks_juvenile_expression",
            "loxp_sites_present",
            "cre_maturity_trigger_present",
            "permanent_unlock_logic",
        ],
        "assignment_label": "Scenario 4 - Advanced Teaching Case",
        "assignment_description": (
            "This teaching case introduces a state-changing unlock system for "
            "a royal guardian dragon."
        ),
        "builder_title": "Build a maturity-unlocked royal guardian defense system",
        "guidance": [
            "Restrict expression to venom gland tissue after maturity",
            "Avoid expression during juvenile development",
            "Ensure activation only after the first maturity molt",
            "Preserve stable guardian defense after unlocking",
        ],
        "goal": "",
        "description": (
            "Advanced royal guardian assignment focused on a permanent unlock "
            "after maturity."
        ),
    },
    "scenario_nightfall_certification": {
        "name": "Nightfall Certification Dragon",
        "difficulty": "Advanced",
        "species": {
            "name": "Nightfall Drake",
            "summary": "Quiet reconnaissance breed suited for certified night operations",
            "description": (
                "A quiet reconnaissance breed trained for covert flight. These dragons are "
                "highly responsive to handlers and suited for night operations, but should "
                "not develop camouflage unless certified."
            ),
            "badge": "Selected for Advanced Contract",
        },
        "client": {
            "name": "Commander Elric Vayne",
            "title": "Director of Covert Operations, Nightfall Division",
            "short_description": "Needs covert dragons that gain night camouflage only after certification.",
            "request_summary": "Create certified night camouflage with permanent approval unlocking and circadian expression.",
        },
        "client_letter": """
From: Commander Elric Vayne
Director of Covert Operations, Nightfall Division

Emberfall Hatchery,

I am submitting a request for a reconnaissance-class dragon intended for covert deployment.

These dragons are trained for infiltration and night operations, where visibility must be minimized. For this purpose, we require a phenotype that allows the dragon to adopt a dark, light-absorbing coloration during nighttime conditions.

However, this trait cannot be present during early development or training.

Not all candidates successfully complete covert certification. Those that fail must be reassigned or released into civilian environments. A dragon capable of active night camouflage would not be suitable for either outcome.

Because of this, the system must meet the following conditions:

- The dragon must display no abnormal pigmentation during development or training
- The ability to transition into a darkened state at night must only be enabled after explicit handler approval
- This activation must be externally controlled and administered intentionally
- Once enabled, the system must remain stable and continue to follow the natural day-night cycle

This is not a temporary effect. It is a controlled designation.

Only dragons that pass training should ever possess it.

A reminder, this request is confidential, our contracts have been sent over secure channels, and we expect discretion in handling this matter. 

-- Commander Elric Vayne
""",
        "scientist_letter": """
From: Dr. Elara Voss
Lead Geneticist, Emberfall Hatchery

To the Apprentice,

This case combines two layers of control, and you will need to treat them separately.

The final phenotype is circadian. Once active, the camouflage system should follow the dragon’s internal day-night rhythm, appearing only during nighttime conditions and disappearing during the day.

However, that system must not exist at all during development.

The dragon should not simply suppress the trait early in life. It should be entirely incapable of expressing it until a specific external signal is provided.

Only after that signal is administered should the system become available, at which point it will operate according to the natural circadian cycle.

This should immediately eliminate several simpler approaches.

A system that responds directly to time will not satisfy the approval requirement. A system that responds only to an external trigger will not satisfy the circadian requirement. You will need both.

You are looking for a design in which an external event enables a system, and that system then follows an internal rhythm.

Think carefully about how to separate those two layers.

-- Dr. Elara Voss
""",
        "requirements": [
            "nyxmelanin_present",
            "circadian_control_present",
            "approval_unlock_present",
            "stop_blocks_training_expression",
            "loxp_sites_present",
            "combined_logic_present",
        ],
        "assignment_label": "Scenario 5 - Advanced Design",
        "assignment_description": (
            "This contract combines external approval unlocking with circadian control "
            "of night camouflage."
        ),
        "builder_title": "Build a certified circadian camouflage system",
        "guidance": [
            "Restrict expression to scale pigment cells during nighttime conditions",
            "Avoid expression before covert certification",
            "Ensure activation only after handler approval",
            "Preserve natural day-night camouflage cycling after approval",
        ],
        "goal": "",
        "description": (
            "Advanced Nightfall Drake assignment focused on permanent handler certification "
            "and night-active expression."
        ),
    },
    "scenario_compulsive_hoarding": {
        "name": "Compulsive Hoarding Research Model",
        "difficulty": "Final / Expert",
        "species": {
            "name": "Cairnkeeper Drake",
            "summary": "Research breed with intense object attachment and measurable hoarding behavior",
            "description": (
                "A highly intelligent dragon breed known for intense object attachment, "
                "strong emotional memory, and measurable hoarding behavior."
            ),
            "badge": "Selected for Final Expert Contract",
        },
        "client": {
            "name": "Dr. Mireya Caldus",
            "title": "Professor of Behavioral Neuroscience, Ardent University",
            "short_description": "Needs a precise behavioral research model for compulsive hoarding.",
            "request_summary": "Create a precise research model for studying compulsive hoarding behavior without disrupting normal behavior.",
        },
        "client_letter": """
From: Dr. Mireya Caldus
Professor of Behavioral Neuroscience, Ardent University

Dear Dr. Elara Voss and the Emberfall Genetics Team,

I am reaching out with a request that falls somewhat outside your usual scope.

My laboratory studies the neural basis of complex behaviors across species. We typically source our research animals from a multispecies transgenics supplier. However, I have recently been granted special permission to pursue a project involving a Cairnkeeper Drakes.

Our supplier has declined to work with this species due to its behavioral profile.

The dragons I am studying display a form of compulsive hoarding. They will collect and guard objects of perceived value to an extent that interferes with feeding, rest, and social interaction. Attempts to interrupt this behavior often result in extreme distress responses.

Despite this, the behavior is consistent and measurable, which makes it an ideal model for studying maladaptive reward processing.

Through prior work, my team has narrowed this behavior to activity in the nucleus accumbens and to a subset of reward-sensitive neurons. Reward-sensitive neurons are not exclusive to the nucleus accumbens; related populations exist across multiple brain regions, so region targeting and cell-type targeting are both required.

My team is well aware that social bonding in these animals is strongly associated with oxytocin-expressing neurons also present in the nucleus accumbens. Preserving this system is critical. These systems overlap anatomically but must be treated independently.

I am not interested in eliminating this system. I am interested in selectively reducing its pathological activation.

For this reason, I require a design that meets the following conditions:

- The intervention must be restricted to the nucleus accumbens
- It must target only the specific neuron population associated with compulsive reward-seeking
- It must not interfere with normal feeding, bonding, or exploratory behavior
- It must not produce global behavioral suppression or distress

This is a behavioral study. The animal must remain intact, functional, and observable.

If successful, this model will allow us to study how targeted modulation of a specific neural circuit alters behavior without disrupting the broader system.

I understand that this is not your primary application domain, but I have been assured that your team is capable of this level of precision.

Best Regards,

Dr. Mireya Caldus
""",
        "scientist_letter": """
From: Dr. Elara Voss
Lead Geneticist, Emberfall Hatchery

To the Apprentice,

This is not a standard assignment.

Our work rarely intersects with behavioral research at this level of specificity, and for good reason. The margin for error is extremely small.

You are not being asked to produce a visible trait, or even to enable a discrete function.

You are being asked to modify a system that is already functioning, and to do so without disrupting the organism as a whole.

The client has already identified the relevant brain region, the nucleus accumbens, and has further narrowed the behavior to a specific population of reward-sensitive neurons.

Those reward-sensitive neurons are not exclusive to the nucleus accumbens. Related populations exist in multiple brain regions, which means neuron subtype targeting alone would be too broad and region targeting alone would affect too many cells.

Oxytocin-producing neurons are equally important to this design. They support social bonding and attachment behaviors, and they must be preserved while the reward circuit is modulated.

That should immediately tell you that a single layer of control will not be sufficient.

If you target the entire region, you will affect behaviors that are not part of the problem. If you target the wrong cell population, you will miss the effect entirely. If your system is too broad, you will suppress the animal rather than refine its behavior.

You will need to think in terms of overlap.

Where is the system active? Which cells are involved? Which cells must be excluded?

And most importantly, how do you ensure that your intervention is present only where those conditions intersect?

There is no single correct design for this case. There are, however, many ways to fail it.

I will not be evaluating whether your construct matches mine.

I will be evaluating whether your reasoning is sound. And remember, I am always looking for the simplest design that will get the job done, added complexities can have unintended effects.

Dr. Elara Voss
""",
        "requirements": [
            "region_targeting_present",
            "reward_neuron_targeting_present",
            "modulator_present",
            "intersectional_logic_present",
            "bonding_exclusion_present",
            "avoids_global_suppression",
        ],
        "assignment_label": "Final Scenario - Expert Design",
        "assignment_description": (
            "This scenario tests intersectional neural targeting for a complex "
            "behavioral research model."
        ),
        "builder_title": "Build a precise compulsive hoarding research model",
        "guidance": [
            "Restrict expression to reward-sensitive neurons within the nucleus accumbens",
            "Avoid expression in reward-sensitive neurons outside the nucleus accumbens",
            "Ensure activation only where BOTH region targeting and neuron subtype targeting overlap",
            "Preserve oxytocin-mediated bonding behavior at all costs",
            "Avoid global suppression",
            "Target BOTH region AND neuron subtype",
        ],
        "goal": "",
        "description": (
            "Final expert assignment focused on layered specificity for targeted "
            "behavioral modulation."
        ),
    },
}

DEFAULT_SCENARIO_ID = "scenario_1"


def get_scenario(scenario_id=DEFAULT_SCENARIO_ID):
    return SCENARIOS.get(scenario_id, SCENARIOS[DEFAULT_SCENARIO_ID])
