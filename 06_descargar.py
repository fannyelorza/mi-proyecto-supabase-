from supabase import create_client
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

response = supabase.table("productos").select("*").execute()

df = pd.DataFrame(response.data)

df.to_csv("productos.csv", index=False)

print("CSV descargado")