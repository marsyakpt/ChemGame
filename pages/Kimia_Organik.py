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
    st.markdown("### 🧪 Cabang Kimia yang Bikin Hidup Lebih… Karbon!")

    st.markdown("""
    Pernah mikir kenapa parfum bisa wangi? Atau kenapa mie instan butuh minyak?  
    Jawabannya: semua itu senyawa organik!

   Kimia Organik adalah cabang kimia yang mempelajari senyawa berbasis karbon.  
    Mulai dari hidrokarbon sederhana, alkohol beraroma khas, ester pewangi, hingga molekul besar seperti karbohidrat dan protein yang jadi pondasi tubuh kita.

   Di CHiQ, kamu akan diajak mengenali karakter senyawa ini lewat penjelasan ringan dan kuis seru—gak bikin pusing, tapi bikin penasaran!
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
    st.markdown("""
    Bayangin kamu lagi megang parfum favorit, nyemil donat, atau cuci tangan pakai sabun wangi...  
    Tanpa kamu sadari, kamu sedang berinteraksi langsung dengan dunia **Kimia Organik**!

    Dari molekul kecil seperti **hidrokarbon** yang bikin bahan bakar menyala,  
    sampai struktur kompleks seperti **protein** yang menyusun tubuhmu—semuanya berbasis **karbon**, dan semuanya punya cerita.

    Di halaman ini, CHiQ bakal ajak kamu eksplor berbagai jenis senyawa organik:  
    ada yang aromanya khas, ada yang sifatnya unik, dan ada yang jadi bagian penting dalam hidup kita sehari-hari.

    Kamu bebas pilih jalur eksplorasimu.  
    Mau mulai dari yang simpel kayak hidrokarbon, atau langsung loncat ke senyawa yang bikin mie instan gurih?

    🎓 Belajar di CHiQ gak harus urut—pilih topik yang paling bikin kamu kepo duluan, dan biarkan rasa penasaranmu nuntun ke insight kimia yang gak terduga! ⚗️✨
    """)

    if "materi_topik_organik" not in st.session_state:
        st.session_state.materi_topik_organik = None

    if st.session_state.materi_topik_organik is None:
        st.markdown("### 📚 Pilih Topik Materimu:")
        st.button("🔥 Hidrokarbon", on_click=lambda: st.session_state.update({"materi_topik_organik": "hidrokarbon"}))
        st.button("🍷 Alkohol, Fenol, Eter", on_click=lambda: st.session_state.update({"materi_topik_organik": "alkohol"}))
        st.button("🍋 Aldehid & Keton", on_click=lambda: st.session_state.update({"materi_topik_organik": "aldehid_keton"}))
        st.button("🧂 Asam Karboksilat & Derivat", on_click=lambda: st.session_state.update({"materi_topik_organik": "karboksilat"}))
        st.button("🌿 Amina & Derivat", on_click=lambda: st.session_state.update({"materi_topik_organik": "amina"}))
        st.button("🧴 Lemak & Minyak", on_click=lambda: st.session_state.update({"materi_topik_organik": "lemak"}))
        st.button("🍞 Karbohidrat", on_click=lambda: st.session_state.update({"materi_topik_organik": "karbohidrat"}))
        st.button("🥚 Protein", on_click=lambda: st.session_state.update({"materi_topik_organik": "protein"}))
        st.markdown("---")
        st.button("⬅️ Kembali ke Menu", on_click=ke_slide, args=("menu",))
    else:
        topik = st.session_state.materi_topik_organik
        if topik == "hidrokarbon":
            st.markdown("## 🔥 Hidrokarbon")
            st.markdown("- Senyawa karbon & hidrogen\n- Jenis: alkan, alken, alkuna")
        elif topik == "alkohol":
            st.markdown("## 🍷 Alkohol, Fenol, Eter")
            st.markdown("- Gugus -OH & sifat larut air\n- Reaksi oksidasi & aroma senyawa")
        elif topik == "aldehid_keton":
            st.markdown("## 🍋 Aldehid & Keton")
            st.markdown("- Gugus karbonil\n- Contoh senyawa: formaldehid, aseton")
        elif topik == "karboksilat":
            st.markdown("## 🧂 Asam Karboksilat & Derivatnya")
            st.markdown("- Gugus -COOH\n- Derivat: ester, anhidrida, amida")
        elif topik == "amina":
            st.markdown("## 🌿 Amina & Derivatnya")
            st.markdown("- Gugus -NH₂\n- Sifat basa & reaktivitas")
        elif topik == "lemak":
            st.markdown("## 🧴 Lemak & Minyak")
            st.markdown("- Trigliserida\n- Reaksi saponifikasi & peran dalam tubuh")
        elif topik == "karbohidrat":
            st.markdown("## 🍞 Karbohidrat")
            st.markdown("- Monosakarida, disakarida, polisakarida\n- Fungsi sebagai sumber energi")
        elif topik == "protein":
            st.markdown("## 🥚 Protein")
            st.markdown("- Asam amino & struktur 3D\n- Peran enzim & fungsi biologis")

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
        if name:
            st.session_state.player_name = name
            st.rerun()
        else:
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
