# Exercice 12
mot_de_passe = input("Entrez un mot de passe : ")

caracteres_speciaux = ["!", "@", "#", "$", "%"]

if len(mot_de_passe) <= 8:
    print('le mot de passe doit avoir au moins 8 caracteres')
else:
    print('le mot de passe a le bon nombre de caracteres')
if any(c.isupper() for c in mot_de_passe):
    print('le mot de passe contient au moins une majuscule')
else:
    print('le mot de passe doit contenir au moins une majuscule')