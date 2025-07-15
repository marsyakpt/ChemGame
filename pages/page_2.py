import streamlit as st

st.title("⚗️ Kimia Anorganik")

if "slide_anorganik" not in st.session_state:
    st.session_state.slide_anorganik = "menu"

def ke_slide(nama):
    st.session_state.slide_anorganik = nama

# Menu utama
if st.session_state.slide_anorganik == "menu":
    st.write("Silakan pilih:")
    st.button("📖 Materi", on_click=ke_slide, args=("materi",))
    st.button("🎮 Game", on_click=ke_slide, args=("game",))

# Materi
elif st.session_state.slide_anorganik == "materi":
    st.subheader("📘 Materi Kimia Anorganik")
    st.markdown("""
    - Tabel periodik unsur  
    - Sifat logam dan non-logam  
    - Reaksi asam-basa  
    - Senyawa kompleks  
    - Oksidasi-reduksi
    """)
    st.button("⬅️ Kembali", on_click=ke_slide, args=("menu",))

# Game
elif st.session_state.slide_anorganik == "game":
    st.markdown("## 🎮 Game Kimia Anorganik")
    st.markdown("---")

    soal_anorganik = [
        {"pertanyaan": "Unsur golongan alkali tanah adalah?", "opsi": ["Na", "Mg", "Cl", "Fe"], "jawaban": "Mg"},
        {"pertanyaan": "Asam sulfat memiliki rumus kimia?", "opsi": ["HCl", "HNO₃", "H₂SO₄", "H₂CO₃"], "jawaban": "H₂SO₄"},
        {"pertanyaan": "Fe³⁺ + e⁻ → Fe²⁺ adalah proses?", "opsi": ["Oksidasi", "Reduksi", "Netralisasi", "Ionisasi"], "jawaban": "Reduksi"},
        {"pertanyaan": "Kompleks [Cu(NH₃)₄]²⁺ berwarna?", "opsi": ["Biru", "Merah", "Hijau", "Kuning"], "jawaban": "Biru"},
        {"pertanyaan": "Sifat logam yang paling umum adalah?", "opsi": ["Mudah larut", "Mudah terbakar", "Mengkilap", "Tidak reaktif"], "jawaban": "Mengkilap"},
    ]

    if "leaderboard_anorganik" not in st.session_state:
        st.session_state.leaderboard_anorganik = []

    if "player_name_anorganik" not in st.session_state or not st.session_state.player_name_anorganik:
        nama = st.text_input("Masukkan nama kamu dulu ya! 👇", key="input_nama_anorganik")
        if nama:
            st.session_state.player_name_anorganik = nama
            st.rerun()
        else:
            st.stop()

    if "soal_acak_anorganik" not in st.session_state:
        import random
        st.session_state.soal_acak_anorganik = random.sample(soal_anorganik, 3)
        st.session_state.index_anorganik = 0
        st.session_state.skor_anorganik = 0
        st.session_state.selesai_anorganik = False

    if st.session_state.selesai_anorganik:
        st.balloons()
        st.success(f"🎉 {st.session_state.player_name_anorganik}, skor akhir kamu: {st.session_state.skor_anorganik} dari {len(st.session_state.soal_acak_anorganik)}")

        st.session_state.leaderboard_anorganik.append(
            {"nama": st.session_state.player_name_anorganik, "skor": st.session_state.skor_anorganik}
        )

        st.markdown("### 🏆 Leaderboard Sementara")
        leaderboard = sorted(st.session_state.leaderboard_anorganik, key=lambda x: x["skor"], reverse=True)
        for i, entry in enumerate(leaderboard[:5]):
            st.write(f"{i+1}. **{entry['nama']}** - {entry['skor']} poin")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔁 Ulang Game"):
                del st.session_state.soal_acak_anorganik
                del st.session_state.index_anorganik
                del st.session_state.skor_anorganik
                del st.session_state.selesai_anorganik
                st.rerun()
        with col2:
            st.button("📚 Kembali ke Materi", on_click=ke_slide, args=("materi",))
        with col3:
            st.button("🏠 Kembali ke Home", on_click=ke_slide, args=("menu",))

    else:
        soal = st.session_state.soal_acak_anorganik[st.session_state.index_anorganik]
        st.markdown(f"**Soal {st.session_state.index_anorganik + 1} dari {len(st.session_state.soal_acak_anorganik)}**")
        st.info(soal["pertanyaan"])
        jawaban = st.radio("Pilih jawaban kamu:", soal["opsi"], key=f"jawaban_anorganik_{st.session_state.index_anorganik}")

        if st.button("✅ Cek Jawaban"):
            if jawaban == soal["jawaban"]:
                st.success("Jawaban kamu BENAR! 👍")
                st.session_state.skor_anorganik += 1
            else:
                st.error(f"Jawaban SALAH. Jawaban yang benar adalah **{soal['jawaban']}**.")

            st.session_state.index_anorganik += 1
            if st.session_state.index_anorganik >= len(st.session_state.soal_acak_anorganik):
                st.session_state.selesai_anorganik = True

            st.rerun()

    st.markdown("---")
    st.button("⬅️ Kembali", on_click=ke_slide, args=("menu",))
