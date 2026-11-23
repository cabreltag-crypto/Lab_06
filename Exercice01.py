# Exercice 1

voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
mot = input('entrez votre mot : ')
compteur = 0
for i in mot:
    if i in voyelles:
        compteur = compteur + 1
print(f'le mot {mot} contient  {compteur} voyelles')