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
        html, body, [data-testid="stAppViewContainer"], .stApp {
            height: 100vh !important;
            overflow: hidden !important;
        }

        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }

        [data-testid="stHeader"] {
            display: none !important;
        }

        [data-testid="stToolbar"] {
            right: 0.5rem !important;
        }

        iframe {
            width: 100% !important;
            height: 100vh !important;
            border: 0 !important;
            display: block !important;
        }

        div[data-testid="stVerticalBlock"] > div:has(iframe) {
            height: 100vh !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "FLAMSENTINELLE.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(
    html_content,
    height=1,
    scrolling=False,
)
