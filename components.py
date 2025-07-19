import streamlit as st

def show_sidebar_logo():
    with st.sidebar:
        st.image("logo.png.2.png", use_container_width=True)

def sidebar_tentang_web():
    st.header("📌 Tentang Web")
    st.markdown("""
    **CHIQ (Chemistry Interactive Quiz)** adalah platform edukasi kimia berbasis kuis interaktif yang dikembangkan oleh **Marsya Kartika Putri**, mahasiswa Politeknik AKA Bogor jurusan Analisis Kimia.

    Tujuan utama web ini adalah membuat pembelajaran kimia lebih seru dan mudah dipahami 💡.
    """)

    st.markdown("---")
    st.markdown("### ✉️ Kirim Saran")

    with st.form("form_saran"):
        nama = st.text_input("Nama (opsional)")
        pesan = st.text_area("Saran / Masukan kamu")
        submit = st.form_submit_button("Kirim")

        if submit:
            st.success("Terima kasih! Saranmu sudah terkirim 🤗 (simulasi)")
