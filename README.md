# Python — Bases et POO

> Fiche personnelle de révision Python
> Cette documentation regroupe les notions essentielles de Python : variables, conditions, boucles, fonctions, collections, `*args`, `**kwargs`, scope, modules, classes et POO.

---

## Sommaire

* [1. Variables](#1--variables)
* [2. Types de données](#2--types-de-données)
* [3. Entrées et sorties](#3--entrées-et-sorties)
* [4. Opérateurs](#4--opérateurs)
* [5. Conditions](#5--conditions)
* [6. Boucles](#6--boucles)
* [7. Listes](#7--listes)
* [8. Tuples](#8--tuples)
* [9. Sets](#9--sets)
* [10. Dictionnaires](#10--dictionnaires)
* [11. Fonctions](#11--fonctions)
* [12. `*args` et `**kwargs`](#12--args-et-kwargs)
* [13. Scope et règle LEGB](#13--scope-et-règle-legb)
* [14. Modules et bibliothèques](#14--modules-et-bibliothèques)
* [15. Exceptions](#15--exceptions)
* [16. Fichiers](#16--fichiers)
* [17. Compréhensions](#17--compréhensions)
* [18. Classes et objets](#18--classes-et-objets)
* [19. Constructeur `__init__`](#19--constructeur-__init__)
* [20. `self`](#20--self)
* [21. Méthodes](#21--méthodes)
* [22. Héritage](#22--héritage)
* [23. Encapsulation](#23--encapsulation)
* [24. Exemple complet POO](#24--exemple-complet-poo)

---

# 1. Variables

Une variable permet de stocker une valeur.

```python
nom = "Ayan"
age = 21
taille = 1.70
etudiant = True
```

Python détermine automatiquement le type.

```python
print(nom)
print(age)
```

Modifier une variable :

```python
age = 22
```

Plusieurs affectations :

```python
a = b = 10

x, y = 10, 20
```

Échanger deux variables :

```python
a, b = b, a
```

---

# 2. Types de données

## `str` — chaîne de caractères

```python
nom = "Ayan"
```

## `int` — entier

```python
age = 21
```

## `float` — nombre décimal

```python
prix = 15.5
```

## `bool` — booléen

```python
majeur = True
```

## `list` — liste

```python
nombres = [1, 2, 3]
```

## `tuple` — tuple

```python
nombres = (1, 2, 3)
```

## `set` — ensemble

```python
nombres = {1, 2, 3}
```

## `dict` — dictionnaire

```python
personne = {
    "nom": "Ayan",
    "age": 21
}
```

Vérifier le type :

```python
print(type(age))
```

Convertir un type :

```python
age = int("21")
prix = float("15.5")
nombre = str(20)
```

---

# 3. Entrées et sorties

## Afficher

```python
print("Bonjour")
```

## Demander une information

```python
nom = input("Entrez votre nom : ")
```

`input()` retourne toujours une chaîne (`str`).

Pour récupérer un nombre :

```python
age = int(input("Entrez votre âge : "))
```

## F-string

```python
nom = "Ayan"
age = 21

print(f"Je m'appelle {nom} et j'ai {age} ans.")
```

---

# 4. Opérateurs

## Opérateurs arithmétiques

```python
+    # addition
-    # soustraction
*    # multiplication
/    # division
//   # division entière
%    # reste
**   # puissance
```

Exemple :

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

## Comparaison

```python
==   # égal
!=   # différent
>    # supérieur
<    # inférieur
>=   # supérieur ou égal
<=   # inférieur ou égal
```

## Logique

```python
and
or
not
```

Exemple :

```python
age = 21

if age >= 18 and age < 30:
    print("Entre 18 et 29 ans")
```

---

# 5. Conditions

## `if`

```python
age = 20

if age >= 18:
    print("Majeur")
```

## `if / else`

```python
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

## `if / elif / else`

```python
note = 15

if note >= 16:
    print("Très bien")
elif note >= 10:
    print("Admis")
else:
    print("Échec")
```

---

# 6. Boucles

## Boucle `for`

```python
for i in range(5):
    print(i)
```

Résultat :

```text
0
1
2
3
4
```

### Parcourir une liste

```python
nombres = [10, 20, 30]

for nombre in nombres:
    print(nombre)
```

## `while`

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

## `break`

Arrête la boucle :

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

## `continue`

Passe directement à l'itération suivante :

```python
for i in range(10):
    if i == 5:
        continue

    print(i)
```

## `range()`

```python
range(5)          # 0 à 4
range(2, 6)       # 2 à 5
range(0, 10, 2)   # 0, 2, 4, 6, 8
```

---

# 7. Listes

Une liste est **modifiable**.

```python
nombres = [10, 20, 30]
```

## Accéder à un élément

```python
print(nombres[0])
print(nombres[-1])
```

## Ajouter

```python
nombres.append(40)
```

## Insérer

```python
nombres.insert(1, 15)
```

## Supprimer

```python
nombres.remove(20)
```

ou :

```python
nombres.pop()
```

## Taille

```python
len(nombres)
```

## Trier

```python
nombres.sort()
```

## Parcourir

```python
for nombre in nombres:
    print(nombre)
```

---

# 8. Tuples

Un tuple ressemble à une liste mais il est **non modifiable**.

```python
nombres = (10, 20, 30)
```

Accéder :

```python
print(nombres[0])
```

Parcourir :

```python
for nombre in nombres:
    print(nombre)
```

Un tuple peut être utilisé pour retourner plusieurs valeurs :

```python
def calcul():
    return 10, 20

a, b = calcul()

print(a)
print(b)
```

---

# 9. Sets

Un `set` contient des éléments **uniques**.

```python
nombres = {1, 2, 3, 3, 4}

print(nombres)
```

Les doublons sont supprimés.

## Ajouter

```python
nombres.add(5)
```

## Supprimer

```python
nombres.remove(2)
```

## Vérifier

```python
if 3 in nombres:
    print("Existe")
```

## Union

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

## Intersection

```python
print(a & b)
```

## Différence

```python
print(a - b)
```

---

# 10. Dictionnaires

Un dictionnaire fonctionne avec **clé → valeur**.

```python
personne = {
    "nom": "Ayan",
    "age": 21,
    "ville": "Antananarivo"
}
```

## Accéder

```python
print(personne["nom"])
```

## Ajouter

```python
personne["profession"] = "Étudiante"
```

## Modifier

```python
personne["age"] = 22
```

## Supprimer

```python
del personne["age"]
```

ou :

```python
personne.pop("age")
```

## Vérifier une clé

```python
if "nom" in personne:
    print("La clé existe")
```

## Parcourir

```python
for cle, valeur in personne.items():
    print(cle, valeur)
```

Méthodes importantes :

```python
personne.keys()
personne.values()
personne.items()
```

---

# 11. Fonctions

Une fonction permet de regrouper du code réutilisable.

```python
def dire_bonjour():
    print("Bonjour")
```

Appeler la fonction :

```python
dire_bonjour()
```

## Paramètre

```python
def bonjour(nom):
    print(f"Bonjour {nom}")

bonjour("Ayan")
```

## Plusieurs paramètres

```python
def addition(a, b):
    return a + b

resultat = addition(10, 5)

print(resultat)
```

## `return`

`return` permet de retourner une valeur :

```python
def carre(nombre):
    return nombre * nombre

print(carre(5))
```

## Paramètre par défaut

```python
def bonjour(nom="Ayan"):
    print(f"Bonjour {nom}")
```

---

# 12. `*args` et `**kwargs`

## `*args`

Permet de recevoir plusieurs arguments positionnels.

```python
def addition(*args):
    total = 0

    for nombre in args:
        total += nombre

    return total

print(addition(10, 20, 30))
```

`args` est un **tuple**.

```python
def test(*args):
    print(type(args))
```

## `**kwargs`

Permet de recevoir plusieurs arguments nommés.

```python
def afficher(**kwargs):
    for cle, valeur in kwargs.items():
        print(cle, valeur)

afficher(
    nom="Ayan",
    age=21,
    ville="Antananarivo"
)
```

`kwargs` est un **dictionnaire**.

## Les deux ensemble

```python
def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(10, 20, nom="Ayan", age=21)
```

---

# 13. Scope et règle LEGB

Le **scope** détermine où une variable est accessible.

Python cherche une variable selon la règle :

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

## Local

```python
def test():
    nom = "Ayan"
    print(nom)
```

`nom` existe seulement dans la fonction.

## Global

```python
nom = "Ayan"

def afficher():
    print(nom)
```

## `global`

Pour modifier une variable globale :

```python
compteur = 0

def incrementer():
    global compteur
    compteur += 1
```

## Enclosing

```python
def externe():
    nom = "Ayan"

    def interne():
        print(nom)

    interne()
```

## `nonlocal`

Permet de modifier une variable du scope enclosing :

```python
def compteur():
    nombre = 0

    def incrementer():
        nonlocal nombre
        nombre += 1
        print(nombre)

    incrementer()
```

---

# 14. Modules et bibliothèques

Un **module** est un fichier Python contenant du code réutilisable.

## Importer un module

```python
import random

nombre = random.randint(1, 10)
```

## Importer une fonction

```python
from math import sqrt

print(sqrt(25))
```

## Alias

```python
import random as rd

print(rd.randint(1, 10))
```

## Bibliothèques Python utiles

### `random`

```python
import random

random.randint(1, 10)
random.choice(["Python", "Java", "C++"])
```

### `math`

```python
import math

math.sqrt(25)
math.pi
```

### `datetime`

```python
import datetime

print(datetime.datetime.now())
```

### `os`

```python
import os

print(os.getcwd())
```

### `json`

```python
import json
```

---

# 15. Exceptions

Les exceptions permettent de gérer les erreurs.

```python
try:
    nombre = int(input("Nombre : "))
    print(10 / nombre)

except ValueError:
    print("Veuillez entrer un nombre.")

except ZeroDivisionError:
    print("Division par zéro impossible.")
```

## `finally`

S'exécute toujours :

```python
try:
    print("Test")
except:
    print("Erreur")
finally:
    print("Fin")
```

---

# 16. Fichiers

## Lire un fichier

```python
with open("fichier.txt", "r") as fichier:
    contenu = fichier.read()

print(contenu)
```

## Écrire

```python
with open("fichier.txt", "w") as fichier:
    fichier.write("Bonjour")
```

Modes :

```text
r → lecture
w → écriture
a → ajouter
```

---

# 17. Compréhensions

Permet de créer une collection de manière concise.

## Liste classique

```python
nombres = []

for i in range(5):
    nombres.append(i)
```

## List comprehension

```python
nombres = [i for i in range(5)]
```

Avec condition :

```python
pairs = [i for i in range(10) if i % 2 == 0]
```

Résultat :

```text
[0, 2, 4, 6, 8]
```

---

# 18. Classes et objets

La programmation orientée objet (POO) permet de créer des **classes** et des **objets**.

Une classe est comme un modèle.

```python
class Personne:
    pass
```

Créer un objet :

```python
personne1 = Personne()
personne2 = Personne()
```

Ici :

```text
Personne → classe
personne1 → objet
personne2 → objet
```

---

# 19. Constructeur `__init__`

`__init__` est appelé automatiquement lors de la création d'un objet.

```python
class Personne:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
```

Créer un objet :

```python
personne = Personne("Ayan", 21)
```

---

# 20. `self`

`self` représente **l'objet actuel**.

```python
class Personne:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
```

Ici :

```python
self.nom
```

représente le `nom` de l'objet actuel.

Exemple :

```python
p1 = Personne("Ayan", 21)
p2 = Personne("Alice", 22)
```

Alors :

```python
p1.nom
```

→ `Ayan`

et :

```python
p2.nom
```

→ `Alice`

---

# 21. Méthodes

Une méthode est une fonction définie dans une classe.

```python
class Personne:

    def __init__(self, nom):
        self.nom = nom

    def dire_bonjour(self):
        print(f"Bonjour, je suis {self.nom}")
```

Utilisation :

```python
personne = Personne("Ayan")

personne.dire_bonjour()
```

---

# 22. Héritage

Une classe peut hériter d'une autre classe.

```python
class Animal:

    def parler(self):
        print("L'animal fait un bruit")
```

Classe enfant :

```python
class Chien(Animal):
    pass
```

Le chien possède maintenant la méthode `parler()`.

```python
chien = Chien()

chien.parler()
```

---

# 23. Encapsulation

En Python, `_` et `__` peuvent être utilisés pour indiquer qu'un attribut est destiné à un usage interne.

```python
class Personne:

    def __init__(self, nom):
        self._nom = nom
```

Avec `__` :

```python
class Personne:

    def __init__(self, nom):
        self.__nom = nom
```

---

# 24. Exemple complet POO

## Classe Pizza

```python
class Pizza:

    def __init__(self, ingredient, pate, four):
        self.ingredient = ingredient
        self.pate = pate
        self.four = four

    def preparation(self):
        print(
            f"Je prépare la pâte avec {self.pate}, "
            f"puis j'ajoute {self.ingredient} "
            f"et je la mets dans le four {self.four} à 180 degrés."
        )
```

Créer un objet :

```python
pepperoni = Pizza(
    ingredient="saucisse, fromage, tomate",
    pate="farine, oeuf, eau, lait",
    four="Trust"
)
```

Appeler une méthode :

```python
pepperoni.preparation()
```

---

# Résumé rapide

| Notion                     | Exemple                |
| -------------------------- | ---------------------- |
| Variable                   | `age = 21`             |
| String                     | `"Ayan"`               |
| Integer                    | `21`                   |
| Float                      | `1.5`                  |
| Boolean                    | `True`                 |
| Liste                      | `[1, 2, 3]`            |
| Tuple                      | `(1, 2, 3)`            |
| Set                        | `{1, 2, 3}`            |
| Dictionnaire               | `{"nom": "Ayan"}`      |
| Condition                  | `if / elif / else`     |
| Boucle                     | `for / while`          |
| Fonction                   | `def ma_fonction()`    |
| Retour                     | `return`               |
| Arguments variables        | `*args`                |
| Arguments nommés variables | `**kwargs`             |
| Scope                      | `LEGB`                 |
| Module                     | `import math`          |
| Exception                  | `try / except`         |
| Classe                     | `class Personne:`      |
| Objet                      | `Personne()`           |
| Constructeur               | `__init__`             |
| Objet actuel               | `self`                 |
| Méthode                    | `def parler(self):`    |
| Héritage                   | `class Chien(Animal):` |

---

# À retenir en priorité

Pour les bases Python :

```text
Variables
Types
Opérateurs
Conditions
Boucles
Listes
Tuples
Sets
Dictionnaires
Fonctions
*args / **kwargs
Scope
Modules
Exceptions
```

Pour la POO :

```text
Classe
Objet
__init__
self
Attributs
Méthodes
Héritage
Encapsulation
```

> 💡 Quand j'oublie une notion Python, je peux revenir dans ce README et chercher directement la section correspondante.
