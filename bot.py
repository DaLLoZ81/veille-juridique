import os
import requests
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText

# 1. RÉCUPÉRATION DES ACCÈS (DEPUIS LE COFFRE-FORT)
CLIENT_ID = os.getenv('PISTE_CLIENT_ID')
CLIENT_SECRET = os.getenv('PISTE_CLIENT_SECRET')

# 2. OBTENTION DU JETON (Le badge pour entrer sur Légifrance)
def get_token():
    url = "https://oauth.piste.gouv.fr/api/oauth/token"
    payload = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'scope': 'openid'}
    response = requests.post(url, data=payload)
    return response.json().get('access_token')

# 3. RECHERCHE DES TEXTES
def chercher_textes(token, mot_cle, fond):
    url = "https://api.piste.gouv.fr/dila/legifrance/lf-engine-app/search"
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    
    # On cherche sur les 7 derniers jours
    date_debut = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    
    payload = {
        "fond": fond,
        "recherche": {
            "champs": [{"criteres": [{"typeRecherche": "UN_DES_MOTS", "valeur": mot_cle}], "typeChamp": "ALL"}],
            "filtres": [{"facette": "DATE_PUBLI", "dates": {"start": date_debut}}]
        }
    }
    
    res = requests.post(url, headers=headers, json=payload)
    return res.json().get('results', [])

# 4. EXECUTION ET ENVOI
token = get_token()
resultats_hospitalier = chercher_textes(token, "fonction publique hospitalière", "JORF")
# ... la logique d'envoi de mail suivra ici
