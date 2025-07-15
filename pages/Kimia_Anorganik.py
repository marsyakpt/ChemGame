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
    st.markdown("### Cabang Kimia yang Bikin Warna Bicara dan Endapan Menjawab!")

    st.markdown("""
    Pernah lihat nyala api berwarna hijau di laboratorium? Atau larutan yang tiba-tiba mengendap saat ditetesin reagen?  
    Itu bukan sulap, tapi reaksi khas dari senyawa anorganik yang ada di sekeliling kita.

    Kimia Anorganik adalah cabang kimia yang mempelajari unsur dan senyawa non-karbon—mulai dari garam dapur, logam-logam, larutan asam basa, sampai ion-ion misterius yang biasa muncul di laboratorium.

    Misalnya, ion natrium bisa menghasilkan **nyala api kuning terang**, sedangkan ion tembaga menghadirkan warna **biru kehijauan yang khas**.  
    Reaksi antara ion klorida dan perak dapat membentuk **endapan putih mirip kabut halus**.

    Lewat penjelasan singkat dan kuis seru, CHIQ bantu kamu mengenali karakter senyawa anorganik dengan gaya belajar yang santai.
    """)

    st.markdown("### 🎯 Jadi kamu mau pilih yang mana nih?")
    st.markdown("""
    - 📖 *Baca Materi dulu* — pelajari reaksi dan penjelasannya dari awal  
    - 🎮 *Langsung ke Quis* — uji kemampuanmu dan lihat seberapa cepat kamu bisa mengenali senyawa!
    
    Tenang aja, mau mulai dari mana pun, CHiQ tetap siap jadi partner belajarmu 😄✨
    """)

    st.button("📖 Materi", on_click=ke_slide, args=("materi",))
    st.button("🎮 Quis", on_click=ke_slide, args=("game",))


# --------------------- MATERI ---------------------
elif st.session_state.slide_anorganik == "materi":

    if "materi_topik_anorganik" not in st.session_state:
        st.session_state.materi_topik_anorganik = None

    if st.session_state.materi_topik_anorganik is None:
        
        st.markdown("""
        Pernah lihat nyala api tiba-tiba berubah warna saat logam dipanaskan?  
        Atau larutan bening yang mendadak membentuk endapan putih mirip kabut kecil?

        Itu bukan efek visual—itu **reaksi nyata dari senyawa anorganik** yang ada di sekeliling kita!

        Di Kimia Anorganik, setiap warna, busa, dan perubahan larutan punya makna.  
        Logam bicara lewat api, dan ion bereaksi lewat transformasi dramatis dalam tabung uji.

        CHiQ bakal ajak kamu menyelami sisi paling visual dan logis dari dunia kimia.  
        Kamu gak akan disuruh hafal—tapi diajak mengamati, memahami, dan *decode* pola dari reaksi yang bisa kamu lihat langsung.

        ---
        ### 🎯 Jadi... kamu mau mulai dari mana dulu?

        Pikirkan:  
        Mau mengurai cahaya warna-warni dari nyala logam?  
        Atau membongkar misteri larutan yang tiba-tiba berubah saat ditetesin reagen?

        💬 *CHiQ percaya: belajar kimia itu bukan soal urutan, tapi soal rasa ingin tahu yang bikin reaksi dalam kepala ikut menyala.* ⚡✨
        """)

        st.markdown("### 📚 Pilih Topik Materimu:")
        st.button("🔥 Uji Nyala", on_click=lambda: st.session_state.update({"materi_topik_anorganik": "uji_nyala"}))
        st.button("🧪 Uji Kualitatif Senyawa", on_click=lambda: st.session_state.update({"materi_topik_anorganik": "uji_kualitatif"}))
        st.markdown("---")
        st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))

    else:
        topik = st.session_state.materi_topik_anorganik

        if topik == "uji_nyala":
            st.markdown("## 🔥 Uji Nyala")
            st.markdown("""
            Warna api bisa mengungkap identitas logam di balik senyawa!  
            Saat logam dipanaskan, elektronnya loncat energi dan memancarkan cahaya khas.

            | Logam           | Warna Nyala           |
            |----------------|------------------------|
            | Natrium (Na⁺)   | Kuning terang 🍋        |
            | Kalium (K⁺)     | Ungu muda 💜            |
            | Kalsium (Ca²⁺)  | Jingga bata 🔶          |
            | Tembaga (Cu²⁺)  | Hijau-biru 💚💙          |
            | Lithium (Li⁺)   | Merah 🔴                |
            | Barium (Ba²⁺)   | Hijau apel 🍏           |
            | Strontium (Sr²⁺)| Merah terang 🔥         |

            🔍 *Semua warna itu bukan sulap—tapi hasil transisi elektron yang kece!*
            """)

        elif topik == "uji_kualitatif":
            st.markdown("## 🧪 Uji Kualitatif Senyawa Anorganik")
            st.markdown("""
            Ion-ion di larutan bisa terdeteksi lewat perubahan fisik: munculnya endapan, perubahan warna, atau bahkan gas.

            | Reagen + Ion               | Hasil Reaksi                |
            |----------------------------|------------------------------|
            | Ag⁺ + Cl⁻                  | Endapan putih (AgCl) ⚪       |
            | Fe³⁺ + SCN⁻                | Warna merah darah 🔴         |
            | Ba²⁺ + SO₄²⁻               | Endapan putih (BaSO₄) ⚪      |
            | Cu²⁺ + NH₃ (amonia)        | Larutan biru kompleks 💙     |
            | Pb²⁺ + I⁻                  | Endapan kuning (PbI₂) 💛     |

            🔬 *Reaksi ini bukan cuma uji lab, tapi cara ion “menunjukkan identitasnya”!*
            """)

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
