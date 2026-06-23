import streamlit as st
import streamlit.components.v1 as components
import time

PASSWORD = st.secrets["PASSWORD"]

DAFTAR_FILE = {
    "📁 Database - Lampiran 1": {
        "view": st.secrets["lampiran1"]["view"],
        "edit": st.secrets["lampiran1"]["edit"],
    },
    "📊 Data Wilayah - Lamp 01": {
        "view": st.secrets["lamp01"]["view"],
        "edit": st.secrets["lamp01"]["edit"],
    },
}

def check_password():
    st.sidebar.title("🔐 Login Kantor")
    user_password = st.sidebar.text_input("Masukkan Password", type="password")
    return user_password == PASSWORD

st.set_page_config(page_title="Portal Data Internal PHW", page_icon="📂", layout="wide")
st.title("📂 Portal Data Internal PHW")

if check_password():
    st.sidebar.markdown("---")
    st.sidebar.title("📁 Pilih Data")

    menu_list = list(DAFTAR_FILE.keys())
    pilihan = st.sidebar.radio("📋 " + str(len(menu_list)) + " file tersedia:", options=menu_list)

    file_info = DAFTAR_FILE[pilihan]
    st.subheader(pilihan)

    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("🔄 Refresh Data"):
            st.rerun()
    with col2:
        st.link_button("✏️ Edit di Google Sheets", file_info["edit"])

    st.caption("💡 Setelah edit di Google Sheets, tunggu 5-10 menit lalu klik Refresh Data.")
    st.markdown("---")

    timestamp = int(time.time() // 60)
    url_with_cache_bust = file_info["view"] + "?t=" + str(timestamp)
    components.iframe(url_with_cache_bust, height=600, scrolling=True)

else:
    st.info("🔒 Silakan masukkan password di sidebar kiri untuk mengakses data.")
