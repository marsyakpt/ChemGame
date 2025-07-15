import streamlit as st

st.title("Kimia Anorganik")

opsi = st.radio("Pilih menu:", ["Materi", "Game"])

if opsi == "Materi":
    st.subheader("Materi Kimia Anorganik")
    st.write("""
    - Tabel periodik unsur
    - Ikatan ionik, kovalen, dan logam
    - Senyawa kompleks
    """)
else:
    st.subheader("Game Kimia Anorganik 🎮")
    soal = st.radio("Manakah logam alkali berikut?", ["Mg", "Ca", "Na", "Fe"])
    if st.button("Cek Jawaban"):
        if soal == "Na":
            st.success("Benar! Na adalah logam alkali.")
        else:
            st.error("Salah! Jawaban yang benar adalah Na.")
