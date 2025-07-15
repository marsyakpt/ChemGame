import streamlit as st

st.title("Kimia Organik")

opsi = st.radio("Pilih menu:", ["Materi", "Game"])

if opsi == "Materi":
    st.subheader("Materi Kimia Organik")
    st.write("""
    - Hidrokarbon (alkana, alkena, alkuna)
    - Gugus fungsi: -OH, -COOH, -NH2
    - Reaksi organik: substitusi, adisi, eliminasi
    """)
else:
    st.subheader("Game Kimia Organik 🎮")
    soal = st.radio("Apa gugus fungsi dari alkohol?", ["-COOH", "-NH2", "-OH", "-CHO"])
    if st.button("Cek Jawaban"):
        if soal == "-OH":
            st.success("Benar! Alkohol punya gugus -OH.")
        else:
            st.error("Salah! Yang benar adalah -OH.")
