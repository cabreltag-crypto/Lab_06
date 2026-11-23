# Exercice 4
mot = input('entrer votre mot : ')
if mot[::1] == mot[::-1]:
    print(f'le mot {mot} est un palindrome')
else:
    print(f'le mot {mot} n\'est pas un palindrome')