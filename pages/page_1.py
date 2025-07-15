import streamlit as st
import random

st.set_page_config(page_title="Kimia Organik", page_icon="🧪")

st.title("🔬 Kimia Organik")

# Navigasi halaman
if "slide_organik" not in st.session_state:
    st.session_state.slide_organik = "menu"

def ke_slide(nama):
    st.session_state.slide_organik = nama

# Halaman Menu
if st.session_state.slide_organik == "menu":
    st.write("Silakan pilih:")
    st.button("📖 Materi", on_click=ke_slide, args=("materi",))
    st.button("🎮 Game", on_click=ke_slide, args=("game",))

# Halaman Materi
elif st.session_state.slide_organik == "materi":
    st.subheader("📘 Materi Kimia Organik")

    if "materi_topik" not in st.session_state:
        st.session_state.materi_topik = None

    if st.session_state.materi_topik is None:
        st.write("Pilih topik materi:")
        st.button("🛢️ Hidrokarbon", on_click=lambda: st.session_state.update({"materi_topik": "hidrokarbon"}))
        st.button("🧪 Gugus Fungsi", on_click=lambda: st.session_state.update({"materi_topik": "gugus"}))
        st.button("⚖️ Asam Basa", on_click=lambda: st.session_state.update({"materi_topik": "asam_basa"}))
        st.button("🔁 Reaksi Organik", on_click=lambda: st.session_state.update({"materi_topik": "reaksi"}))
        st.markdown("---")
        st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))
    else:
        topik = st.session_state.materi_topik
        if topik == "hidrokarbon":
            st.markdown("## 🛢️ Hidrokarbon")
            st.markdown("""
            - Alkana: ikatan tunggal  
            - Alkena: ikatan rangkap dua  
            - Alkuna: ikatan rangkap tiga  
            - Contoh: metana, etena, asetilena
            """)
        elif topik == "gugus":
            st.markdown("## 🧪 Gugus Fungsi")
            st.markdown("""
            - Alkohol (-OH)  
            - Asam Karboksilat (-COOH)  
            - Amin (-NH₂)  
            - Aldehid (-CHO)  
            - Ketona (C=O)
            """)
        elif topik == "asam_basa":
            st.markdown("## ⚖️ Asam Basa dalam Organik")
            st.markdown("""
            - Asam organik: mengandung -COOH  
            - Basa organik: mengandung -NH₂  
            - Contoh asam: asam asetat  
            - Contoh basa: metilamina  
            - Reaksi netralisasi menghasilkan garam organik
            """)
        elif topik == "reaksi":
            st.markdown("## 🔁 Reaksi Organik")
            st.markdown("""
            - Substitusi: atom digantikan oleh gugus lain  
            - Adisi: penambahan gugus ke ikatan rangkap  
            - Eliminasi: penghilangan gugus dari molekul  
            - Contoh: reaksi alkena dengan HBr
            """)
        st.markdown("---")
        st.button("⬅️ Kembali ke Daftar Materi", on_click=lambda: st.session_state.update({"materi_topik": None}))
        st.button("🏠 Kembali ke Menu", on_click=ke_slide, args=("menu",))

# Halaman Game
elif st.session_state.slide_organik == "game":
    st.markdown("## 🎮 Game Kimia Organik")
    st.markdown("---")

    all_soal = [
        {
            "pertanyaan": "Apa gugus fungsi dari alkohol?",
            "opsi": ["-COOH", "-NH2", "-OH", "-CHO"],
            "jawaban": "-OH",
            "penjelasan": "Alkohol memiliki gugus fungsi -OH (hidroksil).",
            "skor": 3
        },
        {
            "pertanyaan": "Gugus fungsi dari asam karboksilat adalah?",
            "opsi": ["-OH", "-COOH", "-NH2", "-C=O"],
            "jawaban": "-COOH",
            "penjelasan": "Asam karboksilat memiliki gugus -COOH, yang bersifat asam.",
            "skor": 5
        },
        {
            "pertanyaan": "Apa jenis reaksi alkena dengan HBr?",
            "opsi": ["Substitusi", "Eliminasi", "Adisi", "Polimerisasi"],
            "jawaban": "Adisi",
            "penjelasan": "Alkena bereaksi dengan HBr melalui mekanisme adisi karena memiliki ikatan rangkap dua.",
            "skor": 2
        },
        {
            "pertanyaan": "Alkana memiliki ikatan apa?",
            "opsi": ["Tunggal", "Rangkap dua", "Rangkap tiga", "Aromatik"],
            "jawaban": "Tunggal",
            "penjelasan": "Alkana hanya memiliki ikatan tunggal antar atom karbon.",
            "skor": 3
        },
        {
            "pertanyaan": "Etanol termasuk golongan senyawa apa?",
            "opsi": ["Eter", "Aldehid", "Alkohol", "Alkana"],
            "jawaban": "Alkohol",
            "penjelasan": "Etanol adalah alkohol karena memiliki gugus -OH terikat pada karbon jenuh.",
            "skor": 4
        },
        {
            "pertanyaan": "Apa nama senyawa CH₃COOH?",
            "opsi": ["Asam asetat", "Etanol", "Metanol", "Asam format"],
            "jawaban": "Asam asetat",
            "penjelasan": "CH₃COOH adalah nama kimia dari asam asetat atau asam etanoat.",
            "skor": 3
        },
        {
            "pertanyaan": "Benzena termasuk senyawa?",
            "opsi": ["Alkana", "Alkena", "Aromatik", "Aldehid"],
            "jawaban": "Aromatik",
            "penjelasan": "Benzena adalah senyawa aromatik karena memiliki sistem cincin terdelokalisasi.",
            "skor": 4
        }
    ]

    if "leaderboard" not in st.session_state:
        st.session_state.leaderboard = []

    if "player_name" not in st.session_state:
        st.session_state.player_name = ""

    if not st.session_state.player_name:
        name = st.text_input("Masukkan nama kamu dulu ya! 👇")
        if name:
            st.session_state.player_name = name
            st.rerun()
        else:
            st.stop()

    if "random_soal" not in st.session_state:
        st.session_state.random_soal = random.sample(all_soal, len(all_soal))
        st.session_state.index_soal = 0
        st.session_state.skor = 0
        st.session_state.selesai = False

    if st.session_state.selesai:
        total_maks = sum(s["skor"] for s in st.session_state.random_soal)
        st.balloons()
        st.success(f"🎉 {st.session_state.player_name}, skor akhir kamu: {st.session_state.skor} dari {total_maks} poin!")

        st.session_state.leaderboard.append(
            {"nama": st.session_state.player_name, "skor": st.session_state.skor}
        )

        st.markdown("### 🏆 Leaderboard Sementara")
        for i, entry in enumerate(sorted(st.session_state.leaderboard, key=lambda x: x["skor"], reverse=True)[:5]):
            st.write(f"{i+1}. **{entry['nama']}** - {entry['skor']} poin")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔁 Ulang Game"):
                for k in ["random_soal", "index_soal", "skor", "selesai"]:
                    del st.session_state[k]
                st.rerun()
        with col2:
            st.button("📚 Kembali ke Materi", on_click=ke_slide, args=("materi",))
        with col3:
            st.button("🏠 Kembali ke Menu", on_click=ke_slide, args=("menu",))

    else:
        soal = st.session_state.random_soal[st.session_state.index_soal]
        st.markdown(f"**Soal {st.session_state.index_soal + 1} dari {len(st.session_state.random_soal)}**")
        st.info(soal["pertanyaan"])

        opsi_label = ['A', 'B', 'C', 'D']
        opsi_dict = {f"{label}. {teks}": teks for label, teks in zip(opsi_label, soal["opsi"])}
        jawaban_pilihan = st.radio("Pilih jawaban kamu:", list(opsi_dict.keys()), key=st.session_state.index_soal)
        jawaban = opsi_dict[jawaban_pilihan]

        if st.button("✅ Cek Jawaban"):
            if jawaban == soal["jawaban"]:
                st.success(f"Jawaban kamu BENAR! (+{soal['skor']} poin)")
                st.session_state.skor += soal["skor"]
            else:
                st.error(f"Salah 😢 Jawaban benar: **{soal['jawaban']}** (+0 poin)")

            st.info(f"💡 Penjelasan: {soal['penjelasan']}")

            st.session_state.index_soal += 1
            if st.session_state.index_soal >= len(st.session_state.random_soal):
                st.session_state.selesai = True
            st.rerun()

    st.markdown("---")
    st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))
