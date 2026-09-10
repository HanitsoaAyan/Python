number = int(input("Entrez un nombre : "))


for pair in range(number+1):
    if pair%2 == 0:
        print(pair)
        
if number%2 !=0:
    print("Nombre ", number, " est impair")
    
    
