import streamlit as st
import pandas as pd
import altair as alt

# ================== KONFIGURASI ==================
st.set_page_config(
    page_title="Smart Calorie & Nutrition Tracker",
    page_icon="🍎",
    layout="centered"
)

# ================== SESSION STATE ==================
if "page" not in st.session_state:
    st.session_state.page = 1

if "user" not in st.session_state:
    st.session_state.user = {}

if "meals" not in st.session_state:
    st.session_state.meals = []

# ================== PAGE 1 ==================
def page_data_pengguna():
    st.title("👤 Data Pengguna")

    nama = st.text_input("Nama")
    umur = st.number_input("Umur", min_value=0, max_value=100)
    jk = st.selectbox("Jenis Kelamin", ["Pilih", "Laki-laki", "Perempuan"])

    if st.button("Simpan & Lanjut ➡"):
        if nama == "" or jk == "Pilih":
            st.error("Semua data wajib diisi")
        else:
            st.session_state.user = {
                "nama": nama,
                "umur": umur,
                "jk": jk
            }
            st.session_state.page = 2
            st.rerun()

# ================== PAGE 2 ==================
def page_input_makanan():
    st.title("🍽 Input Makanan")

    makanan = st.text_input("Nama makanan (bebas)")
    kalori = st.number_input("Total kalori (kkal)", min_value=0)

    if st.button("Tambah Makanan"):
        if makanan == "" or kalori == 0:
            st.error("Nama makanan dan kalori wajib diisi")
        else:
            protein = (kalori * 0.20) / 4
            karbo = (kalori * 0.50) / 4
            lemak = (kalori * 0.30) / 9
            serat = karbo * 0.10
            gula = karbo * 0.20

            st.session_state.meals.append({
                "makanan": makanan,
                "kalori": kalori,
                "protein": protein,
                "karbo": karbo,
                "lemak": lemak,
                "serat": serat,
                "gula": gula
            })

            st.success(f"{makanan} berhasil ditambahkan")

    if st.session_state.meals:
        st.subheader("📋 Makanan Dikonsumsi")
        for i, m in enumerate(st.session_state.meals, 1):
            st.write(f"{i}. {m['makanan']} - {m['kalori']} kkal")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Kembali"):
            st.session_state.page = 1
            st.rerun()
    with col2:
        if st.button("Lanjut ➡"):
            st.session_state.page = 3
            st.rerun()

# ================== PAGE 3 ==================
def page_total_kalori():
    st.title("🔥 Total Kalori Harian")

    total_kalori = sum(m["kalori"] for m in st.session_state.meals)
    st.metric("Total Kalori", f"{total_kalori:.0f} kkal")

    if st.button("Lihat Analisis Gizi ➡"):
        st.session_state.page = 4
        st.rerun()

# ================== PAGE 4 ==================
def page_analisis_gizi():
    st.title("📊 Analisis Gizi & Rekomendasi")

    total = {
        "kalori": 0,
        "protein": 0,
        "karbo": 0,
        "lemak": 0,
        "serat": 0,
        "gula": 0
    }

    for m in st.session_state.meals:
        for k in total:
            total[k] += m[k]

    st.subheader("🔎 Total Asupan")
    st.write(f"🔥 Kalori: {total['kalori']:.0f} kkal")
    st.write(f"🥩 Protein: {total['protein']:.1f} g")
    st.write(f"🍚 Karbohidrat: {total['karbo']:.1f} g")
    st.write(f"🥑 Lemak: {total['lemak']:.1f} g")
    st.write(f"🥦 Serat: {total['serat']:.1f} g")
    st.write(f"🍬 Gula: {total['gula']:.1f} g")

    st.subheader("📌 Evaluasi & Rekomendasi")

    if total["protein"] < 50:
        st.warning("Protein masih kurang")
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Roast_chicken.jpg")

    if total["karbo"] < 225:
        st.warning("Karbohidrat masih kurang")
        st.image("https://upload.wikimedia.org/wikipedia/commons/8/8f/Oatmeal.jpg")

    if total["lemak"] < 60:
        st.warning("Lemak sehat masih kurang")
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/c4/Avocado_Hass.jpg")

    if total["serat"] < 25:
        st.warning("Serat masih kurang")
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/03/Broccoli_and_cross_section_edit.jpg")

    if total["gula"] < 25:
        st.warning("Gula alami masih kurang")
        st.image("https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg")

    # ================== APRESIASI ==================
    if (
        total["protein"] >= 50 and
        total["karbo"] >= 225 and
        total["lemak"] >= 60 and
        total["serat"] >= 25 and
        total["gula"] >= 25
    ):
        st.success("🎉 Luar biasa! Asupan gizi harian kamu hari ini sudah TERPENUHI dengan baik!")
        st.balloons()
        st.markdown("""
        💚 **Kerja bagus!**  
        Kamu sudah menjaga keseimbangan nutrisi dengan sangat baik hari ini.  
        Pertahankan pola makan sehat ini untuk energi, fokus, dan kesehatan jangka panjang 🚀🥗
        """)

    st.subheader("🌈 Grafik Asupan Gizi")

    df = pd.DataFrame({
        "Nutrisi": ["Protein", "Karbohidrat", "Lemak", "Serat", "Gula"],
        "Jumlah": [
            total["protein"],
            total["karbo"],
            total["lemak"],
            total["serat"],
            total["gula"]
        ]
    })

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Nutrisi", sort=None),
        y="Jumlah",
        color=alt.Color(
            "Nutrisi",
            scale=alt.Scale(
                range=["#FF6B6B", "#4D96FF", "#6BCB77", "#FFD93D", "#C77DFF"]
            )
        ),
        tooltip=["Nutrisi", "Jumlah"]
    ).properties(height=350)

    st.altair_chart(chart, use_container_width=True)

    if st.button("🔄 Mulai Ulang"):
        st.session_state.page = 1
        st.session_state.user = {}
        st.session_state.meals = []
        st.rerun()

# ================== ROUTER ==================
if st.session_state.page == 1:
    page_data_pengguna()
elif st.session_state.page == 2:
    page_input_makanan()
elif st.session_state.page == 3:
    page_total_kalori()
elif st.session_state.page == 4:
    page_analisis_gizi()
