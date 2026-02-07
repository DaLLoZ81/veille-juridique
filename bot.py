import os
import sys

# On force l'écriture dans les logs quoi qu'il arrive
sys.stdout.write("--- DEBUT DU SCRIPT PYTHON ---\n")
sys.stdout.flush()

print("Vérification des secrets en cours...")

user_mail = os.getenv('EMAIL_USER')
if user_mail:
    print(f"✅ Le bot voit votre adresse : {user_mail}")
else:
    print("❌ Le bot ne voit pas de secret EMAIL_USER")

print("--- FIN DU SCRIPT PYTHON ---")
sys.stdout.flush()
# --- CETTE PARTIE DÉCLENCHE LE BOT ---
if __name__ == "__main__":
    print("!!! LE DÉCLENCHEUR FONCTIONNE !!!")
    # Ici nous remettrons vos fonctions de veille après
