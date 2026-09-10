phrase = input("Entrez une phrase ==> ")

nombre_caracteres = len(phrase)

mots = phrase.split()
nombre_mots = len(mots)

mot_plus_long = max(mots, key=len)

voyelles = "aeiouyAEIOUY"
nombre_voyelles = 0

for caractere in phrase:
    if caractere in voyelles:
        nombre_voyelles += 1

nombre_consonnes = 0

for caractere in phrase:
    if caractere.isalpha() and caractere not in voyelles:
        nombre_consonnes += 1

print("Nombre de caractères :", nombre_caracteres)
print("Nombre de mots :", nombre_mots)
print("Mot le plus long :", mot_plus_long)
print("Nombre de voyelles :", nombre_voyelles)
print("Nombre de consonnes :", nombre_consonnes)