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
        {"pertanyaan": "Apa gugus fungsi dari alkohol?", "opsi": ["-COOH", "-NH2", "-OH", "-CHO"], "jawaban": "-OH"},
        {"pertanyaan": "Gugus fungsi dari asam karboksilat adalah?", "opsi": ["-OH", "-COOH", "-NH2", "-C=O"], "jawaban": "-COOH"},
        {"pertanyaan": "Apa jenis reaksi alkena dengan HBr?", "opsi": ["Substitusi", "Eliminasi", "Adisi", "Polimerisasi"], "jawaban": "Adisi"},
        {"pertanyaan": "Alkana memiliki ikatan apa?", "opsi": ["Tunggal", "Rangkap dua", "Rangkap tiga", "Aromatik"], "jawaban": "Tunggal"},
        {"pertanyaan": "Etanol adalah contoh dari?", "opsi": ["Eter", "Aldehid", "Alkohol", "Alkana"], "jawaban": "Alkohol"},
    ]

    if "leaderboard" not in st.session_state:
        st.session_state.leaderboard = []

    if "player_name" not in st.session_state or not st.session_state.player_name:
        nama = st.text_input("Masukkan nama kamu dulu ya! 👇")
        if nama:
            st.session_state.player_name = nama
            st.rerun()
        else:
            st.stop()

    if "random_soal" not in st.session_state:
        import random
        st.session_state.random_soal = random.sample(all_soal, 3)
        st.session_state.index_soal = 0
        st.session_state.skor = 0
        st.session_state.selesai = False

    if st.session_state.selesai:
        st.balloons()
        st.success(f"🎉 {st.session_state.player_name}, skor akhir kamu: {st.session_state.skor} dari {len(st.session_state.random_soal)}")

        st.session_state.leaderboard.append(
            {"nama": st.session_state.player_name, "skor": st.session_state.skor}
        )

        st.markdown("---")
        st.markdown("### 🏆 Leaderboard Sementara")
        sorted_leaderboard = sorted(st.session_state.leaderboard, key=lambda x: x["skor"], reverse=True)
        for i, entry in enumerate(sorted_leaderboard[:5]):
            st.write(f"{i+1}. **{entry['nama']}** - {entry['skor']} poin")

        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔁 Ulang Game"):
                del st.session_state.random_soal
                del st.session_state.index_soal
                del st.session_state.skor
                del st.session_state.selesai
                st.rerun()
        with col2:
            st.button("📚 Kembali ke Materi", on_click=ke_slide, args=("materi",))
        with col3:
            st.button("🏠 Kembali ke Home", on_click=ke_slide, args=("menu",))

    else:
        soal = st.session_state.random_soal[st.session_state.index_soal]
        st.markdown(f"**Soal {st.session_state.index_soal + 1} dari {len(st.session_state.random_soal)}**")
        st.info(soal["pertanyaan"])
        jawaban = st.radio("Pilih jawaban kamu:", soal["opsi"], key="jawaban")

        if st.button("✅ Cek Jawaban"):
            if jawaban == soal["jawaban"]:
                st.success("Jawaban kamu BENAR! 👍")
                st.session_state.skor += 1
            else:
                st.error(f"Jawaban SALAH. Jawaban yang benar adalah **{soal['jawaban']}**.")

            st.session_state.index_soal += 1
            if st.session_state.index_soal >= len(st.session_state.random_soal):
                st.session_state.selesai = True

            st.rerun()

    st.markdown("---")
    st.button("⬅️ Kembali", on_click=ke_slide, args=("menu",))
