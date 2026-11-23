# Exercice 7
adresse = input('entrer votre adresse courriel: ')
index1 = adresse.find('@')
index2 = adresse.find('.')
if index2 == index1 + 1:
    print("l'adresse semble valide")
else:
    print("l'adresse semble non valide")

