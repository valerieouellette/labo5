import random


def choix_mot():
    liste_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    mot = input("Choisissez un mot: ")
    for lettre in mot:
        if lettre in liste_numeros:
            raise ValueError
    return mot


def menu_liste_mots():
    liste_mots = []
    erreur = False
    while not erreur:
        try:
            mot = choix_mot()
        except ValueError:
            erreur = True
        else:
            liste_mots.append(mot)
    
    return liste_mots


def choix_mot_liste(liste):
    mot = input("Choisissez un mot de la liste: ")
    if mot in liste:
        return mot
    else:
        raise Exception


def index_aleatoire(mot, liste_mots, nb_rec=1):
    ind_max = len(liste_mots) - 1
    index = random.randint(0, ind_max)
    if liste_mots[index] == mot:
        return nb_rec
    else:
        liste_mots.pop(index)
        nb_rec += 1
        return index_aleatoire(mot, liste_mots, nb_rec)


def menu_choix_mot_liste():
    liste_mots = menu_liste_mots()
    bon_mot = False
    while not bon_mot:
        try: 
            mot = choix_mot_liste(liste_mots)
        except:
            print("Le mot n'est pas dans la liste. Veuillez recommencer.")
        else:
            bon_mot = True
            nb_recursions = index_aleatoire(mot, liste_mots)
            print(f"{nb_recursions} récursions pour trouver le mot!")


menu_choix_mot_liste()


