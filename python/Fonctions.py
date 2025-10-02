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
    affichage = supabase.table('oeuvres').select('*').eq('niveau', niveau).execute()
    details = affichage.data
    return render_template('oeuvreparniveau.html', details=details)

def detailsparoeuvrecode():
    id=request.form.get('id')
    # Logique pour récupérer les détails en fonction de l'oeuvre
    affichage = supabase.table('oeuvres').select('*').eq('id', id).execute()
    details = affichage.data[0]
    return render_template('detailsoeuvre.html', details=details)