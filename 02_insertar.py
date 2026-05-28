from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

supabase.table("productos").insert({
    "nombre": "Laptop",
    "precio": 15000,
    "stock": 10
}).execute()

print("Producto agregado")