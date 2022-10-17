'''
Vous devez implémenter un algorithme offrant un menu à un utilisateur lui permettant d'entrer plusieurs mots, un seul à la fois, tant et 
aussi longtemps que son mot ne contient pas de chiffres en utilisant la gestion d'erreur.
'''

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
    



'''Vous devez implémenter un algorithme demandant à l'utilisateur d'entrer un mot présent dans la liste. Si l'utilisateur entre un mot 
n'étant pas dans la liste, lancez(raise) une erreur. '''

menu_liste_mots()