import streamlit as st

st.set_page_config(
    page_title="Shavkat Store Pro",
    page_icon="🏪",
    layout="wide"
)

st.title("Shavkat Store Pro")

st.write("Если ты видишь это сообщение, значит app.py работает.")

try:
    import pages
    st.success("Папка pages найдена")
except Exception as e:
    st.error(e)
