import streamlit as st
import pandas as pd
from io import BytesIO

from database import (
    get_products,
    add_product,
    update_product,
    delete_product,
)

st.set_page_config(layout="wide")

st.title("📦 Склад")

# ---------- Получаем товары ----------

products = get_products()

# ---------- Итоги ----------

total_qty = sum(p["qty"] for p in products)

total_cost = sum(
    p["qty"] * float(p["cost"])
    for p in products
)

total_price = sum(
    p["qty"] * float(p["price"])
    for p in products
)

profit = total_price - total_cost

c1, c2, c3, c4 = st.columns(4)

c1.metric("📦 Товаров", total_qty)

c2.metric(
    "💰 Себестоимость",
    f"{total_cost:,.0f} сом"
)

c3.metric(
    "🏷 Стоимость продажи",
    f"{total_price:,.0f} сом"
)

c4.metric(
    "📈 Возможная прибыль",
    f"{profit:,.0f} сом"
)

st.divider()

# ---------- Поиск ----------

search = st.text_input(
    "🔍 Поиск товара"
)

if search:

    products = [

        p for p in products

        if search.lower() in p["name"].lower()

    ]

# ---------- Добавление ----------

with st.expander(
    "➕ Добавить товар"
):

    col1, col2 = st.columns(2)

    with col1:

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

    with col2:

        category = st.text_input(
            "Категория"
        )

        brand = st.text_input(
            "Бренд"
        )

        note = st.text_area(
            "Комментарий"
        )

    if st.button("💾 Сохранить"):

        if name == "":

            st.warning("Введите название")

        else:

            add_product(

                name,

                qty,

                cost,

                price,

                category,

                brand,

                note

            )

            st.success("Товар добавлен")

            st.rerun()

st.divider()

# ---------- Таблица ----------

if len(products):

    df = pd.DataFrame(products)

    show = df[
        [
            "id",
            "name",
            "qty",
            "cost",
            "price",
            "category",
            "brand",
        ]
    ]

    show.columns = [

        "ID",

        "Название",

        "Кол-во",

        "Себестоимость",

        "Продажа",

        "Категория",

        "Бренд"

    ]

    st.dataframe(
        show,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("Товаров нет.")

st.divider()

# ---------- Excel ----------

if len(products):

    excel = pd.DataFrame(products)

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        excel.to_excel(
            writer,
            index=False
        )

    st.download_button(

        "📤 Экспорт в Excel",

        output.getvalue(),

        "products.xlsx",

        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

st.divider()

# ---------- Удаление ----------

if len(products):

    ids = {

        f'{p["name"]} ({p["qty"]})': p["id"]

        for p in products

    }

    selected = st.selectbox(

        "Удалить товар",

        ids.keys()

    )

    if st.button("🗑️ Удалить"):

        delete_product(

            ids[selected]

        )

        st.success("Удалено")

        st.rerun()
