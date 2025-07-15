import streamlit as st

st.title("⚗️ Kimia Anorganik")

# Inisialisasi status
if "slide_anorganik" not in st.session_state:
    st.session_state.slide_anorganik = "menu"

# Fungsi untuk berpindah slide
def ke_slide(nama):
    st.session_state.slide_anorganik = nama

# Menu utama Kimia Anorganik
if st.session_state.slide_anorganik == "menu":
    st.write("Mau belajar atau main game?")
    st.button("📖 Materi", on_click=ke_slide, args=("materi",))
    st.button("🎮 Game", on_click=ke_slide, args=("game",))

# Halaman Materi
elif st.session_state.slide_anorganik == "materi":
    st.subheader("📘 Materi Kimia Anorganik")
    st.markdown("""
    - Tabel periodik unsur
    - Ikatan ionik, kovalen, dan logam
    - Senyawa kompleks
    - Reaksi redoks dan elektrokimia
    """)
    st.button("⬅️ Kembali", on_click=ke_slide, args=("menu",))

# Halaman Game
elif st.session_state.slide_anorganik == "game":
    st.subheader("🎮 Game Kimia Anorganik")
    soal = st.radio("Unsur manakah yang termasuk logam alkali?", ["Ca", "Mg", "Na", "Al"])
    if st.button("Cek Jawaban"):
        if soal == "Na":
            st.success("✅ Benar! Na (natrium) adalah logam alkali.")
        else:
            st.error("❌ Salah! Jawaban yang benar adalah Na.")
    st.button("⬅️ Kembali", on_click=ke_slide, args=("menu",))
