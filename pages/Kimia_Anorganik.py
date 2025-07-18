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
    
    Tenang aja, mau mulai dari mana pun, CHIQ tetap siap jadi partner belajarmu 😄✨
    """)

    st.button("📖 Materi", on_click=ke_slide, args=("materi",))
    st.button("🎮 Quis", on_click=ke_slide, args=("game",))


# --------------------- MATERI ---------------------
elif st.session_state.slide_anorganik == "materi":

    if "materi_topik_anorganik" not in st.session_state:
        st.session_state.materi_topik_anorganik = None

    if st.session_state.materi_topik_anorganik is None:
       
        st.markdown("""
        Bayangkan kamu sedang berdiri di depan meja lab—lampu neon menggantung tenang, bunsen menyala biru, dan tabung reaksi siap diisi.  
        Kamu panaskan sebatang logam... dan *cling!* api berubah jadi warna hijau kebiruan yang misterius.

        Tak lama, kamu teteskan larutan bening ke reagen.  
        Diam-diam, muncul kabut putih halus yang melayang pelan dalam gelas kimia.

        Ini bukan sulap. Ini **Kimia Anorganik**.  
        Dunia reaksi visual tempat ion-ion bereaksi, logam bicara lewat nyala, dan larutan berubah jadi petunjuk tersembunyi.

        CHIQ gak ngajak kamu hafalan.  
        CHIQ ngajak kamu kenali karakter senyawa lewat warna, perubahan, dan interaksi yang bisa kamu lihat langsung.

        ### Jadi, kamu mau mulai eksplorasi dari mana dulu?

        🔥 Api yang bicara melalui warna logam?  
        🧪 Larutan bening yang diam-diam punya reaksi mengejutkan?

        💬 *Di CHIQ, setiap reaksi adalah kisah—dan kamu adalah pembaca warna, pola, dan clue-nya.* ⚡✨
        """)

        st.markdown("### 📚 Pilih Topik Materimu 📚")
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
            Saat dipanaskan, elektron logam naik energi dan memancarkan cahaya khas saat kembali.

            | Logam           | Warna Nyala           |
            |----------------|------------------------|
            | Natrium (Na⁺)   | Kuning terang 🍋        |
            | Kalium (K⁺)     | Ungu muda 💜            |
            | Kalsium (Ca²⁺)  | Jingga bata 🔶          |
            | Tembaga (Cu²⁺)  | Hijau-biru 💚💙          |
            | Lithium (Li⁺)   | Merah 🔴                |
            | Barium (Ba²⁺)   | Hijau apel 🍏           |
            | Strontium (Sr²⁺)| Merah terang 🔥         |

            🔍 *Warna-warna ini bukan dekorasi, tapi tanda "bahasa cahaya" dari logam-logam laboratorium!*
            """)

        elif topik == "uji_kualitatif":
            st.markdown("## 🧪 Uji Kualitatif Senyawa Anorganik")
            st.markdown("""
            Ion-ion di larutan bisa bereaksi dengan pereagen tertentu, menghasilkan perubahan visual: endapan, warna, atau gas.

            | Reagen + Ion               | Hasil Reaksi                |
            |----------------------------|------------------------------|
            | Ag⁺ + Cl⁻                  | Endapan putih (AgCl) ⚪       |
            | Fe³⁺ + SCN⁻                | Larutan merah darah 🔴        |
            | Ba²⁺ + SO₄²⁻               | Endapan putih (BaSO₄) ⚪      |
            | Cu²⁺ + NH₃ (amonia)        | Larutan biru kompleks 💙     |
            | Pb²⁺ + I⁻                  | Endapan kuning (PbI₂) 💛     |

            🧪 *CHiQ bakal bantu kamu baca sinyal dari reaksi-reaksi ini seperti detektif kimia.* 🔬✨
            """)

        st.markdown("---")
        st.button("⬅️ Kembali", on_click=lambda: st.session_state.update({"materi_topik_anorganik": None}))
        st.button("🏠 Menu", on_click=ke_slide, args=("menu",))




# ---------------------- GAME ----------------------
elif st.session_state.slide_anorganik == "game":
    st.subheader("🎮 Game Kimia Anorganik")
    st.markdown("---")

    all_soal_anorganik = [
    {"pertanyaan": "Ion berikut yang menghasilkan endapan putih saat ditetesi AgNO₃ adalah...", "opsi": ["NO₃⁻", "Cl⁻", "SO₄²⁻", "CO₃²⁻"], "jawaban": "Cl⁻", "penjelasan": "Cl⁻ + Ag⁺ → AgCl, yaitu endapan putih yang nggak larut. Ini uji klasik untuk mengenali ion klorida! ⚪", "skor": 3},
    {"pertanyaan": "Ion yang menghasilkan warna nyala kuning terang adalah...", "opsi": ["K⁺", "Li⁺", "Na⁺", "Ba²⁺"], "jawaban": "Na⁺", "penjelasan": "Natrium dikenal dengan warna nyala kuning cerah yang khas banget. Bisa langsung kelihatan dari jauh 🔥🍋", "skor": 4},
    {"pertanyaan": "Endapan putih yang tidak larut dalam asam nitrat pekat terbentuk ketika ion SO₄²⁻ direaksikan dengan...", "opsi": ["AgNO₃", "BaCl₂", "NaOH", "HCl"], "jawaban": "BaCl₂", "penjelasan": "SO₄²⁻ + Ba²⁺ → BaSO₄, yaitu endapan putih yang tetap stabil meski disiram HNO₃ pekat. Super solid! ⚗️", "skor": 2},
    {"pertanyaan": "Reaksi cincin coklat pada uji anion menandakan keberadaan...", "opsi": ["Cl⁻", "PO₄³⁻", "NO₃⁻", "CO₃²⁻"], "jawaban": "NO₃⁻", "penjelasan": "Uji cincin coklat pakai FeSO₄ dan H₂SO₄. Kalau muncul ring coklat misterius, itu tanda ada NO₃⁻ 🔍🟤", "skor": 3},
    {"pertanyaan": "Kation berikut yang membentuk larutan biru tua dengan NH₄OH adalah...", "opsi": ["Fe³⁺", "Cu²⁺", "Pb²⁺", "Al³⁺"], "jawaban": "Cu²⁺", "penjelasan": "Cu²⁺ + NH₄OH → kompleks [Cu(NH₃)₄]²⁺ berwarna biru tua. Iconic warna larutan tembaga! 💙", "skor": 2},
    {"pertanyaan": "Ion yang memberikan endapan hitam dengan H₂S dalam suasana asam adalah...", "opsi": ["Na⁺", "Cu²⁺", "Ca²⁺", "K⁺"], "jawaban": "Cu²⁺", "penjelasan": "Cu²⁺ + H₂S → CuS, endapan hitam elegan. Ini reaksi khas logam golongan II! ⚫", "skor": 3},
    {"pertanyaan": "Warna nyala ungu pucat dihasilkan oleh ion...", "opsi": ["K⁺", "Li⁺", "Ca²⁺", "Ba²⁺"], "jawaban": "K⁺", "penjelasan": "Kalium ngasih warna ungu pucat yang halus. Kadang perlu filter kobalt biru biar makin jelas 💜", "skor": 4},
    {"pertanyaan": "Uji kualitatif digunakan untuk...", "opsi": ["Menentukan konsentrasi", "Menentukan berat molekul", "Mengidentifikasi jenis ion", "Menentukan titik didih"], "jawaban": "Mengidentifikasi jenis ion", "penjelasan": "Uji kualitatif itu tentang siapa yang ada di larutan, bukan seberapa banyak. Kayak kenalan duluan 🧪", "skor": 3},
    {"pertanyaan": "Ion yang diuji dengan HCl menghasilkan gas yang membuat air kapur menjadi keruh adalah...", "opsi": ["PO₄³⁻", "CO₃²⁻", "SO₄²⁻", "Cl⁻"], "jawaban": "CO₃²⁻", "penjelasan": "CO₃²⁻ + HCl → CO₂ ↑. Gas ini bikin air kapur keruh karena terbentuk CaCO₃. Uji visual banget! ☁️", "skor": 4},
    {"pertanyaan": "Ion Cl⁻ diuji dengan AgNO₃ menghasilkan endapan...", "opsi": ["Kuning", "Hitam", "Putih", "Coklat"], "jawaban": "Putih", "penjelasan": "Ag⁺ + Cl⁻ → AgCl, endapan putih yang bisa menghitam kalau kena cahaya. Reaksi cantik nan klasik ⚪🖤", "skor": 3},
    {"pertanyaan": "Uji nyala hijau kekuningan menunjukkan keberadaan ion...", "opsi": ["Ba²⁺", "Cu²⁺", "K⁺", "Ca²⁺"], "jawaban": "Ba²⁺", "penjelasan": "Barium memancarkan warna nyala hijau kekuningan yang khas, kayak daun kena sorotan matahari 🌿✨", "skor": 4},
    {"pertanyaan": "Kelompok ion yang tidak menghasilkan endapan dengan reagen umum adalah...", "opsi": ["Golongan I", "Golongan II", "Golongan V", "Golongan III"], "jawaban": "Golongan V", "penjelasan": "Golongan V (Na⁺, K⁺, NH₄⁺) itu humble banget di lab—nggak suka bikin endapan 😄💧", "skor": 3},
    {"pertanyaan": "Ion berikut yang termasuk golongan III kation adalah...", "opsi": ["Ag⁺", "Cu²⁺", "Fe³⁺", "Ba²⁺"], "jawaban": "Fe³⁺", "penjelasan": "Fe³⁺ tergolong golongan III karena membentuk hidroksida dalam suasana netral atau basa. Suka ngambek di larutan 😅", "skor": 4},
    {"pertanyaan": "Ion berikut yang tergolong dalam anion adalah...", "opsi": ["Fe³⁺", "K⁺", "Cl⁻", "NH₄⁺"], "jawaban": "Cl⁻", "penjelasan": "Cl⁻ punya muatan negatif, otomatis dia masuk tim anion. Simpel dan penting! ➖", "skor": 2},
    {"pertanyaan": "Warna nyala merah karmin dihasilkan oleh ion...", "opsi": ["Li⁺", "Ca²⁺", "Na⁺", "K⁺"], "jawaban": "Li⁺", "penjelasan": "Li⁺ nyala merah karmin-nya tajam banget—kayak nonton kembang api versi kimia ❤️🔥", "skor": 3},
    {"pertanyaan": "Reagen yang digunakan untuk menguji PO₄³⁻ adalah...", "opsi": ["HCl", "AgNO₃", "Amonium molibdat", "BaCl₂"], "jawaban": "Amonium molibdat", "penjelasan": "PO₄³⁻ + amonium molibdat → endapan kuning khas fosfat. Reaksinya mirip lukisan kimia ☀️🎨", "skor": 4},
    {"pertanyaan": "Gas CO₂ dari reaksi HCl dan ion karbonat terdeteksi dengan cara...", "opsi": ["Diuji nyala", "Uji bau", "Dilarutkan air kapur", "Disaring"], "jawaban": "Dilarutkan air kapur", "penjelasan": "CO₂ bikin air kapur keruh karena terbentuk CaCO₃. Visual banget, kayak larutan berubah jadi kabut 🫧", "skor": 3},
    {"pertanyaan": "Ion yang diuji dengan KSCN dan memberikan warna merah darah adalah...", "opsi": ["Cu²⁺", "Fe³⁺", "Al³⁺", "Zn²⁺"], "jawaban": "Fe³⁺", "penjelasan": "Fe³⁺ + SCN⁻ → kompleks merah darah Fe(SCN)₃. Dramatis dan jelas banget warnanya 🩸", "skor": 5},
    {"pertanyaan": "Salah satu reagen yang digunakan dalam pengelompokan kation adalah...", "opsi": ["H₂O", "NH₄OH", "NaCl", "H₂O₂"], "jawaban": "NH₄OH", "penjelasan": "NH₄OH bantu mengendapkan hidroksida logam sesuai golongannya. Jadi ‘pintu masuk’ klasifikasi kation 🧪", "skor": 3},
]

    if "leaderboard_anorganik" not in st.session_state:
        st.session_state.leaderboard_anorganik = []

    if "player_name_anorganik" not in st.session_state:
        st.session_state.player_name_anorganik = ""

    if not st.session_state.player_name_anorganik:
        name = st.text_input("Masukkan nama kamu dulu ya! 👇")
        col_a, col_b = st.columns([2, 1])
        with col_a:
            if name:
                st.session_state.player_name_anorganik = name
                st.rerun()
        with col_b:
            st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))
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
