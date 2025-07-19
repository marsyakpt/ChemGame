import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Setup akses Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Buka Sheet pakai ID 
sheet = client.open_by_key("173bLLhKkH4n0R9HVc4h1ySbXPtp_edpjLPw8DPsb-lg").sheet1  # Ganti dengan ID Sheet 

# Header & Deskripsi
st.set_page_config(page_title="Tentang CHiQ", page_icon="📌")
st.title("📌 Tentang Aplikasi CHiQ")
st.markdown("""
CHiQ adalah aplikasi kuis kimia interaktif yang dibangun untuk membuat pembelajaran jadi fun, visual, dan anti monoton 🎉

### 👩‍🔬 Tim Pengembang CHiQ:
- Fathia Arifahanum M Nur — 2460368  
- Marsya Kartika Putri — 2460412  
- Nuri Septrianti — 2460475  
- Terrie Aulia Hannifa — 2460526  
""")

st.markdown("---")
st.header("💬 Kotak Saran")

# Input user
nama = st.text_input("🧪 Nama kamu (opsional)")
saran = st.text_area("💡 Tulis saran, ide, atau harapan kamu buat CHiQ")

if st.button("Kirim Saran"):
    if saran.strip():
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([waktu, nama, saran])
        st.success("✅ Saran kamu sudah masuk ke lab CHiQ! Terima kasih atas kontribusinya 💌")
    else:
        st.warning("⚠️ Eh, sarannya belum ditulis nih. Yuk diisi dulu 😅")
