def page_analisis_gizi():
    st.title("📊 Analisis Gizi Lengkap")

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

    st.subheader("🔎 Total Asupan Harian")
    st.write(f"🔥 Kalori: {total['kalori']} kkal")
    st.write(f"🥩 Protein: {total['protein']} g")
    st.write(f"🍚 Karbohidrat: {total['karbo']} g")
    st.write(f"🥑 Lemak: {total['lemak']} g")
    st.write(f"🥦 Serat: {total['serat']} g")
    st.write(f"🍬 Gula: {total['gula']} g")

    st.subheader("📌 Status Gizi")
    if total["kalori"] < 1800:
        st.warning("Asupan kalori rendah")
    elif total["kalori"] <= 2200:
        st.success("Asupan kalori normal")
    else:
        st.error("Asupan kalori berlebih")

    st.subheader("💡 Saran Kesehatan")
    if total["protein"] < 50:
        st.write("- Tambahkan sumber protein")
    if total["serat"] < 25:
        st.write("- Perbanyak sayur dan buah")
    if total["gula"] > 50:
        st.write("- Kurangi konsumsi gula")

    if st.button("🔄 Mulai Ulang"):
        st.session_state.page = 1
        st.session_state.user = {}
        st.session_state.meals = []
        st.rerun()
