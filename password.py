
mdp = input("Creer un mot de passe ==> ")

if len(mdp) >= 8 and any(c.isdigit() for c in mdp) and any(c.isupper() for c in mdp) and any(c.islower() for c in mdp):
    print("Mot de passe Valider")
else :
    print("Le mot de passe ne peut pas etre valider")   
    
