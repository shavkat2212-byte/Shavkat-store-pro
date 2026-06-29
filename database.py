from supabase import create_client
from config import SUPABASE_KEY, SUPABASE_URL

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# -----------------------------
# PRODUCTS
# -----------------------------

def get_products():

    result = supabase.table("products") \
        .select("*") \
        .order("id", desc=True) \
        .execute()

    return result.data


def add_product(data):

    return supabase.table("products").insert(data).execute()


def delete_product(product_id):

    return supabase.table("products") \
        .delete() \
        .eq("id", product_id) \
        .execute()


def update_product(product_id, data):

    return supabase.table("products") \
        .update(data) \
        .eq("id", product_id) \
        .execute()
