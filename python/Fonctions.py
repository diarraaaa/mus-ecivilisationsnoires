from flask import request, render_template
from dotenv import load_dotenv
import os
load_dotenv()
supabase_url = os.getenv("supabase_url")
supabase_key = os.getenv("supabase_key")
from supabase import create_client, Client
supabase: Client = create_client(supabase_url, supabase_key)                                         

def detailsparniveaucode():
    niveau=request.form.get('niveau')
    # Logique pour récupérer les détails en fonction du niveau
    
   