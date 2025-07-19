import streamlit as st
import requests

# Konfigurasi halaman
st.set_page_config(page_title="Tentang Web", page_icon="📌")

# ===== CSS / FONT =====
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #1e1b2e, #2a2640);
        color: #f3f3f3;
    }

    h1, h2, h3 {
        color: #f8f8f8;
        font-weight: 600;
    }

    .stButton>button {
        border-radius: 8px;
        background-color: #6c5ce7;
        color: white;
        transition: 0.3s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #a29bfe;
        color: black;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== ISI HALAMAN UTAMA =====
st.title("📌 Tentang Web Ini")
st.markdown("""
### 👩‍🔬 Apa itu CHIQ?
CHIQ adalah singkatan dari **Chemistry Interactive Quiz** — platform edukatif berbasis web yang menyajikan **materi kimia ringkas dan kuis interaktif** dengan tampilan menarik.

---

### 🎯 Latar Belakang
Web ini dibuat untuk membantu supaya belajar kimia bisa jadi lebih fun, interaktif, dan nggak membosankan.  
Lewat CHIQ, kamu bisa belajar dengan:
- 📚 Materi visual & singkat  
- 🎮 Kuis seru dan menantang  
- 🏆 Leaderboard dan skor buat ngelacak sejauh mana pemahaman kamu berkembang

---

### 💬 Kotak Saran
Kami sangat terbuka dengan masukanmu!  
Silakan isi form di bawah ini:
""")

# ===== FORM SARAN DI HALAMAN UTAMA =====
with st.form(key="form_saran"):
    nama = st.text_input("🧪 Nama kamu (opsional)")
    saran = st.text_area("💡 Masukkan saran/kritik kamu di sini")
    kirim = st.form_submit_button("Kirim Saran")

    if kirim:
        if nama and saran:
            form_url = "https://docs.google.com/forms/d/e/1FAIpQLSclXEvPTa6hOHn8Ybfr7PEMQs3Ddw8mtrvV3emYUPAa-5G9UA/formResponse"
            form_data = {
                "entry.2005620554": nama,
                "entry.1045781291": saran
            }

            try:
                response = requests.post(form_url, data=form_data)
                if response.status_code in [200, 302]:
                    st.success("🎉 Terima kasih atas sarannya!")
                else:
                    st.warning("⚠️ Saran sudah dikirim, tapi Google Form tidak merespon dengan baik.")
            except Exception as e:
                st.error(f"🚨 Gagal mengirim saran: {e}")
        else:
            st.warning("⚠️ Isi nama dan saran dulu ya sebelum dikirim.")
