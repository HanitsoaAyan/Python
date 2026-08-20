noteBacc = float(input("Entrez votre moyenne du Bacc ==>  "))

if noteBacc >= 18:
    print("Il aura les félicitations du jury")
elif noteBacc >= 16:
    print("Mention : Très Bien")
elif noteBacc >= 14:
    print("Mention : Bien")
elif noteBacc >= 12:
    print("Mention : Assez Bien")
else:
    print("Pas de mention")
