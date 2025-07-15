import streamlit as st

st.title("Halo! Selamat Datang di Game Kimia! 🎉")
st.subheader("Kamu mau ngapain dulu nih? Pilih halaman:")

st.page_link("pages/page_1.py", label="🔬 Kimia Organik")
st.page_link("pages/page_2.py", label="⚗️ Kimia Anorganik")
