import streamlit as st
import random

st.set_page_config(page_title="Kimia Anorganik", page_icon="⚗️")
st.title("⚗️ Kimia Anorganik")

# Navigasi halaman
if "slide_anorganik" not in st.session_state:
    st.session_state.slide_anorganik = "menu"

def ke_slide(nama):
    st.session_state.slide_anorganik = nama

# ---------------------- MENU ----------------------
if st.session_state.slide_anorganik == "menu":
    st.write("Silakan pilih:")
    st.button("📖 Materi", on_click=ke_slide, args=("materi",))
    st.button("🎮 Game", on_click=ke_slide, args=("game",))

# --------------------- MATERI ---------------------
elif st.session_state.slide_anorganik == "materi":
    st.subheader("📘 Materi Kimia Anorganik")
    st.markdown("## ⚗️ Praktikum Digital CHIQ")

    st.markdown("""
    “Pernah lihat nyala api berwarna hijau di laboratorium? Atau larutan yang tiba-tiba mengendap saat ditetesin reagen?”  
    Di materi Kimia Anorganik CHiQ, kamu akan belajar mengenali senyawa anorganik lewat dua uji populer: 🔥 **Uji Nyala** dan 🧪 **Uji Kualitatif**.

    Materi disajikan dalam gaya praktikum digital: singkat, aplikatif, dan bikin kamu ngerasa kayak bantu dosen di lab! 😄
    """)

    st.markdown("### 📘 Materi yang Akan Kamu Pelajari:")
    st.markdown("""
    - 🔥 **Uji Nyala:** Kenali ion logam berdasarkan warna api. Contoh: Na⁺ → kuning, Cu²⁺ → biru kehijauan  
    - 🧪 **Uji Kualitatif:** Identifikasi ion lewat reaksi khas seperti endapan & perubahan warna. Contoh: Cl⁻ + Ag⁺ → endapan putih
    """)

    st.markdown("### 🎯 Jalur Belajar Kamu:")
    st.markdown("""
    Pilih salah satu:
    - 📖 *Baca Materi* — pelajari reaksi dan interpretasi  
    - 🎮 *Langsung ke Game* — uji seberapa cepat kamu mengenali senyawa
    """)


    if "materi_topik_anorganik" not in st.session_state:
        st.session_state.materi_topik_anorganik = None

    if st.session_state.materi_topik_anorganik is None:
        st.write("Pilih topik materi:")
        st.button("🔢 Tabel Periodik", on_click=lambda: st.session_state.update({"materi_topik_anorganik": "periodik"}))
        st.button("🔧 Sifat Logam & Non-Logam", on_click=lambda: st.session_state.update({"materi_topik_anorganik": "sifat"}))
        st.button("💧 Reaksi Asam Basa", on_click=lambda: st.session_state.update({"materi_topik_anorganik": "asam_basa"}))
        st.button("🔗 Senyawa Kompleks", on_click=lambda: st.session_state.update({"materi_topik_anorganik": "kompleks"}))
        st.button("🔥 Redoks", on_click=lambda: st.session_state.update({"materi_topik_anorganik": "redoks"}))
        st.markdown("---")
        st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))
    else:
        topik = st.session_state.materi_topik_anorganik
        if topik == "periodik":
            st.markdown("## 🔢 Tabel Periodik")
            st.markdown("- Golongan & periode\n- Sifat periodik: jari-jari atom, energi ionisasi, keelektronegatifan")
        elif topik == "sifat":
            st.markdown("## 🔧 Sifat Logam & Non-Logam")
            st.markdown("- Logam: konduktor, mengkilap, mudah ditempa\n- Non-logam: isolator, rapuh, tidak mengkilap")
        elif topik == "asam_basa":
            st.markdown("## 💧 Reaksi Asam Basa")
            st.markdown("- Asam: donor proton (H⁺)\n- Basa: akseptor proton\n- Reaksi netralisasi: asam + basa → garam + air")
        elif topik == "kompleks":
            st.markdown("## 🔗 Senyawa Kompleks")
            st.markdown("- Contoh: [Cu(NH₃)₄]²⁺\n- Sifat warna & bentuk geometris")
        elif topik == "redoks":
            st.markdown("## 🔥 Oksidasi-Reduksi")
            st.markdown("- Oksidasi: pelepasan e⁻\n- Reduksi: penerimaan e⁻\n- Contoh: Fe³⁺ + e⁻ → Fe²⁺")

        st.markdown("---")
        st.button("⬅️ Kembali", on_click=lambda: st.session_state.update({"materi_topik_anorganik": None}))
        st.button("🏠 Menu", on_click=ke_slide, args=("menu",))

# ---------------------- GAME ----------------------
elif st.session_state.slide_anorganik == "game":
    st.subheader("🎮 Game Kimia Anorganik")
    st.markdown("---")

    all_soal_anorganik = [
        {"pertanyaan": "Unsur golongan alkali tanah adalah?", "opsi": ["Na", "Mg", "Cl", "Fe"], "jawaban": "Mg", "penjelasan": "Golongan alkali tanah meliputi Be, Mg, Ca, dll.", "skor": 3},
        {"pertanyaan": "Asam sulfat memiliki rumus kimia?", "opsi": ["HCl", "HNO₃", "H₂SO₄", "H₂CO₃"], "jawaban": "H₂SO₄", "penjelasan": "H₂SO₄ adalah nama lain dari asam sulfat.", "skor": 4},
        {"pertanyaan": "Fe³⁺ + e⁻ → Fe²⁺ adalah proses?", "opsi": ["Oksidasi", "Reduksi", "Netralisasi", "Ionisasi"], "jawaban": "Reduksi", "penjelasan": "Reduksi adalah penerimaan elektron.", "skor": 2},
        {"pertanyaan": "Kompleks [Cu(NH₃)₄]²⁺ berwarna?", "opsi": ["Biru", "Merah", "Hijau", "Kuning"], "jawaban": "Biru", "penjelasan": "Ion kompleks Cu²⁺ + NH₃ menghasilkan warna biru.", "skor": 3},
        {"pertanyaan": "Sifat logam yang paling umum adalah?", "opsi": ["Mudah larut", "Mudah terbakar", "Mengkilap", "Tidak reaktif"], "jawaban": "Mengkilap", "penjelasan": "Logam biasanya punya permukaan mengkilap.", "skor": 2},
    ]

    if "leaderboard_anorganik" not in st.session_state:
        st.session_state.leaderboard_anorganik = []

    if "player_name_anorganik" not in st.session_state:
        st.session_state.player_name_anorganik = ""

    if not st.session_state.player_name_anorganik:
        name = st.text_input("Masukkan nama kamu dulu ya! 👇")
        if name:
            st.session_state.player_name_anorganik = name
            st.rerun()
        else:
            st.stop()

    if "random_soal_anorganik" not in st.session_state:
        st.session_state.random_soal_anorganik = random.sample(all_soal_anorganik, len(all_soal_anorganik))
        st.session_state.index_soal_anorganik = 0
        st.session_state.skor_anorganik = 0
        st.session_state.jawaban_dipilih_anorganik = None
        st.session_state.tampilkan_penjelasan_anorganik = False
        st.session_state.selesai_anorganik = False

    if st.session_state.selesai_anorganik:
        total_maks = sum(s["skor"] for s in st.session_state.random_soal_anorganik)
        st.balloons()
        st.success(f"🎉 {st.session_state.player_name_anorganik}, skor kamu: {st.session_state.skor_anorganik}/{total_maks} poin")

        st.session_state.leaderboard_anorganik.append(
            {"nama": st.session_state.player_name_anorganik, "skor": st.session_state.skor_anorganik}
        )

        st.markdown("### 🏆 Leaderboard Sementara")
        for i, entry in enumerate(sorted(st.session_state.leaderboard_anorganik, key=lambda x: x["skor"], reverse=True)[:5]):
            st.write(f"{i+1}. **{entry['nama']}** - {entry['skor']} poin")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔁 Ulang Game"):
                for key in ["random_soal_anorganik", "index_soal_anorganik", "skor_anorganik", "jawaban_dipilih_anorganik", "tampilkan_penjelasan_anorganik", "selesai_anorganik"]:
                    del st.session_state[key]
                st.rerun()
        with col2:
            st.button("📚 Kembali ke Materi", on_click=ke_slide, args=("materi",))
        with col3:
            st.button("🏠 Menu", on_click=ke_slide, args=("menu",))

    else:
        soal = st.session_state.random_soal_anorganik[st.session_state.index_soal_anorganik]
        st.markdown(f"**Soal {st.session_state.index_soal_anorganik + 1} dari {len(st.session_state.random_soal_anorganik)}**")
        st.info(soal["pertanyaan"])

        opsi_label = ['A', 'B', 'C', 'D']
        opsi_dict = {f"{label}. {text}": text for label, text in zip(opsi_label, soal["opsi"])}

        jawaban_dipilih = st.radio("Pilih jawaban:", list(opsi_dict.keys()), key=f"radio_{st.session_state.index_soal_anorganik}")
        jawaban = opsi_dict[jawaban_dipilih]

        if st.button("✅ Cek Jawaban"):
            st.session_state.tampilkan_penjelasan_anorganik = True
            st.session_state.jawaban_dipilih_anorganik = jawaban
            if jawaban == soal["jawaban"]:
                st.session_state.skor_anorganik += soal["skor"]
            st.rerun()

        if st.session_state.tampilkan_penjelasan_anorganik:
            if st.session_state.jawaban_dipilih_anorganik == soal["jawaban"]:
                st.success(f"✅ Jawaban kamu BENAR! (+{soal['skor']} poin)")
            else:
                st.error(f"❌ Salah. Jawaban benar: **{soal['jawaban']}**")

            st.info(f"💡 Penjelasan: {soal['penjelasan']}")

            if st.button("➡️ Lanjut Soal"):
                st.session_state.index_soal_anorganik += 1
                st.session_state.jawaban_dipilih_anorganik = None
                st.session_state.tampilkan_penjelasan_anorganik = False
                if st.session_state.index_soal_anorganik >= len(st.session_state.random_soal_anorganik):
                    st.session_state.selesai_anorganik = True
                st.rerun()

        st.markdown("---")
        st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))
