# Exercice 9
import string

phrase = input("Entrez une phrase : ")
for char in string.punctuation + "’'":
    phrase = phrase.replace(char, " ")

mots = phrase.split()
if not mots:
    print("Aucun mot trouvé.")

mot_plus_long = max(mots, key=len)
print(f"Mot le plus long : {mot_plus_long}")