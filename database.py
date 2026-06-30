from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# ---------------- PRODUCTS ---------------- #

def get_products():
    response = (
        supabase.table("products")
        .select("*")
        .order("id", desc=True)
        .execute()
    )
    return response.data


def add_product(name, qty, cost, price, category="", brand="", note=""):
    return (
        supabase.table("products")
        .insert({
            "name": name,
            "qty": qty,
            "cost": cost,
            "price": price,
            "category": category,
            "brand": brand,
            "note": note,
        })
        .execute()
    )


def update_product(product_id, name, qty, cost, price, category="", brand="", note=""):
    return (
        supabase.table("products")
        .update({
            "name": name,
            "qty": qty,
            "cost": cost,
            "price": price,
            "category": category,
            "brand": brand,
            "note": note,
        })
        .eq("id", product_id)
        .execute()
    )


def delete_product(product_id):
    return (
        supabase.table("products")
        .delete()
        .eq("id", product_id)
        .execute()
    )


def get_product(product_id):
    response = (
        supabase.table("products")
        .select("*")
        .eq("id", product_id)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None
