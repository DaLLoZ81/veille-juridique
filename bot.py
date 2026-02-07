import os
import sys

# On utilise sys.stdout.write pour forcer l'écriture immédiate
sys.stdout.write("!!! LE PYTHON EST BIEN ALIVE !!!\n")
sys.stdout.flush()

print(f"Utilisateur : {os.getenv('EMAIL_USER')}")
print("Fin du test de vie.")
