def get_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Inter:wght@400;500;600;700&family=Libre+Baskerville:wght@400;700&display=swap');

    :root {
        --ink: #2d2117;
        --muted: #624934;
        --ember: #8d4428;
        --ember-dark: #67311f;
        --gold: #c99445;
        --parchment: #fff6df;
        --panel: rgba(255, 248, 229, 0.94);
        --line: rgba(98, 73, 52, 0.24);
    }

    .stApp {
        background:
            radial-gradient(circle at 8% 4%, rgba(197, 107, 53, 0.20), transparent 24rem),
            radial-gradient(circle at 90% 18%, rgba(69, 123, 108, 0.16), transparent 22rem),
            linear-gradient(135deg, #faefd6 0%, #ead4aa 48%, #d2ad70 100%);
        color: var(--ink);
        font-family: "Inter", sans-serif;
    }

    .block-container {
        max-width: 980px;
        margin-left: auto;
        margin-right: auto;
        padding-top: 3.5rem;
        padding-bottom: 4rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    section[data-testid="stSidebar"],
    div[data-testid="stSidebar"],
    div[data-testid="collapsedControl"] {
        display: none;
    }

    div[data-testid="stSidebarContent"] {
        visibility: hidden;
    }

    .app-shell {
        max-width: 900px;
        margin: 0 auto 1.5rem auto;
        text-align: center;
    }

    .app-shell,
    .app-shell h1,
    .app-shell h2,
    .app-shell h3,
    .app-shell p,
    .app-shell div,
    .app-shell strong {
        text-align: center !important;
    }

    .app-shell p,
    .app-shell h2,
    .centered-subtitle {
        max-width: 700px;
        margin-left: auto !important;
        margin-right: auto !important;
        text-align: center !important;
    }

    .cover-shell {
        padding-top: 4rem;
    }

    .eyebrow {
        margin: 0 0 0.5rem 0;
        color: var(--ember-dark);
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0.14em;
        text-transform: uppercase;
    }

    h1,
    h2,
    h3,
    h4 {
        color: var(--ink);
        font-family: "Cinzel", serif;
        letter-spacing: 0;
    }

    h1 {
        font-size: 3rem;
        margin: 0 0 1rem 0;
    }

    h2 {
        color: var(--ember-dark);
        font-size: 1.25rem;
        margin-top: 0;
    }

    .intro {
        color: var(--muted);
        font-size: 1.12rem;
        line-height: 1.75;
        margin: 0 auto;
        max-width: 740px;
        text-align: center;
    }

    .intro.small {
        font-size: 1rem;
    }

    .centered-subtitle {
        max-width: 700px;
        margin: 0 auto 2rem auto;
        text-align: center !important;
    }

    .contract-card,
    .detail-panel,
    .base-card,
    .result-panel,
    .construct-row {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 8px;
        box-shadow: 0 12px 28px rgba(61, 35, 16, 0.14);
    }

    .contract-card {
        align-items: flex-start;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        height: 100%;
        min-height: 196px;
        padding: 1.25rem;
        text-align: left;
    }

    .contract-card h3 {
        font-size: 1.32rem;
        margin: 0 0 0.35rem 0;
    }

    .contract-card p {
        color: var(--muted);
        line-height: 1.55;
        margin: 0.6rem 0 0 0;
    }

    .contract-card p:last-child {
        flex: 1;
    }

    .client-role {
        color: var(--ember) !important;
        font-size: 0.88rem;
        font-weight: 800;
    }

    .detail-panel {
        padding: 1.4rem;
        text-align: center;
    }

    .detail-panel h1,
    .detail-panel h2 {
        text-align: center;
    }

    .requirements {
        background: rgba(255, 255, 255, 0.34);
        border: 1px solid rgba(98, 73, 52, 0.14);
        border-radius: 8px;
        margin-top: 1.4rem;
        padding: 1rem 1.15rem;
    }

    .requirements ul {
        color: var(--muted);
        line-height: 1.75;
        margin-bottom: 0;
    }

    .letter-wrap {
        margin: 0 auto 1.4rem auto;
        max-width: 760px;
    }

    .letter-paper {
        background:
            linear-gradient(180deg, rgba(255, 252, 238, 0.7), rgba(244, 226, 184, 0.78)),
            var(--parchment);
        border: 1px solid rgba(98, 73, 52, 0.28);
        border-radius: 8px;
        box-shadow: 0 18px 40px rgba(61, 35, 16, 0.18);
        color: #352617;
        font-family: "Libre Baskerville", Georgia, serif;
        font-size: 1.02rem;
        line-height: 1.8;
        padding: 2.25rem 2.45rem;
        text-align: left;
    }

    .letter-paper p {
        margin: 0 0 1.05rem 0;
    }

    .letter-paper p:last-child {
        margin-bottom: 0;
    }

    .section-heading {
        font-size: 1.35rem;
        margin: 1.25rem 0 0.8rem 0;
    }

    .base-card {
        min-height: 230px;
        padding: 1rem;
        text-align: left;
    }

    .species-grid {
        margin: 0 auto 1.4rem auto;
        max-width: 620px;
    }

    .species-card {
        min-height: 0;
        padding: 1.35rem;
    }

    .species-card h3 {
        font-size: 1.55rem;
        margin: 0.35rem 0 0.45rem 0;
    }

    .base-card.selected {
        border-color: var(--ember);
        box-shadow: 0 0 0 3px rgba(141, 68, 40, 0.16), 0 14px 28px rgba(61, 35, 16, 0.16);
    }

    .base-card h4 {
        font-size: 1.08rem;
        margin: 0.75rem 0 0.5rem 0;
    }

    .base-card p,
    .base-card span {
        color: var(--muted);
        display: block;
        font-size: 0.92rem;
        line-height: 1.5;
    }

    .base-card span {
        color: var(--ember-dark);
        font-weight: 800;
        margin-top: 0.75rem;
    }

    .base-swatch {
        border: 2px solid rgba(255, 246, 223, 0.86);
        border-radius: 50%;
        box-shadow: 0 3px 10px rgba(45, 33, 23, 0.24);
        height: 42px;
        width: 42px;
    }

    .species-pill {
        background: rgba(69, 123, 108, 0.12);
        border: 1px solid rgba(69, 123, 108, 0.24);
        border-radius: 999px;
        color: #315b51;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: 800;
        margin-bottom: 0.9rem;
        padding: 0.35rem 0.75rem;
    }

    .trial-assignment {
        background: rgba(255, 255, 255, 0.36);
        border: 1px solid rgba(141, 68, 40, 0.18);
        border-left: 4px solid var(--ember);
        border-radius: 8px;
        color: var(--ink);
        margin: 0 0 1rem 0;
        padding: 0.8rem 0.95rem;
        text-align: left;
    }

    .trial-assignment strong {
        display: block;
        font-size: 0.98rem;
        margin-bottom: 0.25rem;
    }

    .trial-assignment p {
        color: var(--muted);
        font-size: 0.92rem;
        line-height: 1.5;
        margin: 0;
    }

    .trial-intro {
        margin: 0 auto 1.1rem auto;
        max-width: 740px;
    }

    .trial-badge {
        background: rgba(69, 123, 108, 0.12);
        border: 1px solid rgba(69, 123, 108, 0.22);
        border-radius: 999px;
        color: #315b51;
        display: inline-block;
        align-self: flex-start;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        margin-bottom: 0.75rem;
        padding: 0.25rem 0.55rem;
        text-transform: uppercase;
        width: fit-content;
    }

    .transition-note {
        background: rgba(255, 255, 255, 0.34);
        border: 1px solid rgba(98, 73, 52, 0.14);
        border-radius: 8px;
        color: var(--muted);
        font-size: 0.96rem;
        line-height: 1.55;
        margin: 0 auto 1.4rem auto;
        max-width: 760px;
        padding: 0.85rem 1rem;
        text-align: center;
    }

    .construct-preview {
        background: #3a2a1f;
        border: 1px solid rgba(255, 246, 223, 0.22);
        border-radius: 8px;
        color: #fff6df;
        font-size: 1.05rem;
        line-height: 1.8;
        margin-bottom: 0.9rem;
        padding: 1rem;
        text-align: center;
    }

    .construct-preview strong {
        color: #ffd885;
    }

    .construct-token {
        background: rgba(255, 246, 223, 0.1);
        border: 1px solid rgba(255, 216, 133, 0.38);
        border-radius: 8px;
        color: #ffd885;
        display: inline-block;
        font-weight: 800;
        margin: 0.18rem;
        padding: 0.35rem 0.55rem;
    }

    .construct-arrow {
        color: rgba(255, 246, 223, 0.68);
        font-weight: 800;
    }

    .construct-row {
        margin-bottom: 0.55rem;
        padding: 0.8rem 0.95rem;
    }

    .construct-row strong,
    .construct-row span {
        display: block;
    }

    .construct-row span {
        color: var(--muted);
        font-size: 0.92rem;
        line-height: 1.5;
        margin-top: 0.25rem;
    }

    .result-panel {
        margin-top: 0.9rem;
        padding: 1.2rem;
    }

    .result-panel h3 {
        margin-top: 0;
    }

    .result-panel p {
        color: var(--muted);
        line-height: 1.65;
    }

    .result-panel ul {
        color: var(--muted);
        line-height: 1.65;
        margin-bottom: 0;
    }

    .scientist-guidance,
    .submission-status,
    .library-item {
        background: rgba(255, 255, 255, 0.34);
        border: 1px solid rgba(98, 73, 52, 0.14);
        border-radius: 8px;
        padding: 0.9rem 1rem;
    }

    .scientist-guidance {
        background: rgba(255, 252, 238, 0.72);
        border-color: rgba(141, 68, 40, 0.28);
        margin: 0 auto 1.4rem auto;
        max-width: 900px;
    }

    .scientist-guidance p {
        color: var(--muted);
        line-height: 1.6;
        margin: 0 0 0.45rem 0;
    }

    .scientist-guidance ul {
        color: var(--muted);
        line-height: 1.65;
        margin: 0;
        padding-left: 1.3rem;
    }

    .scientist-guidance li {
        margin: 0 0 0.35rem 0;
    }

    .scientist-guidance strong {
        color: var(--ember-dark);
        display: block;
        margin-top: 0.55rem;
    }

    .library-item strong,
    .submission-status strong {
        color: var(--ember-dark);
    }

    .library-item p {
        color: var(--muted);
        line-height: 1.55;
        margin: 0.35rem 0 0 0;
    }

    .library-item {
        margin-bottom: 0.7rem;
    }

    .library-item span {
        color: var(--ink);
        display: block;
        font-size: 0.92rem;
        line-height: 1.5;
        margin-top: 0.35rem;
    }

    .submission-status {
        min-height: 2.85rem;
    }

    .postit-note {
        background: #fff0a8;
        border: 1px solid rgba(137, 103, 31, 0.32);
        border-radius: 8px;
        box-shadow: 0 8px 18px rgba(80, 57, 22, 0.12);
        color: #4e3b16;
        line-height: 1.6;
        padding: 1rem;
    }

    .stButton > button {
        background: var(--ember-dark);
        border: 1px solid var(--ember-dark);
        border-radius: 8px;
        color: #fff8e8;
        font-weight: 800;
        min-height: 2.85rem;
        transition: all 0.15s ease;
        white-space: normal;
    }

    .stButton > button:hover {
        background: var(--ember);
        border-color: var(--ember);
        color: #fff8e8;
        transform: translateY(-1px);
    }

    .stButton > button:focus,
    .stButton > button:active {
        color: #fff8e8;
    }

    div[data-testid="stExpander"] {
        background: rgba(255, 248, 229, 0.58);
        border: 1px solid var(--line);
        border-radius: 8px;
    }

    div[data-testid="stSelectbox"] label {
        color: var(--ink);
        font-weight: 800;
    }

    @media (max-width: 760px) {
        .block-container {
            padding-top: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        h1 {
            font-size: 2.1rem;
        }

        .cover-shell {
            padding-top: 1rem;
        }

        .base-card {
            min-height: auto;
        }

        .letter-paper {
            font-size: 0.96rem;
            padding: 1.4rem;
        }
    }
    </style>
    """
