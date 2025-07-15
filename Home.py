import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="CHIQ | Home", page_icon="🏠")

# Judul & Subjudul
st.title("🏠 Home")
st.subheader("Selamat datang di CHIQ: Chemistry Interactive Quiz 🎉")

# Kalimat pengantar seru
st.markdown("""
**Yo, welcome to CHIQ! 😎**

Ini bukan web kimia biasa—ini platform interaktif buat kamu yang mau belajar kimia sambil main kuis seru dan ngumpulin skor kece 🧬🎮

Di sini kamu bisa:
- 📚 Baca materi kimia yang ringkas & gampang dicerna
- 🎯 Main kuis interaktif dan uji pemahaman
- 🏆 Naik peringkat di leaderboard & saingin temenmu

Sekarang, yuk pilih topik awal kamu:
""")

# Link ke halaman materi/game
st.page_link("pages/Kimia_Organik.py", label="🔬 Kimia Organik")
st.page_link("pages/Kimia_Anorganik.py", label="⚗️ Kimia Anorganik")
