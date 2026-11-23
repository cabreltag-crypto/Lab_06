# Exercice 11

numero = input("Entrez votre numéro de carte de crédit : ")
numero = numero.replace(" ", "").replace('-','')
if numero.isnumeric():
    quatre_derniers = numero[-4:]
    print(quatre_derniers)
    nb_etoiles = len(numero) - 4
    numero_masque = ("*" * nb_etoiles) + quatre_derniers
print(f"Numéro masqué : {numero_masque}")




