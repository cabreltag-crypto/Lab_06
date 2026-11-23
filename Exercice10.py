# Exercice 10

numero = input("Entrez votre numéro de carte de crédit : ")
quatre_derniers = numero[-4:]
nb_etoiles = len(numero) - 4
numero_masque = ("*" * nb_etoiles) + quatre_derniers
print(f"Numéro masqué : {numero_masque}")