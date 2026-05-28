import streamlit as st
import os

st.set_page_config(
    page_title="☀️ Manmeet Summer Diet — June 2026",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide ALL Streamlit chrome so the HTML fills the full window
st.markdown("""
<style>
    /* Hide every piece of Streamlit UI */
    #MainMenu, footer, header, .stDeployButton,
    [data-testid="stToolbar"], [data-testid="stDecoration"],
    [data-testid="stStatusWidget"], [data-testid="collapsedControl"],
    [data-testid="stSidebarNav"] { display: none !important; visibility: hidden !important; }

    /* Remove all padding so the iframe fills edge-to-edge */
    .main .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    .main { padding: 0 !important; margin: 0 !important; }
    html, body { margin: 0; padding: 0; overflow: hidden; background: #050a0e; }

    /* iframe itself fills the viewport */
    iframe {
        display: block;
        border: none;
        width: 100vw;
        height: 100vh;
    }
</style>
""", unsafe_allow_html=True)

# ── Load the HTML file ──────────────────────────────────────────────────────
html_path = os.path.join(os.path.dirname(__file__), "manmeet-summer-diet.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Inject a tiny patch so the site knows it's inside Streamlit
    # (removes the custom cursor conflict and fixes vh units in iframe)
    patch = """
    <style>
      /* iframe viewport fix — vh units don't behave in iframes on some browsers */
      #hero { min-height: 100vh; }
      /* Ensure body scroll works inside iframe */
      body { overflow-y: auto !important; }
    </style>
    """
    html_content = html_content.replace("</head>", patch + "</head>", 1)

    # Render — scrolling=True lets the user scroll through the site
    st.components.v1.html(html_content, height=5800, scrolling=True)
else:
    st.error("⚠️ manmeet-summer-diet.html not found. Make sure it's in the same folder as app.py.")
    st.code("Your repo structure should be:\n  app.py\n  manmeet-summer-diet.html\n  requirements.txt\n  .streamlit/config.toml")
