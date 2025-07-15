import streamlit as st
import random

st.set_page_config(page_title="Kimia Organik", page_icon="🧪")

st.title("🔬 Kimia Organik")

# Navigasi halaman
if "slide_organik" not in st.session_state:
    st.session_state.slide_organik = "menu"

def ke_slide(nama):
    st.session_state.slide_organik = nama

# ==================== MENU AWAL ====================
if st.session_state.slide_organik == "menu":
    st.write("Silakan pilih:")
    st.button("📖 Materi", on_click=ke_slide, args=("materi",))
    st.button("🎮 Game", on_click=ke_slide, args=("game",))

# ==================== MATERI ====================
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

# ==================== GAME ====================
elif st.session_state.slide_organik == "game":
    st.markdown("## 🎮 Game Kimia Organik")
    st.markdown("---")

    all_soal = [...]  # <-- tetap gunakan list soalmu yang lengkap tadi

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
        import random
        st.session_state.random_soal = random.sample(all_soal, len(all_soal))
        st.session_state.index_soal = 0
        st.session_state.skor = 0
        st.session_state.selesai = False
        st.session_state.jawaban_cek = False

    if st.session_state.selesai:
        total_maks = sum(s["skor"] for s in st.session_state.random_soal)
        st.balloons()
        st.success(f"🎉 {st.session_state.player_name}, skor akhir kamu: {st.session_state.skor} dari {total_maks} poin!")
        st.session_state.leaderboard.append({"nama": st.session_state.player_name, "skor": st.session_state.skor})

        st.markdown("### 🏆 Leaderboard Sementara")
        for i, entry in enumerate(sorted(st.session_state.leaderboard, key=lambda x: x["skor"], reverse=True)[:5]):
            st.write(f"{i+1}. **{entry['nama']}** - {entry['skor']} poin")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔁 Ulang Game"):
                for k in ["random_soal", "index_soal", "skor", "selesai", "jawaban_cek"]:
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
        selected_option = st.radio("Pilih jawaban kamu:", list(opsi_dict.keys()), key=f"soal_{st.session_state.index_soal}")
        jawaban = opsi_dict[selected_option]

        if not st.session_state.jawaban_cek:
            if st.button("✅ Cek Jawaban"):
                st.session_state.jawaban_dipilih = jawaban
                st.session_state.jawaban_cek = True
                st.rerun()
        else:
            jawaban = st.session_state.jawaban_dipilih
            if jawaban == soal["jawaban"]:
                st.success(f"✅ Jawaban kamu BENAR! (+{soal['skor']} poin)")
                st.session_state.skor += soal["skor"]
            else:
                st.error(f"❌ Salah! Jawaban benar: **{soal['jawaban']}** (+0 poin)")
            st.info(f"💡 Penjelasan: {soal['penjelasan']}")

            if st.button("➡️ Lanjut Soal"):
                st.session_state.index_soal += 1
                st.session_state.jawaban_cek = False
                if st.session_state.index_soal >= len(st.session_state.random_soal):
                    st.session_state.selesai = True
                st.rerun()

        st.markdown("---")
        st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))

