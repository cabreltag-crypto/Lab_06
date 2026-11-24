# Exercice 12
mot_de_passe = input("Entrez un mot de passe : ")

caracteres_speciaux = ["!", "@", "#", "$", "%"]
critere_respectes = []
critere_non_respectes = []

if len(mot_de_passe) <= 8:
    critere_non_respectes.append('taille de mot de passe')
else:
    critere_respectes.append('taille de mot de passe')
if any(c.isupper() for c in mot_de_passe):
    critere_respectes.append('doit contenir majuscule')
else:
    critere_non_respectes.append('doit contenir majuscule')
if any(c.islower() for c in mot_de_passe):
    critere_respectes.append('doit contenir minuscule')
else:
    critere_non_respectes.append('doit contenir minuscule')
if any(c.isnumeric() for c in mot_de_passe):
    critere_respectes.append('doit contenir chiffre')
else:
    critere_non_respectes.append('doit contenir chiffre')
if any(c in caracteres_speciaux for c in mot_de_passe):
    critere_respectes.append('doit contenir caractere special')
else:
    critere_non_respectes.append('doit contenir caractere special')


print(f'votre mot de passe respecte les criteres suivant : {critere_respectes}')
print(f'votre mot de passe ne respecte pas les criteres suivant : {critere_non_respectes}')