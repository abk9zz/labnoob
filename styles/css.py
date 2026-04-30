def get_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');

    .stApp {
        background-color: #fffef8;
        background-image: repeating-linear-gradient(
            to bottom,
            #fffef8,
            #fffef8 28px,
            #d3d3d3 29px
        );
    }

    .page {
        padding: 40px;
        font-family: 'Patrick Hand', cursive;
        font-size: 20px;
        line-height: 28px;
        color: #2f2a24;
    }

    .page h1,
    .page h2,
    .page h3 {
        font-family: 'Patrick Hand', cursive;
        color: #1f1a16;
        letter-spacing: 0;
    }

    .notebook-page {
        min-height: 560px;
    }

    .cover-page,
    .final-page {
        max-width: 900px;
        margin: 0 auto;
    }

    .divider {
        width: 4px;
        min-height: 560px;
        background-color: #c2b8a3;
        margin: 0 auto;
    }

    .postit {
        background-color: #fff2a8;
        border: 1px solid #e2cc61;
        box-shadow: 2px 3px 0 rgba(0, 0, 0, 0.12);
        color: #3a321d;
        font-family: 'Patrick Hand', cursive;
        font-size: 19px;
        line-height: 26px;
        padding: 16px;
        transform: rotate(-1deg);
    }

    .stButton > button,
    .stFormSubmitButton > button {
        background-color: #f4f1e8;
        border: 1px solid #c2b8a3;
        border-radius: 8px;
        color: #2f2a24;
        font-family: 'Patrick Hand', cursive;
        font-size: 20px;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        border-color: #8f806b;
        background-color: #ece5d6;
        color: #1f1a16;
    }

    section[data-testid="stSidebar"] {
        background-color: #f4f1e8;
    }
    </style>
    """
