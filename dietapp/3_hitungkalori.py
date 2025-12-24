import streamlit as st

st.title("🔥 Total Kalori Harian")

# ===== HITUNG TOTAL =====
total_kalori = 0
for item in st.session_state.meals:
    total_kalori += item["kalori"]

st.metric("Total Kalori", f"{total_kalori} kkal")

# ===== DETAIL =====
if st.session_state.meals:
    st.subheader("📊 Detail Perhitungan")
    for item in st.session_state.meals:
        st.write(f"- {item['makanan']} : {item['kalori']} kkal")
else:
    st.info("Belum ada makanan yang dimasukkan.")
