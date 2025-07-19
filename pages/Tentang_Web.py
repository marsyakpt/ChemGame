import streamlit as st

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
""")

# ===== TIM PENGEMBANG =====
st.markdown("---")
st.subheader("👩‍🔬 Tim Pengembang CHIQ")
st.markdown("""
Berikut adalah tim di balik web CHIQ 🎉:

- **Fathia Arifahanum M Nur** — 2460368  
- **Marsya Kartika Putri** — 2460412  
- **Nuri Septrianti** — 2460475  
- **Terrie Aulia Hannifa** — 2460526  
""")

# ===== KOTAK SARAN =====
st.markdown("---")
st.subheader("💬 Kotak Saran")
st.markdown("""
Kami sangat terbuka dengan masukanmu!  
Klik tombol di bawah untuk memberi saran langsung lewat Google Form resmi kami ⬇️
""")

form_link = "https://forms.gle/N5byRH4xtgaia9gt6"
st.markdown(f"[📝 Isi Saran di Google Form]({form_link})", unsafe_allow_html=True)
