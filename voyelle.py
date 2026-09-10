phrase = input("Entrez une phrase : ")

cpt = 0

voyelle = ['a','i','e','u','o','y']

for char in phrase:
    if char in voyelle:
        cpt += 1
    
print(cpt)