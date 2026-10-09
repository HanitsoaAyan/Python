import time

print("Bienvenue sur notre simulateur de Jardin")
time.sleep(2)

titre = input("Veuillez entrer le nom du jardin \n ==> ")

print("Chargement !!!")
time.sleep(3)

print("Le Jardin ", titre, " est prêt !!!" )


L = [
    ["[]","[]","[]","[]","[]"],
    ["[]","[]","[]","[]","[]"],
    ["[]","[]","[]","[]","[]"]
]

for ligne in L:
    for colone in ligne:
        print(colone, end=" ")
    print()
    
print()

time.sleep(2)

choice = input("Veuillez choisir une case : ")

if(choice )
