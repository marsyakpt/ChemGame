import streamlit as st
from components import show_sidebar_logo, sidebar_tentang_web

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
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        background-color: #6c5ce7;
        color: white;
        border: none;
        transition: 0.3s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #a29bfe;
        color: black;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== SIDEBAR =====
with st.sidebar:
    menu = st.radio("Navigasi", ["Home", "Kimia Anorganik", "Kimia Organik", "Tentang Web"])
    show_sidebar_logo()

# ===== HALAMAN BERDASARKAN MENU =====
if menu == "Home":
    st.image("logo.png.2.png", width=300)

    st.title("Yo, welcome to CHIQ! 😎")
    st.subheader("Chemistry Interactive Quiz")

    st.markdown("""
    Belajar kimia jadi beda—fun, interaktif, dan anti bikin pusing! 🎉  
    CHiQ hadir buat kamu yang mau belajar sambil bermain dan dapetin skor kece! 🧬🎮  
    """)

    st.markdown("""
    Di CHiQ kamu bisa:
    - 📚 Belajar materi kimia yang ringkas & estetik
    - 🎯 Main kuis interaktif dan uji pemahaman
    - 🏆 Naik peringkat di leaderboard untuk melihat sejauh mana kamu memahami materi!
    """)

    st.markdown("### 🔍 Pilih topik awal kamu:")
    st.page_link("pages/Kimia_Organik.py", label="🔬 Kimia Organik")
    st.page_link("pages/Kimia_Anorganik.py", label="⚗️ Kimia Anorganik")

    st.markdown("---")
    st.markdown("### 💡 Fun Fact Kimia!")
    st.markdown("""
    - 🍌 **Pisang itu sedikit radioaktif!**
    - ❄️ **Air bisa membeku & mendidih sekaligus di titik triple!**
    - 💎 **Berlian dan grafit = karbon beda struktur**
    - 🌩️ **Petir bisa membentuk ozon di atmosfer**
    - 🔥 **Glow stick nyala karena reaksi kimia**
    """)

elif menu == "Kimia Anorganik":
    st.switch_page("pages/Kimia_Anorganik.py")

elif menu == "Kimia Organik":
    st.switch_page("pages/Kimia_Organik.py")

elif menu == "Tentang Web":
    sidebar_tentang_web()
