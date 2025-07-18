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

        st.markdown("### 📚 Pilih Topik Materimu 📚")
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

            Pengujian Kualitatif:
            -	


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

            Pengujian Kualitatif:
            a. Uji Alkohol
                Uji Lucas: Alkohol + reagen Lucas (ZnCl₂ + HCl pekat)
                - Alkohol tersier  : keruh cepat
                - Alkohol sekunder : keruh lambat
                - Alkohol primer   : tidak keruh
            b. Uji Fenol
                Dengan FeCl₃       : Larutan berubah warna ungu, biru, atau hijau.



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

             **🔬 Pengujian Kualitatif:**
             
                - **a. Uji Aldehid**  
                    • Uji Tollens : Aldehida + AgNO₃ amoniakal → *cermin perak*  
                    • Uji Fehling : Aldehida + larutan Fehling → *endapan merah bata (Cu₂O)*
                - **b. Uji Keton**  
                    • Uji 2,4-DNP : menghasilkan *endapan kuning/oranye*



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

            Pengujian Kulitatif:
            - Dengan NaHCO₃: Menghasilkan gelembung CO₂.
            

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

            Pengujian Kualitatif:
            - Dengan NaOH                  : Menghasilkan gas amonia (NH₃) berbau khas.
            - Dengan benzensulfonilklorida : Menghasilkan cairan yang tidak larut
            

            🧠 *Fun fact:* Tanpa amina, kamu gak bisa mikir—karena dopamin = amina!
            """)

        elif topik == "lemak":
            st.markdown("## 🧴 Lemak & Minyak")
            st.markdown("""
            Lemak dan minyak adalah trigliserida—gabungan gliserol + 3 asam lemak.  
            Lemak padat (mentega), minyak cair (zaitun), tapi sama-sama organik.

            Reaksi saponifikasi? Yup, itu cara bikin sabun dari lemak + basa.

            Pengujian Kualitatif:
            - Dengan NaOH   : Menghasilkan busa
            - Dengan NaHCO3 : Menghasilkan busa


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

            Pengujian Kualitatif:
            - Uji Molisch  : alfa-naftol + H2SO4 -> Menghasilkan cincin ungu di batas
            - Uji Benedict : benedict + gula reduksi -> endapan merah bata
            - Uji Iodium   : iodin + amilum -> warna biru tua

            

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

            Pengujian Kualitatif:
            - Uji Biuret       : Protein + Cu2+ -> warna ungu
            - Uji Xantoproteat : Aromatik + asam nitrat -> warna kuning
            - Uji Millon       : Fenol + Millon -> warna merah


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
        {"pertanyaan": "Uji Lucas digunakan untuk menguji senyawa...", "opsi": ["Aldehid", "Alkohol", "Karbohidrat", "Protein"], "jawaban": "Alkohol", "penjelasan": "Uji Lucas membedakan alkohol primer, sekunder, dan tersier.", "skor": 3},
        {"pertanyaan": "Hasil uji Lucas yang cepat keruh menunjukkan alkohol...", "opsi": ["Primer", "Sekunder", "Tersier", "Tidak bereaksi"], "jawaban": "Tersier", "penjelasan": "Alkohol tersier langsung bereaksi dan membuat larutan keruh.", "skor": 3},
        {"pertanyaan": "Senyawa fenol diuji menggunakan reagen...", "opsi": ["Benedict", "Lucas", "FeCl₃", "NaHCO₃"], "jawaban": "FeCl₃", "penjelasan": "FeCl₃ bereaksi dengan fenol menghasilkan warna ungu/hijau.", "skor": 4},
        {"pertanyaan": "Cermin perak terbentuk pada uji...", "opsi": ["Benedict", "Tollens", "Molisch", "Biuret"], "jawaban": "Tollens", "penjelasan": "Uji Tollens menunjukkan aldehid melalui endapan perak.", "skor": 4},
        {"pertanyaan": "Uji Fehling positif akan menghasilkan...", "opsi": ["Endapan merah bata", "Larutan biru", "Gas CO₂", "Warna ungu"], "jawaban": "Endapan merah bata", "penjelasan": "Fehling positif untuk aldehid.", "skor": 3},
        {"pertanyaan": "Reagen 2,4-DNP digunakan untuk mendeteksi...", "opsi": ["Alkohol", "Ester", "Keton dan aldehid", "Amida"], "jawaban": "Keton dan aldehid", "penjelasan": "2,4-DNP menghasilkan endapan kuning/oranye.", "skor": 4},
        {"pertanyaan": "NaHCO₃ digunakan untuk menguji...", "opsi": ["Alkohol", "Asam karboksilat", "Fenol", "Amina"], "jawaban": "Asam karboksilat", "penjelasan": "Reaksi menghasilkan gas CO₂.", "skor": 2},
        {"pertanyaan": "Uji ester ditandai dengan munculnya...", "opsi": ["Warna ungu", "Gas", "Cermin perak", "Bau khas alkohol atau buah"], "jawaban": "Bau khas alkohol atau buah", "penjelasan": "Ester bereaksi menghasilkan aroma khas.", "skor": 3},
        {"pertanyaan": "Uji Molisch digunakan untuk mengetahui adanya...", "opsi": ["Lemak", "Karbohidrat", "Protein", "Alkohol"], "jawaban": "Karbohidrat", "penjelasan": "Molisch menghasilkan cincin ungu jika positif.", "skor": 2},
        {"pertanyaan": "Uji iodin pada amilum menunjukkan warna...", "opsi": ["Merah", "Kuning", "Biru tua", "Hijau"], "jawaban": "Biru tua", "penjelasan": "Reaksi amilum dengan iodin.", "skor": 3},
        {"pertanyaan": "Uji Benedict menghasilkan endapan merah bata pada...", "opsi": ["Karbohidrat reduksi", "Protein", "Lemak", "Asam"], "jawaban": "Karbohidrat reduksi", "penjelasan": "Contoh: glukosa → endapan merah bata.", "skor": 3},
        {"pertanyaan": "Uji Biuret untuk protein menghasilkan warna...", "opsi": ["Ungu", "Kuning", "Biru", "Putih"], "jawaban": "Ungu", "penjelasan": "Biuret positif menghasilkan warna ungu.", "skor": 3},
        {"pertanyaan": "Uji Millon menunjukkan warna merah pada senyawa yang mengandung...", "opsi": ["Fenol", "Ester", "Karbohidrat", "Aldehid"], "jawaban": "Fenol", "penjelasan": "Reaksi fenol dengan Millon → merah.", "skor": 3},
        {"pertanyaan": "Amonia (NH₃) dengan bau khas terbentuk saat menguji...", "opsi": ["Amida + NaOH", "Protein + Biuret", "Karbohidrat + H₂SO₄", "Alkohol + Lucas"], "jawaban": "Amida + NaOH", "penjelasan": "Amida bereaksi menghasilkan NH₃.", "skor": 2},
        {"pertanyaan": "Uji Xantoproteat positif menghasilkan warna...", "opsi": ["Ungu", "Biru", "Kuning", "Hijau"], "jawaban": "Kuning", "penjelasan": "Reaksi senyawa aromatik dengan HNO₃.", "skor": 4},
        {"pertanyaan": "Endapan kuning/oranye muncul saat uji...", "opsi": ["2,4-DNP", "Biuret", "Benedict", "FeCl₃"], "jawaban": "2,4-DNP", "penjelasan": "Reaksi dengan karbonil → endapan warna.", "skor": 3},
        {"pertanyaan": "Uji lemak menghasilkan...", "opsi": ["Gas", "Endapan merah", "Busa", "Warna ungu"], "jawaban": "Busa", "penjelasan": "Lemak + basa → sabun + busa.", "skor": 3},
        {"pertanyaan": "Warna ungu pada uji FeCl₃ menandakan adanya...", "opsi": ["Fenol", "Amina", "Amilum", "Karbohidrat"], "jawaban": "Fenol", "penjelasan": "Reaksi positif fenol.", "skor": 3},
        {"pertanyaan": "Uji iodin positif ditandai dengan...", "opsi": ["Cermin perak", "Warna biru tua", "Gelembung gas", "Busa"], "jawaban": "Warna biru tua", "penjelasan": "Amilum bereaksi dengan iodin.", "skor": 3},
        {"pertanyaan": "Karbohidrat reduksi memberikan reaksi positif dengan...", "opsi": ["Molisch dan Benedict", "Biuret dan Benedict", "Lucas dan FeCl₃", "Iodin dan Millon"], "jawaban": "Molisch dan Benedict", "penjelasan": "Molisch → karbohidrat umum, Benedict → gula reduksi.", "skor": 4},
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
