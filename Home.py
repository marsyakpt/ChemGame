import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")
st.title("🏠 Home")
st.subheader("Selamat datang di Game & Materi Kimia! 🎉")

st.page_link("pages/Kimia_Organik.py", label="🔬 Kimia Organik")
st.page_link("pages/Kimia_Anorganik.py", label="⚗️ Kimia Anorganik")
