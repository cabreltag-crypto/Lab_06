# Exercice 12
mot_de_passe = input("Entrez un mot de passe : ")

# Définition des caractères spéciaux considérés
caracteres_speciaux = "!, @, #, $, %"

if len(mot_de_passe) <= 8:
    print('le mot de passe doit avoir au moins 8 caracteres')
else:
    print('le mot de passe a le bon nombre de caracteres')
