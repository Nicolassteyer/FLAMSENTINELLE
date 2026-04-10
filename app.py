from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FLAMSENTINELLE",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }

        .stApp {
            margin: 0 !important;
            padding: 0 !important;
        }

        [data-testid="stHeader"] {
            display: none;
        }

        [data-testid="stToolbar"] {
            right: 0.5rem;
        }

        iframe {
            width: 100% !important;
            border: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "FLAMSENTINELLE.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(
    html_content,
    height=2200,
    scrolling=True,
)
