import streamlit as st
from database import supabase

st.set_page_config(
    page_title="Shavkat Store Pro",
    page_icon="🏪",
    layout="wide"
)

st.title("🏪 Shavkat Store Pro")

st.write("## Проверка подключения к Supabase")

try:
    result = supabase.table("products").select("*").limit(1).execute()

    st.success("✅ Подключение к Supabase успешно!")

    st.write("База данных отвечает.")

except Exception as e:

    st.error("❌ Не удалось подключиться к Supabase")

    st.code(str(e))
