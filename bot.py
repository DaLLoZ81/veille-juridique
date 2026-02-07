import os

# 1. On force l'affichage immédiat pour vérifier que le bot "parle"
print("--- DÉMARRAGE DU DIAGNOSTIC ---")

# 2. On vérifie si les secrets sont bien chargés
client_id = os.getenv('PISTE_CLIENT_ID')
email = os.getenv('EMAIL_USER')

if client_id:
    print(f"✅ Identifiant PISTE détecté (commence par : {client_id[:5]}...)")
else:
    print("❌ ERREUR : PISTE_CLIENT_ID est vide. Vérifiez vos Secrets GitHub.")

if email:
    print(f"✅ Email détecté : {email}")
else:
    print("❌ ERREUR : EMAIL_USER est vide. Vérifiez vos Secrets GitHub.")

print("--- FIN DU DIAGNOSTIC ---")
