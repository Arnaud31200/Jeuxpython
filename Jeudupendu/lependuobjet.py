""" Appel du module random """
from random import choice

LISTEDEMOTS = []
with open("Jeudupendu/liste.txt") as myfile:
    for line in myfile:
        LISTEDEMOTS.append(line.strip())

class SYSTEME():
    """ Classe du systeme de jeu """
    LISTEDELETTRES = []
    MOTCACHE = []
    LETTRESUTILISEES = []
    def __init__(self, vies, motchoisi):
        self.vies = vies
        self.motchoisi = motchoisi
        for lettres in motchoisi:
            SYSTEME.LISTEDELETTRES.append(lettres)
            SYSTEME.MOTCACHE.append("_")
        print("Bienvenue dans le jeu du pendu !")
        print("Vous avez ", self.vies, "vies !")
        print("En", len(self.motchoisi), "lettres : ")
        print(" ".join(SYSTEME.MOTCACHE))
    
    def reponse_negative(self):
        """ Fonction de réponse négative """
        print("Incorrect !")
        self.vies = self.vies - 1
        print("Il vous reste ", self.vies, "vies !")

def reponse_positive(lettre_proposee):
    """ Fonction de réponse négative """
    print("Correct !")
    position_lettre = [
        I for I, numero_position in enumerate(SYSTEME.LISTEDELETTRES)
        if numero_position == lettre_proposee]
    for position in position_lettre:
        SYSTEME.MOTCACHE[position] = lettre_proposee

JEU = SYSTEME(5, choice(LISTEDEMOTS))
REPONSE = str(input("Propose une lettre : "))

while JEU.vies > 0:
    if REPONSE not in SYSTEME.LETTRESUTILISEES:
        if REPONSE in SYSTEME.LISTEDELETTRES:
            reponse_positive(REPONSE)
            SYSTEME.LETTRESUTILISEES.append(REPONSE)
        if REPONSE not in SYSTEME.LISTEDELETTRES:
            JEU.reponse_negative()
            SYSTEME.LETTRESUTILISEES.append(REPONSE)
        if SYSTEME.MOTCACHE == SYSTEME.LISTEDELETTRES:
            print("Le mot est : ", JEU.motchoisi)
            print("Tu as Gagné !")
            break
    if REPONSE in SYSTEME.LISTEDELETTRES:
        print("Lettre déjà utilisée !")
    print(" ".join(SYSTEME.MOTCACHE))
    print("Lettres utilisée : ", " ".join(SYSTEME.LETTRESUTILISEES))
    REPONSE = str(input("Propose une lettre : "))

if JEU.vies == 0:
    print("Tu as perdu !")
    print("Le mot était :", JEU.motchoisi)
    print("Jeu terminé !")
