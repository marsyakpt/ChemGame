import streamlit as st

st.title("🔬 Kimia Organik")

# Inisialisasi status halaman
if "slide_organik" not in st.session_state:
    st.session_state.slide_organik = "menu"

def ke_slide(nama):
    st.session_state.slide_organik = nama

# Menu awal
if st.session_state.slide_organik == "menu":
    st.write("Silakan pilih:")
    st.button("📖 Materi", on_click=ke_slide, args=("materi",))
    st.button("🎮 Game", on_click=ke_slide, args=("game",))

# Halaman Materi
elif st.session_state.slide_organik == "materi":
    st.subheader("📘 Materi Kimia Organik")

    # Step 1: Cek apakah sudah pilih topik
    if "materi_topik" not in st.session_state:
        st.session_state.materi_topik = None

    # Step 2: Kalau belum pilih topik, tampilkan daftar topik
    if st.session_state.materi_topik is None:
        st.write("Pilih topik materi:")
        st.button("🛢️ Hidrokarbon", on_click=lambda: st.session_state.update({"materi_topik": "hidrokarbon"}))
        st.button("🧪 Gugus Fungsi", on_click=lambda: st.session_state.update({"materi_topik": "gugus"}))
        st.button("⚖️ Asam Basa", on_click=lambda: st.session_state.update({"materi_topik": "asam_basa"}))
        st.button("🔁 Reaksi Organik", on_click=lambda: st.session_state.update({"materi_topik": "reaksi"}))
        st.markdown("---")
        st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))

    # Step 3: Kalau sudah pilih topik, tampilkan materinya
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
            - Adisi: penambahan atom/gugus ke ikatan rangkap  
            - Eliminasi: penghilangan gugus dari molekul  
            - Contoh: reaksi alkena dengan HBr
            """)

        # Tombol kembali ke daftar topik
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
            "penjelasan": "Asam karboksilat memiliki gugus -COOH yang bersifat asam.",
            "skor": 5
        },
        {
            "pertanyaan": "Apa jenis reaksi alkena dengan HBr?",
            "opsi": ["Substitusi", "Eliminasi", "Adisi", "Polimerisasi"],
            "jawaban": "Adisi",
            "penjelasan": "Alkena bereaksi dengan HBr melalui mekanisme adisi karena ikatan rangkap.",
            "skor": 2
        }
    ]

    if "leaderboard" not in st.session_state:
        st.session_state.leaderboard = []

    if "player_name" not in st.session_state:
        st.session_state.player_name = ""

    if not st.session_state.player_name:
        st.session_state.player_name = st.text_input("Masukkan nama kamu dulu ya! 👇")
        if st.session_state.player_name:
            st.experimental_rerun()
        else:
            st.stop()

    if "random_soal" not in st.session_state:
        import random
        st.session_state.random_soal = random.sample(all_soal, len(all_soal))
        st.session_state.index_soal = 0
        st.session_state.skor = 0
        st.session_state.selesai = False

    if st.session_state.selesai:
        total_maks = sum(soal["skor"] for soal in st.session_state.random_soal)
        st.balloons()
        st.success(f"🎉 {st.session_state.player_name}, skor akhir kamu: {st.session_state.skor} dari {total_maks} poin!")

        st.session_state.leaderboard.append(
            {"nama": st.session_state.player_name, "skor": st.session_state.skor}
        )

        st.markdown("### 🏆 Leaderboard Sementara")
        leaderboard = sorted(st.session_state.leaderboard, key=lambda x: x["skor"], reverse=True)
        for i, entry in enumerate(leaderboard[:5]):
            st.write(f"{i+1}. **{entry['nama']}** - {entry['skor']} poin")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔁 Ulang Game"):
                del st.session_state.random_soal
                del st.session_state.index_soal
                del st.session_state.skor
                del st.session_state.selesai
                st.experimental_rerun()
        with col2:
            st.button("📚 Kembali ke Materi", on_click=ke_slide, args=("materi",))
        with col3:
            st.button("🏠 Kembali ke Home", on_click=ke_slide, args=("menu",))

    else:
        soal = st.session_state.random_soal[st.session_state.index_soal]
        st.markdown(f"**Soal {st.session_state.index_soal + 1} dari {len(st.session_state.random_soal)}**")
        st.info(soal["pertanyaan"])

        opsi_label = ['A', 'B', 'C', 'D']
        opsi_dict = {f"{label}. {teks}": teks for label, teks in zip(opsi_label, soal["opsi"])}
        jawaban_dipilih = st.radio("Pilih jawaban kamu:", list(opsi_dict.keys()), key=st.session_state.index_soal)
        jawaban = opsi_dict[jawaban_dipilih]

        if st.button("✅ Cek Jawaban"):
            if jawaban == soal["jawaban"]:
                st.success(f"Jawaban kamu BENAR! 👍 (+{soal['skor']} poin)")
                st.session_state.skor += soal["skor"]
            else:
                st.error(f"Salah 😢 Jawaban yang benar: **{soal['jawaban']}** (+0 poin)")

            st.info(f"💡 Penjelasan: {soal['penjelasan']}")

            st.session_state.index_soal += 1
            if st.session_state.index_soal >= len(st.session_state.random_soal):
                st.session_state.selesai = True

            st.experimental_rerun()

    st.markdown("---")
    st.button("⬅️ Kembali", on_click=ke_slide, args=("menu",))

