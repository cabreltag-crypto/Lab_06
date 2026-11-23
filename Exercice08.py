# Exercice 8
phrase = input('entrer votre phrase: ')

nb_lettres = 0
nb_chiffres = 0
nb_espaces = 0

for caractere in phrase:
    if caractere.isalpha():
        nb_lettres += 1
    elif caractere.isdigit():
        nb_chiffres += 1
    elif caractere.isspace():
        nb_espaces += 1

print(f"Nombre de lettres : {nb_lettres}")
print(f"Nombre de chiffres : {nb_chiffres}")
print(f"Nombre d'espaces : {nb_espaces}")
