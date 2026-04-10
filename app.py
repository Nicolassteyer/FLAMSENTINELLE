from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FLAMSENTINELLE",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_path = Path(__file__).parent / "FLAMSENTINELLE.html"
html_content = html_path.read_text(encoding="utf-8")

st.components.v1.html(html_content, height=1200, scrolling=True)
