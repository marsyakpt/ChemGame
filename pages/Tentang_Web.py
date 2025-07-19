import streamlit as st

# Setup halaman
st.set_page_config(page_title="Tentang CHiQ", page_icon="📌")

# Header & Deskripsi
st.title("📌 Tentang Aplikasi CHiQ")
st.markdown("""
CHiQ adalah aplikasi kuis kimia interaktif yang dibangun untuk membuat pembelajaran jadi fun, visual, dan anti monoton 🎉

### 👩‍🔬 Tim Pengembang CHiQ:
- Fathia Arifahanum M Nur — 2460368  
- Marsya Kartika Putri — 2460412  
- Nuri Septrianti — 2460475  
- Terrie Aulia Hannifa — 2460526  
""")

# Pemisah konten
st.markdown("---")

# Form Kotak Saran
st.header("💬 Kotak Saran")

nama = st.text_input("🧪 Nama kamu (opsional)")
saran = st.text_area("💡 Tulis saran atau ide buat CHiQ")

if st.button("Kirim Saran"):
    if saran.strip():
        st.success("✅ Saran kamu sudah terkirim dan siap dianalisis di lab CHiQ! Terima kasih 💌")
        # Di sini nanti bisa tambahkan fungsi simpan ke Sheets
    else:
        st.warning("⚠️ Saran belum diisi. Yuk tulis dulu sebelum dikirim 😅")
