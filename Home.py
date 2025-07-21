import streamlit as st
from components import show_sidebar_logo  # FIXED

# Konfigurasi halaman
st.set_page_config(page_title="CHIQ | Home", page_icon="🧪")

# ===== CSS: BACKGROUND + FONT =====
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #1e1b2e, #2a2640);
        color: #f3f3f3;
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1e1b2e, #2a2640);
        background-attachment: fixed;
        color: #f3f3f3;
    }

    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }

    h1, h2, h3, h4, h5, h6 {
        color: #f8f8f8;
        font-weight: 600;
    }

    p, li {
        font-weight: 300;
    }

    .stButton>button {
        border-radius: 8px;
        padding:
