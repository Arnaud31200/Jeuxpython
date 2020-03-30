""" Appel du module random """
from random import choice

LISTEDEMOTS = []
MOT = choice(LISTEDEMOTS)
LISTEDELETTRES = []
MOTCACHE = []
LETTRESUTILISEES = []
VIES = 5

with open("Jeudupendu/liste.txt") as myfile:
    for line in myfile:
        LISTEDEMOTS.append(line.strip())

for lettres in MOT:
    LISTEDELETTRES.append(lettres)
    MOTCACHE.append("_")

def reponse_positive(lettre_proposee):
    """ Fonction de réponse négative """
    print("Correct !")
    position_lettre = [
        I for I, numero_position in enumerate(LISTEDELETTRES) if numero_position == lettre_proposee]
    for position in position_lettre:
        MOTCACHE[position] = lettre_proposee

def reponse_negative():
    """ Fonction de réponse négative """
    print("Incorrect !")
    print("vies : ", VIES)

def lettres_utilisees(lettre):
    """ Fonction de lettres utilisée """
    LETTRESUTILISEES.append(lettre)

print("En", len(MOT), "lettres : ")
print(" ".join(MOTCACHE))
USER_ANSWER = str(input("Propose une lettre : "))

while VIES > 0:
    if USER_ANSWER not in LETTRESUTILISEES:
        if USER_ANSWER in LISTEDELETTRES:
            reponse_positive(USER_ANSWER)
            lettres_utilisees(USER_ANSWER)
        if USER_ANSWER not in LISTEDELETTRES:
            VIES = VIES - 1
            reponse_negative()
            lettres_utilisees(USER_ANSWER)
        if MOTCACHE == LISTEDELETTRES:
            print("Le mot est : ", MOT)
            print("Tu as Gagné !")
            break
    if USER_ANSWER in LETTRESUTILISEES:
        print("Lettre déjà utilisée !")
    print(" ".join(MOTCACHE))
    print("Lettres utilisée : ", " ".join(LETTRESUTILISEES))
    USER_ANSWER = str(input("Propose une lettre : "))

if VIES == 0:
    print("Tu as perdu !")
    print("Le mot était :", MOT)
