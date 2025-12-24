import streamlit as st

st.title("🍽 Catat Makanan (Bebas Total)")

if "meals" not in st.session_state:
    st.session_state.meals = []

nama_makanan = st.text_input("Tulis makanan apa pun yang kamu makan")
berat = st.number_input("Berat makanan (gram)", min_value=1)

# standar sederhana: rata-rata 2.5 kalori per gram
KALORI_PER_GRAM = 2.5

def hitung_gizi(gram):
    kalori = gram * KALORI_PER_GRAM
    protein = gram * 0.12
    karbo = gram * 0.2
    lemak = gram * 0.08
    serat = gram * 0.02
    gula = gram * 0.03

    return {
        "kalori": int(kalori),
        "protein": round(protein, 1),
        "karbo": round(karbo, 1),
        "lemak": round(lemak, 1),
        "serat": round(serat, 1),
        "gula": round(gula, 1),
    }

if st.button("➕ Tambahkan"):
    if nama_makanan.strip() == "":
        st.error("Nama makanan wajib diisi")
    else:
        gizi = hitung_gizi(berat)
        st.session_state.meals.append({
            "makanan": nama_makanan,
            "gram": berat,
            **gizi
        })
        st.success("Makanan berhasil dicatat")

if st.session_state.meals:
    st.subheader("📋 Daftar Makanan")
    for i, m in enumerate(st.session_state.meals, 1):
        st.write(
            f"{i}. {m['makanan']} ({m['gram']} g) → {m['kalori']} kkal"
        )

if st.button("Lanjut ke Ringkasan ➡"):
    st.session_state.page = 3
    st.rerun()
