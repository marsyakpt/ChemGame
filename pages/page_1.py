import streamlit as st
import random

st.title("🧪 Kimia Organik")
st.header("🎮 Game Kimia Organik")

# Inisialisasi halaman
if "slide_organik" not in st.session_state:
    st.session_state.slide_organik = "game"

def ke_slide(nama):
    st.session_state.slide_organik = nama

# Soal lengkap
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
        "penjelasan": "Etanol adalah alkohol karena memiliki gugus -OH.",
        "skor": 4
    }
]

# Leaderboard init
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = []

# Nama pemain
if "player_name" not in st.session_state:
    st.session_state.player_name = ""

if not st.session_state.player_name:
    st.session_state.player_name = st.text_input("Masukkan nama kamu dulu ya! 👇")
    if st.session_state.player_name:
        st.rerun()
    else:
        st.stop()

# Init game session
if "random_soal" not in st.session_state:
    st.session_state.random_soal = random.sample(all_soal, 3)
    st.session_state.index_soal = 0
    st.session_state.skor = 0
    st.session_state.selesai = False

# Kalau selesai
if st.session_state.selesai:
    st.balloons()
    total_maks = sum(soal["skor"] for soal in st.session_state.random_soal)
    st.success(f"🎉 {st.session_state.player_name}, skor akhir kamu: {st.session_state.skor} dari total {total_maks} poin!")

    # Simpan ke leaderboard
    st.session_state.leaderboard.append(
        {"nama": st.session_state.player_name, "skor": st.session_state.skor}
    )

    st.markdown("### 🏆 Leaderboard Sementara")
    sorted_leaderboard = sorted(st.session_state.leaderboard, key=lambda x: x["skor"], reverse=True)
    for i, entry in enumerate(sorted_leaderboard[:5]):
        st.write(f"{i+1}. **{entry['nama']}** - {entry['skor']} poin")

    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔁 Ulang Game"):
            for k in ["random_soal", "index_soal", "skor", "selesai"]:
                del st.session_state[k]
            st.rerun()
    with col2:
        st.button("📚 Kembali ke Materi", on_click=ke_slide, args=("materi",))
    with col3:
        st.button("🏠 Kembali ke Home", on_click=ke_slide, args=("menu",))

# Kalau masih main
else:
    soal = st.session_state.random_soal[st.session_state.index_soal]
    abcd = ['A', 'B', 'C', 'D']
    pilihan_label = [f"{abcd[i]}. {opsi}" for i, opsi in enumerate(soal["opsi"])]

    st.markdown(f"**Soal {st.session_state.index_soal + 1} dari {len(st.session_state.random_soal)}**")
    st.info(soal["pertanyaan"])
    jawaban = st.radio("Pilih jawaban kamu:", pilihan_label, key=st.session_state.index_soal)

    if st.button("✅ Cek Jawaban"):
        jawaban_clean = jawaban.split(". ", 1)[1]  # ambil jawaban asli
        if jawaban_clean == soal["jawaban"]:
            st.success(f"Jawaban kamu BENAR! 👍 (+{soal['skor']} poin)")
            st.session_state.skor += soal["skor"]
        else:
            st.error(f"Jawaban SALAH. Jawaban yang benar adalah **{soal['jawaban']}**.")

        st.markdown(f"**Penjelasan:** {soal['penjelasan']}")
        st.session_state.index_soal += 1

        if st.session_state.index_soal >= len(st.session_state.random_soal):
            st.session_state.selesai = True

        st.rerun()

    st.markdown("---")
    st.button("⬅️ Kembali", on_click=ke_slide, args=("menu",))
