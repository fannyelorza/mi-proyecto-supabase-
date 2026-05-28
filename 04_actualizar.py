from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

supabase.table("productos").update({
    "precio": 12000
}).eq("nombre", "Laptop").execute()

print("Producto actualizado")