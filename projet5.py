class Pizza:
    def __init__(self,i,p,f):
        self.ingredient = i
        self.patte = p
        self.four = f
        
    def preparation(self):
        print("Je prépare la patte avec ", self.patte, " puis j'ajoute l'ingrédient ", self.ingredient, " et je le met dans la four ", self.four, " a 180 degré")
        
        
peperoni = Pizza(i="saucisse,fromage,tomate", p="farine,oeuf,eau,lait",f="Trust")
peperoni.preparation()