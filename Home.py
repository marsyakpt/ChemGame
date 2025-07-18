st.set_page_config(page_title="CHIQ | Home", page_icon="🧪")

# Sidebar berisi logo + teks utama
with st.sidebar:
    st.image("logo.png.png", width=120)
    st.markdown("### Yo, welcome to CHIQ! 😎")
    st.markdown("Chemistry Interactive Quiz")

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
st.markdown("### 💡 Fun Fact Kimia!")

st.markdown("""
- 🍌 **Pisang itu sedikit radioaktif!** Karena mengandung isotop alami kalium-40. Tapi tenang, kamu gak akan glow in the dark 😆  
- ❄️ **Air bisa membeku dan mendidih sekaligus!** Di titik triple, air bisa berada di fase padat, cair, dan gas secara bersamaan  
- 💎 **Grafit dan berlian itu sama-sama karbon!** Bedanya cuma di cara atomnya tersusun. Satu jadi pensil, satu jadi cincin tunangan 💍  
- 🌩️ **Petir bisa bikin ozon!** Makanya setelah badai, kamu kadang cium bau “segar” yang khas—itu ozon hasil reaksi di atmosfer  
- 🔥 **Glow stick bersinar karena reaksi kimia!** Namanya *chemiluminescence*, reaksi yang menghasilkan cahaya tanpa panas  
""")
