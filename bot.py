import os
import requests
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURATION ---
CLIENT_ID = os.getenv('PISTE_CLIENT_ID')
CLIENT_SECRET = os.getenv('PISTE_CLIENT_SECRET')
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

def get_token():
    url = "https://oauth.piste.gouv.fr/api/oauth/token"
    payload = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'scope': 'openid'}
    res = requests.post(url, data=payload)
    if res.status_code != 200:
        print(f"ERREUR AUTHENTIFICATION : {res.status_code}")
        print(res.text)
        return None
    return res.json().get('access_token')

def chercher_donnees(token, mot_cle, fond):
    if not token:
        return []
    
    url = "https://api.piste.gouv.fr/dila/legifrance/lf-engine-app/search"
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    date_debut = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    
    payload = {
        "fond": fond,
        "recherche": {
            "champs": [{"criteres": [{"typeRecherche": "UN_DES_MOTS", "valeur": mot_cle}], "typeChamp": "ALL"}],
            "filtres": [{"facette": "DATE_PUBLI", "dates": {"start": date_debut}}]
        }
    }
    
    res = requests.post(url, headers=headers, json=payload)
    
    # C'est ici que nous vérifions si tout va bien
    if res.status_code == 200:
        return res.json().get('results', [])
    else:
        print(f"ERREUR LÉGIFRANCE ({fond}) : Code {res.status_code}")
        print(f"Message du serveur : {res.text}")
        return []

# --- EXECUTION ---
token = get_token()

if token:
    fph_decrets = chercher_donnees(token, "fonction publique hospitalière", "JORF")
    juris_ce = chercher_donnees(token, "fonction publique", "CETAT")
    juris_admin = chercher_donnees(token, "fonction publique hospitalière", "JURI")

    # Si on a trouvé quelque chose, on prépare le mail (le reste du code est identique)
    # ... [Code de mise en forme et d'envoi de mail] ...
    print("Processus terminé. Vérifiez les logs ci-dessus en cas d'absence de mail.")
else:
    print("Impossible de continuer sans jeton d'accès.")
