import random
choice = random.randint(1,100)

i = 7

while i > 0:
    number = int(input("Devinez le nombre entre 1 à 100 ==> "))
    if number > choice:
        print("Le nombre est trop grand!!")
        i -= 1
    elif number < choice:
        print("Le nombre est trop petit!!")   
        i -= 1
    else:
        print("Bravo! tu as trouvé le nombre ", choice)
        break
        
if i == 0:
    print("Tu as perdu le nombre etait : ", choice)
        
   