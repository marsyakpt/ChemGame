import streamlit as st

st.title("🔬 Kimia Organik")

# Inisialisasi status halaman dalam 1 page
if "slide_organik" not in st.session_state:
    st.session_state.slide_organik = "menu"

# Fungsi navigasi dalam halaman
def ke_slide(nama):
    st.session_state.slide_organik = nama

# Menu awal
if st.session_state.slide_organik == "menu":
    st.write("Silakan pilih:")
    st.button("📖 Materi", on_click=ke_slide, args=("materi",))
    st.button("🎮 Game", on_click=ke_slide, args=("game",))

# Halaman Materi
elif st.session_state.slide_organik == "materi":
    st.subheader("📘 Materi Kimia Organik")
    st.markdown("""
    - Hidrokarbon: alkana, alkena, alkuna
    - Gugus fungsi: -OH, -COOH, -NH2
    - Reaksi: substitusi, adisi, eliminasi
    """)
    st.button("⬅️ Kembali", on_click=ke_slide, args=("menu",))

# Halaman Game
elif st.session_state.slide_organik == "game":
    st.subheader("🎮 Game Kimia Organik")
    soal = st.radio("Apa gugus fungsi dari alkohol?", ["-COOH", "-NH2", "-OH", "-CHO"])
    if st.button("Cek Jawaban"):
        if soal == "-OH":
            st.success("✅ Benar! Alkohol punya gugus -OH.")
        else:
            st.error("❌ Salah! Jawaban yang benar adalah -OH.")
    st.button("⬅️ Kembali", on_click=ke_slide, args=("menu",))
