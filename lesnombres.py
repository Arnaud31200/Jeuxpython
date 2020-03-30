""" Appel du module random """
from random import randint

class Ecart:
    """ Définition de la classe Ecart"""
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        print(
            "Propose un nombre entre "
            , self.nombre1, "et "
            , self.nombre2
            , "et appuie sur Entrée !")

ECART = Ecart(1, 100)
NOMBRE = randint(ECART.nombre1, ECART.nombre2)
REPONSE = int(input("Propose une réponse :"))

while NOMBRE != REPONSE:
    if (ECART.nombre1 - 1) < REPONSE < NOMBRE:
        print("C'est plus !")
    elif NOMBRE < REPONSE < (ECART.nombre2 + 1):
        print("C'est moins !")
    else:
        print("Choisis un nombre entre ", (ECART.nombre1), "et ", (ECART.nombre2), "!")
    REPONSE = int(input("Propose une réponse :"))

if REPONSE == NOMBRE:
    print("Bravo !")
    print("Jeu terminé !")
