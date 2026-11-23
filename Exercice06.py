# Exercice 06
nom = input('entrer le nom: ')
if nom.isalnum() and len(nom) >= 5:
     print('le mot est valide')
else:
    print('le mot n est pas valide')