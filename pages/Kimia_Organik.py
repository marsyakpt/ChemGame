import streamlit as st
import random

st.set_page_config(page_title="Kimia Organik", page_icon="🧪")
st.title("🔬 Kimia Organik")

# Navigasi
if "slide_organik" not in st.session_state:
    st.session_state.slide_organik = "menu"

def ke_slide(nama):
    st.session_state.slide_organik = nama

# ---------------------- MENU ----------------------
if st.session_state.slide_organik == "menu":
    st.markdown("### Cabang Kimia yang Bikin Hidup Lebih… Karbon!")

    st.markdown("""
    Pernah mikir kenapa parfum bisa wangi? Atau kenapa mie instan butuh minyak?  
    Jawabannya: semua itu senyawa organik!

   Kimia Organik adalah cabang kimia yang mempelajari senyawa berbasis karbon.  
    Mulai dari hidrokarbon sederhana, alkohol beraroma khas, ester pewangi, hingga molekul besar seperti karbohidrat dan protein yang jadi pondasi tubuh kita.

   Di CHIQ, kamu akan diajak mengenali karakter senyawa ini lewat penjelasan ringan dan kuis seru—gak bikin pusing, tapi bikin penasaran!
    """)

    st.markdown("### 💡 Contoh Reaksi Organik:")
    st.markdown("""
    - Alkohol memiliki gugus -OH yang bikin larut air dan jadi bahan antiseptik  
    - Senyawa ester punya aroma manis, cocok banget dipakai buat parfum dan pewangi  
    - Karbohidrat & protein adalah molekul kompleks yang jadi sumber energi & pembentuk sel tubuh

   Setiap senyawa punya cerita unik, dan CHiQ bantu kamu mengenalinya dengan pendekatan yang fun dan masuk akal 😄
    """)

    st.markdown("### 🎯 Jadi kamu mau mulai dari mana nih?")
    st.markdown("""
    - 📖 Pelajari dulu semua jenis senyawa dan karakteristiknya  
    - 🎮 Atau langsung uji insting karbon-mu di kuis organik yang gak bikin ngantuk!

   🧠 CHiQ percaya: belajar itu bukan soal cepat atau lambat—tapi soal nyantol di kepala dengan gaya yang relatable ✨
    """)

    st.button("📖 Materi", on_click=ke_slide, args=("materi",))
    st.button("🎮 Kuis", on_click=ke_slide, args=("game",))


# --------------------- MATERI ---------------------
elif st.session_state.slide_organik == "materi":

    if "materi_topik_organik" not in st.session_state:
        st.session_state.materi_topik_organik = None

    if st.session_state.materi_topik_organik is None:
        st.markdown("""
        Bayangin kamu lagi megang parfum favorit, nyemil donat, atau cuci tangan pakai sabun wangi...  
        Tanpa kamu sadari, kamu sedang berinteraksi langsung dengan dunia **Kimia Organik**!

        Dari molekul kecil seperti **hidrokarbon** yang bikin bahan bakar menyala,  
        sampai struktur kompleks seperti **protein** yang menyusun tubuhmu—semuanya berbasis **karbon**, dan semuanya punya cerita.

        Di halaman ini, CHIQ bakal ajak kamu eksplor berbagai jenis senyawa organik:  
        ada yang aromanya khas, ada yang sifatnya unik, dan ada yang jadi bagian penting dalam hidup kita sehari-hari.

        Kamu bebas pilih jalur eksplorasimu.  
        Mau mulai dari yang simpel kayak hidrokarbon, atau langsung loncat ke senyawa yang bikin mie instan gurih?

        🎓 *Belajar di CHiQ gak harus urut—pilih topik yang paling bikin kamu kepo duluan, dan biarkan rasa penasaranmu nuntun ke insight kimia yang gak terduga!* ⚗️✨
        """)

        st.markdown("### 📚 Pilih Topik Materimu:")
        st.button("🔥 Hidrokarbon", on_click=lambda: st.session_state.update({"materi_topik_organik": "hidrokarbon"}))
        st.button("🍷 Alkohol, Fenol, Eter", on_click=lambda: st.session_state.update({"materi_topik_organik": "alkohol"}))
        st.button("🍋 Aldehid & Keton", on_click=lambda: st.session_state.update({"materi_topik_organik": "aldehid_keton"}))
        st.button("🧂 Asam Karboksilat", on_click=lambda: st.session_state.update({"materi_topik_organik": "karboksilat"}))
        st.button("🌿 Amina", on_click=lambda: st.session_state.update({"materi_topik_organik": "amina"}))
        st.button("🧴 Lemak & Minyak", on_click=lambda: st.session_state.update({"materi_topik_organik": "lemak"}))
        st.button("🍞 Karbohidrat", on_click=lambda: st.session_state.update({"materi_topik_organik": "karbohidrat"}))
        st.button("🥚 Protein", on_click=lambda: st.session_state.update({"materi_topik_organik": "protein"}))
        st.markdown("---")
        st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))

    else:
        topik = st.session_state.materi_topik_organik

        if topik == "hidrokarbon":
            st.markdown("## 🔥 Hidrokarbon")
            st.markdown("""
            Coba pikirkan bensin, gas LPG, atau lilin yang kamu nyalakan saat mati lampu—semuanya menyala karena senyawa hidrokarbon!  
            Hidrokarbon cuma terdiri dari karbon dan hidrogen, tapi mereka punya energi besar yang menggerakkan dunia.

            Jenisnya:
            - Alkana (ikatan tunggal): metana, etana  
            - Alkena (rangkap dua): etena, propena  
            - Alkuna (rangkap tiga): etuna, butuna  
            - Aromatik (cincin benzena): biasa di pewangi

            🧠 *Fun fact:* Benzena itu aromatik yang literally... punya aroma 😆
            """)

        elif topik == "alkohol":
            st.markdown("## 🍷 Alkohol, Fenol, Eter")
            st.markdown("""
            Alkohol punya gugus -OH yang bikin larut air dan reaktif. Fenol lebih asam dan sering dipakai di antiseptik.  
            Eter? Senyawa dengan dua gugus alkil di kiri-kanan oksigen—stabil dan sering jadi pelarut.

            Contoh:
            - Etanol (hand sanitizer)  
            - Fenol (desinfektan)  
            - Dietil eter (anestesi)

            🧠 *Fun fact:* Alkohol = bahan parfum yang aromanya nempel di baju berjam-jam!
            """)

        elif topik == "aldehid_keton":
            st.markdown("## 🍋 Aldehid & Keton")
            st.markdown("""
            Gugus karbonil (C=O) jadi ciri khas mereka: aldehid di ujung, keton di tengah.  
            Dipakai di parfum, pelarut, dan reaksi metabolik.

            Contoh:
            - Formaldehid (pengawet)  
            - Aseton (penghapus kuteks!)

            🧠 *Fun fact:* Aroma permen sintetis bisa berasal dari senyawa keton 🍬
            """)

        elif topik == "karboksilat":
            st.markdown("## 🧂 Asam Karboksilat & Derivatnya")
            st.markdown("""
            Gugus -COOH bikin mereka asam.  
            Turunannya bisa berupa ester (wangi), amida (protein), atau anhidrida (reaktif).

            Contoh:
            - Asam asetat (cuka)  
            - Ester stroberi (hasil dari alkohol + asam!)

            🧠 *Fun fact:* Sabun wangi itu hasil reaksi ester dari bahan kimia ini 😄
            """)

        elif topik == "amina":
            st.markdown("## 🌿 Amina & Derivatnya")
            st.markdown("""
            Gugus -NH₂ bikin mereka bersifat basa.  
            Amina terlibat dalam pewarna, protein, neurotransmitter, dan obat-obatan!

            Contoh:
            - Metilamina (amina primer)  
            - Dopamin (neurotransmitter berbasis amina)

            🧠 *Fun fact:* Tanpa amina, kamu gak bisa mikir—karena dopamin = amina!
            """)

        elif topik == "lemak":
            st.markdown("## 🧴 Lemak & Minyak")
            st.markdown("""
            Lemak dan minyak adalah trigliserida—gabungan gliserol + 3 asam lemak.  
            Lemak padat (mentega), minyak cair (zaitun), tapi sama-sama organik.

            Reaksi saponifikasi? Yup, itu cara bikin sabun dari lemak + basa.

            🧠 *Fun fact:* Sabun mandi kamu berasal dari reaksi lemak yang disulap jadi ester bersih 🧼
            """)

        elif topik == "karbohidrat":
            st.markdown("## 🍞 Karbohidrat")
            st.markdown("""
            Karbohidrat adalah senyawa organik yang jadi sumber energi utama.  
            Terdiri dari gula sederhana (glukosa) hingga rantai panjang (selulosa).

            Contoh:
            - Glukosa (gula darah)  
            - Sukrosa (gula dapur)  
            - Selulosa (dinding tumbuhan)

            🧠 *Fun fact:* Gula bisa karamelisasi dan munculin aroma roti yang super bikin lapar 😋
            """)

        elif topik == "protein":
            st.markdown("## 🥚 Protein")
            st.markdown("""
            Protein adalah polimer asam amino yang bikin enzim, otot, hormon, dan struktur tubuh.

            Contoh:
            - Hemoglobin: angkut oksigen  
            - Kolagen: bikin kulit elastis  
            - Insulin: regulasi gula

            🧠 *Fun fact:* Telur yang berubah putih saat dimasak adalah protein yang berubah bentuk (denaturasi)!
            """)

        st.markdown("---")
        st.button("⬅️ Kembali", on_click=lambda: st.session_state.update({"materi_topik_organik": None}))
        st.button("🏠 Menu", on_click=ke_slide, args=("menu",))


# ---------------------- GAME ----------------------
elif st.session_state.slide_organik == "game":
    st.subheader("🎮 Game Kimia Organik")
    st.markdown("---")

    all_soal = [
        {"pertanyaan": "Apa gugus fungsi dari alkohol?", "opsi": ["-COOH", "-NH2", "-OH", "-CHO"], "jawaban": "-OH", "penjelasan": "Alkohol memiliki gugus -OH.", "skor": 3},
        {"pertanyaan": "Gugus fungsi dari asam karboksilat adalah?", "opsi": ["-OH", "-COOH", "-NH2", "-C=O"], "jawaban": "-COOH", "penjelasan": "Asam karboksilat memiliki -COOH.", "skor": 5},
        {"pertanyaan": "Apa jenis reaksi alkena dengan HBr?", "opsi": ["Substitusi", "Eliminasi", "Adisi", "Polimerisasi"], "jawaban": "Adisi", "penjelasan": "Alkena + HBr adalah reaksi adisi.", "skor": 2},
        {"pertanyaan": "Alkana memiliki ikatan apa?", "opsi": ["Tunggal", "Rangkap dua", "Rangkap tiga", "Aromatik"], "jawaban": "Tunggal", "penjelasan": "Alkana hanya punya ikatan tunggal.", "skor": 3},
        {"pertanyaan": "Etanol termasuk?", "opsi": ["Eter", "Aldehid", "Alkohol", "Alkana"], "jawaban": "Alkohol", "penjelasan": "Etanol punya gugus -OH.", "skor": 4},
        {"pertanyaan": "Apa nama CH₃COOH?", "opsi": ["Asam asetat", "Etanol", "Metanol", "Asam format"], "jawaban": "Asam asetat", "penjelasan": "CH₃COOH = Asam asetat", "skor": 3},
        {"pertanyaan": "Benzena termasuk?", "opsi": ["Alkana", "Alkena", "Aromatik", "Aldehid"], "jawaban": "Aromatik", "penjelasan": "Benzena bersifat aromatik.", "skor": 4},
    ]

    if "leaderboard" not in st.session_state:
        st.session_state.leaderboard = []

    if "player_name" not in st.session_state:
        st.session_state.player_name = ""

    if not st.session_state.player_name:
        name = st.text_input("Masukkan nama kamu dulu ya! 👇")
        col_a, col_b = st.columns([2, 1])
        with col_a:
            if name:
                st.session_state.player_name = name
                st.rerun()
        with col_b:
            st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))
        st.stop()


    if "random_soal" not in st.session_state:
        st.session_state.random_soal = random.sample(all_soal, len(all_soal))
        st.session_state.index_soal = 0
        st.session_state.skor = 0
        st.session_state.jawaban_dipilih = None
        st.session_state.tampilkan_penjelasan = False
        st.session_state.selesai = False

    if st.session_state.selesai:
        total_maks = sum(s["skor"] for s in st.session_state.random_soal)
        st.balloons()
        st.success(f"🎉 {st.session_state.player_name}, skor kamu: {st.session_state.skor}/{total_maks} poin")

        st.session_state.leaderboard.append(
            {"nama": st.session_state.player_name, "skor": st.session_state.skor}
        )

        st.markdown("### 🏆 Leaderboard Sementara")
        for i, entry in enumerate(sorted(st.session_state.leaderboard, key=lambda x: x["skor"], reverse=True)[:5]):
            st.write(f"{i+1}. **{entry['nama']}** - {entry['skor']} poin")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔁 Ulang Game"):
                for key in ["random_soal", "index_soal", "skor", "jawaban_dipilih", "tampilkan_penjelasan", "selesai"]:
                    del st.session_state[key]
                st.rerun()
        with col2:
            st.button("📚 Kembali ke Materi", on_click=ke_slide, args=("materi",))
        with col3:
            st.button("🏠 Menu", on_click=ke_slide, args=("menu",))

    else:
        soal = st.session_state.random_soal[st.session_state.index_soal]
        st.markdown(f"**Soal {st.session_state.index_soal + 1} dari {len(st.session_state.random_soal)}**")
        st.info(soal["pertanyaan"])

        opsi_label = ['A', 'B', 'C', 'D']
        opsi_dict = {f"{label}. {text}": text for label, text in zip(opsi_label, soal["opsi"])}

        jawaban_dipilih = st.radio("Pilih jawaban:", list(opsi_dict.keys()), key=f"radio_{st.session_state.index_soal}")
        jawaban = opsi_dict[jawaban_dipilih]

        if st.button("✅ Cek Jawaban"):
            st.session_state.tampilkan_penjelasan = True
            st.session_state.jawaban_dipilih = jawaban
            if jawaban == soal["jawaban"]:
                st.session_state.skor += soal["skor"]
            st.rerun()

        if st.session_state.tampilkan_penjelasan:
            if st.session_state.jawaban_dipilih == soal["jawaban"]:
                st.success(f"✅ Jawaban kamu BENAR! (+{soal['skor']} poin)")
            else:
                st.error(f"❌ Salah. Jawaban benar: **{soal['jawaban']}**")

            st.info(f"💡 Penjelasan: {soal['penjelasan']}")

            if st.button("➡️ Lanjut Soal"):
                st.session_state.index_soal += 1
                st.session_state.jawaban_dipilih = None
                st.session_state.tampilkan_penjelasan = False
                if st.session_state.index_soal >= len(st.session_state.random_soal):
                    st.session_state.selesai = True
                st.rerun()

    st.markdown("---")
    st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))
