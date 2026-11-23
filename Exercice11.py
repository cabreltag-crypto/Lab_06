# Exercice 11

numero = input("Entrez votre numéro de carte de crédit : ")
numero = numero.replace(" ", "").replace('-','')
if numero.isnumeric() and len(numero) == 16:
    quatre_derniers = numero[-4:]
    nb_etoiles = len(numero) - 4
    numero_masque = ("*" * nb_etoiles) + quatre_derniers
    print(f"Numéro masqué : {numero_masque}")
else:
    print('le numero de carte de credit doit contenir 16 chiffres')



