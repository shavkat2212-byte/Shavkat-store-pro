import streamlit as st
import pandas as pd

from database import (
    get_products,
    add_product,
    delete_product
)

st.title("📦 Склад")

st.divider()

c1, c2 = st.columns([2,1])

with c1:

    search = st.text_input(
        "🔍 Поиск товара"
    )

with c2:

    st.write("")
    st.write("")

    refresh = st.button("🔄 Обновить")

st.divider()

with st.expander("➕ Добавить товар", expanded=False):

    name = st.text_input("Название")

    qty = st.number_input(
        "Количество",
        min_value=0,
        step=1
    )

    cost = st.number_input(
        "Себестоимость",
        min_value=0.0
    )

    price = st.number_input(
        "Цена продажи",
        min_value=0.0
    )

    category = st.text_input("Категория (необязательно)")

    brand = st.text_input("Бренд (необязательно)")

    note = st.text_area("Комментарий")

    if st.button("💾 Сохранить товар"):

        if name == "":

            st.warning("Введите название")

        else:

            add_product({

                "name": name,

                "qty": qty,

                "cost": cost,

                "price": price,

                "category": category,

                "brand": brand,

                "note": note

            })

            st.success("Товар сохранен")

            st.rerun()

products = get_products()

if search:

    products = [

        p for p in products

        if search.lower() in p["name"].lower()

    ]

st.divider()

st.subheader("Товары")

if len(products)==0:

    st.info("Товаров пока нет.")

else:

    df = pd.DataFrame(products)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Удаление товара")

    ids = {
        f'{p["name"]} ({p["qty"]} шт)':p["id"]

        for p in products
    }

    selected = st.selectbox(

        "Выберите товар",

        ids.keys()

    )

    if st.button("🗑️ Удалить"):

        delete_product(ids[selected])

        st.success("Удалено")

        st.rerun()
