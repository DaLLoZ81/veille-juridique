import sys

# On force l'écriture immédiate dans les logs
print("--- TENTATIVE DE CONNEXION FORCEE ---", flush=True)

# Cette ligne va volontairement créer une erreur pour nous parler
raise Exception("LE BOT FONCTIONNE ET CECI EST UNE ERREUR VOLONTAIRE")

print("Cette ligne ne sera jamais lue", flush=True)
