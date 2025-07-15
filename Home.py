import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="CHiQ | Home", page_icon="🧪")

# Header
st.title("Yo, welcome to CHiQ! 😎")
st.subheader("Chemistry Interactive Quiz")

# Narasi pembuka
st.markdown("""
Belajar kimia jadi beda—fun, interaktif, dan anti bikin pusing! 🎉  
CHiQ hadir buat kamu yang mau belajar sambil bermain dan dapetin skor kece! 🧬🎮  
""")

# Fitur-fitur
st.markdown("""
Di CHiQ kamu bisa:
- 📚 Belajar materi kimia yang ringkas & estetik
- 🎯 Main kuis interaktif dan uji pemahaman
- 🏆 Naik peringkat di leaderboard dan saingin temanmu!
""")

# Prompt pilihan topik
st.markdown("### 🔍 Pilih topik awal kamu:")
st.markdown("""
Mau jelajah dunia senyawa karbon atau eksplorasi larutan & reaksi redoks?  
Yuk tentukan jalur belajarmu sekarang:
""")

# Link ke halaman materi
st.page_link("pages/Kimia_Organik.py", label="🔬 Kimia Organik")
st.page_link("pages/Kimia_Anorganik.py", label="⚗️ Kimia Anorganik")

# Bonus section
st.markdown("---")
st.markdown("💡 **Fun Fact CHiQ!**")
st.markdown("""
- Air bisa bikin kamu basah, tapi kimia bikin kamu paham kenapa 🤓  
- Aspirin itu senyawa organik, tapi efeknya kadang bikin lupa deadline 💊  
- Kimia itu tentang reaksi—dan di CHiQ, kamulah katalisnya ⚡  
""")
