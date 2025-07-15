import streamlit as st

st.set_page_config(page_title="Beranda", page_icon="🏠")
st.title("🏠 Beranda")
st.subheader("Selamat datang di Game & Materi Kimia! 🎉")
st.write("Pilih halaman yang ingin kamu jelajahi:")

st.page_link("pages/page_1.py", label="🔬 Kimia Organik")
st.page_link("pages/page_2.py", label="⚗️ Kimia Anorganik")
