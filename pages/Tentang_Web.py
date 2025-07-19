import streamlit as st

st.set_page_config(page_title="Tentang CHiQ", page_icon="📌")

st.title("📌 Tentang Aplikasi CHiQ")
st.markdown("""
CHiQ adalah aplikasi kuis kimia interaktif yang dibangun untuk membuat pembelajaran jadi fun, visual, dan anti monoton 🎉

### 👨‍🔬 Tim Pengembang:
- Fathia Arifahanum M Nur 2460368
- Marsya Kartika Putri — 2460412
- Nuri Septrianti — 2460475
- Terrie Aulia hannifa — 2460526
""")

st.markdown("---")
st.header("💬 Kotak Saran")
saran = st.text_area("Tulis ide atau harapan kamu buat CHiQ")

if st.button("Kirim Saran"):
    if saran.strip():
        st.success("Terima kasih! Saran kamu sudah terkirim 💌")
    else:
        st.warning("Isi dulu dong sebelum dikirim 😅")

