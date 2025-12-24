import streamlit as st

st.title("👤 Data Pengguna")

nama = st.text_input("Masukkan Nama")
umur = st.number_input("Masukkan Umur", min_value=1, max_value=100)

jenis_kelamin = st.selectbox(
    "Jenis Kelamin",
    ["Pilih", "Laki-laki", "Perempuan"]
)

if st.button("Simpan Data"):
    if nama == "" or jenis_kelamin == "Pilih":
        st.error("Semua data wajib diisi!")
    else:
        st.session_state.user = {
            "nama": nama,
            "umur": umur,
            "jk": jenis_kelamin
        }
        st.success("Data pengguna berhasil disimpan ✅")

# ===== TAMPILKAN DATA =====
if st.session_state.user:
    st.subheader("📄 Data Tersimpan")
    st.write("Nama :", st.session_state.user["nama"])
    st.write("Umur :", st.session_state.user["umur"])
    st.write("Jenis Kelamin :", st.session_state.user["jk"])
