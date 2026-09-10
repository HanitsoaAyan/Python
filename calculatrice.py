
n1 = int(input("Entrez le premier nombre : "))
n2 = int(input("Entrez le deuxième nombre : "))

signe = input("Entrez le signe que tu veux : ")

match signe:
    case '+':
        result = n1 + n2
        print(result) 
    case '-':
        result = n1 - n2
        print(result) 
    case "*":
        result = n1 * n2
        print(result) 
    case '/':
        if n2 != 0 :
            result = n1 / n2
            print(result) 
        else : 
            print("Impossible de diviser par zéro")
    case '%':
        if n2 != 0 :
            result = n1%n2
            print(result) 
        else : 
            print("Impossible de voir le modulo par zéro")
    case _:
        print("Sign invalid")
          

       
            