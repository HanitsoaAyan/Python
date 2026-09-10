produit = ["Pomme","Pain","Lait","Riz"]

panier = {
    "Pomme":500,
    "Pain":1000,
    "Lait":2500,
    "Riz":3000
}

choix = 0

while choix != 5:
    print("Veuillez selectionner votre choix : \n")
    print("1.Ajouter un produit")
    print("2.Voir le panier")
    print("3.Supprimer un produit")
    print("4.Voir le prix total")
    print("5.Quitter")
    
    choix = int(input("Entrez votre choix ==> "))
    
    match choix: 
        case 1:
            ajouterproduit = input("Entrez un produit ==> ")
            produit.append(ajouterproduit)
            print("Produit ajouté !")
            print(produit)
        case 2:
            for i in produit:
                print(i)
        case 3:
            produitSupprimer = input("Entrez le produit dans le panier : ")
            
            if produitSupprimer in produit:
                produit.remove(produitSupprimer)
                print("Le produit", produitSupprimer, "est supprimer")
            else:
                print("Le produit ", produitSupprimer, "n'existe pas")
        case 4:
            prixTotal = 0
            for article in produit:
                prixTotal += panier[article]
                
            print("Le prix total des produits dans le panier est ", prixTotal)
        case 5:
            exit()
        case _:
            print("ce n'est pas une option")
            
        
        