import streamlit as st

def show_sidebar_logo():
    st.image("logo.png.2.png", use_container_width=True)

def sidebar_tentang_web():
    st.subheader("Tentang Web")
    st.markdown("""
    **CHIQ - Chemical Interactive Quiz**  
    Aplikasi edukatif ini dibuat oleh **Marsya Kartika Putri** sebagai media interaktif belajar Kimia SMA/K.  
    Tujuannya adalah membuat belajar kimia lebih menyenangkan melalui kuis dan materi visual.

    Dibuat dengan ❤️ menggunakan **Python + Streamlit**.
    """)

    st.markdown("### ✉️ Kotak Saran")

    with st.form("saran_form"):
        nama = st.text_input("Nama (opsional)")
        saran = st.text_area("Masukan / Saran")
        submitted = st.form_submit_button("Kirim")

        if submitted:
            st.success("Terima kasih atas sarannya! 🙏 (Simulasi kirim)")
