import os

# Ce message DOIT apparaître après la ligne 14
print("=== DÉBUT DU SCRIPT PYTHON ===")

# On vérifie si GitHub nous donne bien les clés
email_test = os.getenv('EMAIL_USER')
print(f"Connexion établie pour : {email_test}")

# On simule une recherche pour tester l'affichage
print("Recherche en cours dans le fonds JORF...")
print("Résultat : 0 texte trouvé (Simulation)")

print("=== FIN DU SCRIPT PYTHON ===")
