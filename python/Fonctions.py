from flask import request, render_template
from dotenv import load_dotenv
import os

load_dotenv()
supabase_url = os.getenv("supabase_url")
supabase_key = os.getenv("supabase_key")

from supabase import create_client, Client
supabase: Client = create_client(supabase_url, supabase_key)

def detailsparniveaucode():
    niveau = request.form.get('niveau')
    affichage = supabase.table('oeuvres').select('*').eq('niveau', niveau).execute()
    details = affichage.data
    return render_template('oeuvreparniveau.html', details=details)

def detailsparoeuvrecode():
    if request.method == 'POST':
        id_oeuvre = request.form.get('id')
    else:  # GET
        id_oeuvre = request.args.get('id')
    
    if not id_oeuvre:
        return render_template('erreur.html', 
                                message="Aucun identifiant d'œuvre fourni"), 400
    
    affichage = supabase.table('oeuvres').select('*').eq('id', id_oeuvre).execute()
    
    if not affichage.data or len(affichage.data) == 0:
        return render_template('erreur.html', 
                                message=f"Aucune œuvre trouvée avec l'ID {id_oeuvre}"), 404
    
    details = affichage.data[0]
    return render_template('detailsoeuvre.html', details=details)