# Exercice 2
phrase = input('entrer votre Phrase: ')
cpt_majuscule = 0
cpt_minuscule = 0
for mot in phrase:
    if mot.isupper():
        cpt_majuscule = cpt_majuscule +1
    elif mot.islower():
        cpt_minuscule = cpt_minuscule +1
    else:
        pass
print(f'la phrase {phrase} contient  {cpt_majuscule} majuscules')
print(f'la phrase {phrase} contient  {cpt_minuscule} minuscules')