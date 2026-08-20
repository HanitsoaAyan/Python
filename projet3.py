import random
#enumerate()
#break
#validation données
#interface graphique

mots = ["python", "ordinateur", "programmaiton", "clavier", "voyage", "toamasina"]

choix = random.choice(mots)
lettre_trouvees = []
i = 7

while i > 0:
    user = input("Entrez un mot : ")
    if user in choix:
        lettre_trouvees.append(user)
        
        for lettre in choix:
            if lettre in lettre_trouvees:
                print(lettre, end=" ")
            else:
                print("_", end=" ")
        print()
        if all(lettre in lettre_trouvees for lettre in choix):
            print("Tu as gagné !")
            break
        
    else:
        i-=1
        print("Il te reste", i, "vies")
    
    if i == 0:
        print("Tu as perdu ! Le mot était :", choix)   

        
