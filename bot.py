import os
import sys

# On force l'affichage pour le débogage
print("--- INITIALISATION DU BOT ---", flush=True)

try:
    print(f"Version Python : {sys.version}", flush=True)
    print(f"Répertoire de travail : {os.getcwd()}", flush=True)
    print(f"Fichiers présents ici : {os.listdir('.')}", flush=True)
    
    # On vérifie les secrets
    user = os.getenv('EMAIL_USER')
    if user:
        print(f"✅ Utilisateur détecté : {user}", flush=True)
    else:
        print("❌ ALERTE : Aucun utilisateur détecté dans les secrets", flush=True)

except Exception as e:
    print(f"❌ ERREUR CRITIQUE : {e}", flush=True)

print("--- FIN DU DIAGNOSTIC ---", flush=True)
