import streamlit as st

st.title("🔬 Kimia Organik")

# Inisialisasi status halaman dalam 1 page
if "slide_organik" not in st.session_state:
    st.session_state.slide_organik = "menu"

# Fungsi navigasi dalam halaman
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
    st.markdown("""
    - Hidrokarbon: alkana, alkena, alkuna  
    - Gugus fungsi: -OH, -COOH, -NH2  
    - Reaksi: substitusi, adisi, eliminasi
    """)
    st.button("⬅️ Kembali", on_click=ke_slide, args=("menu",))

# Halaman Game
elif st.session_state.slide_organik == "game":
    st.markdown("## 🎮 Game Kimia Organik")
    st.markdown("---")

    # Daftar soal
    all_soal = [
        {"pertanyaan": "Apa gugus fungsi dari alkohol?", "opsi": ["-COOH", "-NH2", "-OH", "-CHO"], "jawaban": "-OH"},
        {"pertanyaan": "Gugus fungsi dari asam karboksilat adalah?", "opsi": ["-OH", "-COOH", "-NH2", "-C=O"], "jawaban": "-COOH"},
        {"pertanyaan": "Apa jenis reaksi alkena dengan HBr?", "opsi": ["Substitusi", "Eliminasi", "Adisi", "Polimerisasi"], "jawaban": "Adisi"},
        {"pertanyaan": "Alkana memiliki ikatan apa?", "opsi": ["Tunggal", "Rangkap dua", "Rangkap tiga", "Aromatik"], "jawaban": "Tunggal"},
        {"pertanyaan": "Etanol adalah contoh dari?", "opsi": ["Eter", "Aldehid", "Alkohol", "Alkana"], "jawaban": "Alkohol"},
    ]

    # Leaderboard init
    if "leaderboard" not in st.session_state:
        st.session_state.leaderboard = []

    # Nama pemain
    if "player_name" not in st.session_state or not st.session_state.player_name:
        nama = st.text_input("Masukkan nama kamu dulu ya! 👇")
        if nama:
            st.session_state.player_name = nama
            st.experimental_rerun()
        else:
            st.stop()

    # Init game session
    if "random_soal" not in st.session_state:
        import random
        st.session_state.random_soal = random.sample(all_soal, 3)
        st.session_state.index_soal = 0
        st.session_state.skor = 0
        st.session_state.selesai = False

    # Jika game selesai
    if st.session_state.selesai:
        st.balloons()
        st.success(f"🎉 {st.session_state.player_name}, skor akhir kamu: {st.session_state.skor} dari {len(st.session_state.random_soal)}")

        # Simpan ke leaderboard
        st.session_state.leaderboard.append(
            {"nama": st.session_state.player_name, "skor": st.session_state.skor}
        )

        st.markdown("---")
        st.markdown("### 🏆 Leaderboard Sementara")
        sorted_leaderboard = sorted(st.session_state.leaderboard, key=lambda x: x["skor"], reverse=True)
        for i, entry in enumerate(sorted_leaderboard[:5]):
            st.write(f"{i+1}. **{entry['nama']}** - {entry['skor']} poin")

        # Tombol navigasi
        st.markdown("---")
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

    # Kalau game belum selesai
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

            st.experimental_rerun()

    st.markdown("---")
    st.button("⬅️ Kembali", on_click=ke_slide, args=("menu",))
