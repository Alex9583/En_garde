# -*- coding: utf-8 -*-

from random import randrange
liste = [1, 2, 3, 4, 5]


def initialise(ppioche=None, pdefausse=None):
    """Initialise la pioche et la défausse"""
    #ppioche et pdefausse sont des listes pour les parties chargées
    if (ppioche is None) and (pdefausse is None):
        pioche = liste * 5
        defausse = []
    else:
        pioche = ppioche
        defausse = pdefausse
    return (pioche, defausse)

x = initialise()
pioche = x[0]
defausse = x[1]


def melange(pioche):
    """Mélange la pioche en décalant les éléments aléatoirements de (0,10)"""
    i = 0
    while (i < len(pioche)):
        decale = randrange(0,10)
        pioche[i],pioche[(i + decale)%len(pioche)] = \
            pioche[(i + decale)%len(pioche)], pioche[i]
        i = i + 1
    return pioche

def pioche_carte(pioche):
    """Retourne la carte à prendre et l'enlève de la pioche"""
    carte = pioche[0]
    pioche.pop(0)
    return carte


def longueur_pioche():
    """Renvoie la longueur de la pioche """
    return (len(pioche))


def defausse_carte(pcarte,defausse):
    """Met la carte à la defausse"""
    defausse = defausse + [pcarte]
    return defausse

def derniere_defausse(defausse):
    """Renvoie la dernière la carte de la défausse """
    if (len(defausse) != 0):
        return defausse[len(defausse) - 1]
    else:
        return None

def affiche():
    """Affiche les informations sur les cartes en jeu """
    print("Il reste ",longueur_pioche()," carte(s) dans la pioche")
    print("Il y a ",len(defausse)," carte(s) dans la défausse")
    print("La dernière carte mise à la défausse est :",derniere_defausse())


def serialise():
    """Récupère les données pour les mettre dans un fichier de sauvegarde"""
    return "C: " + ", ".join([str(c) for c in pioche]) + "; " + \
        ", ".join([str(d) for d in defausse])


def deserialise(pchaine):
    pass


def test_initialise():
    """Test la création de la pioche et de la défausse"""
    if (len(pioche) != 25):
        print("Error 1")
    if (len(defausse) != 0):
        print("Error 2")


def test_melange():
    """Test le melange de la pioche"""
    test_pioche = [pioche[:]]
    melange()
    if (pioche.count(1) != 5):
        print("Error 1")
    if (pioche.count(2) != 5):
        print("Error 2")
    if (pioche.count(3) != 5):
        print("Error 3")
    if (pioche.count(4) != 5):
        print("Error 4")
    if (pioche.count(5) != 5):
        print("Error 5")
    if (pioche != test_pioche):
        return True


def test_pioche_carte():
    """Test si la carte est retirée et si la bonne carte est retournée """
    carte = pioche[0]
    if (pioche_carte() != carte):
        print("Error 1")
    if (pioche.count(carte) != 4):
        print("Error 2")
    if (len(pioche) == 24):
        return True


def test_longueur_pioche():
    """Test si la longueur de la pioche est bien détectée """
    if (longueur_pioche() == 24):
        return True


def test_defausse_carte():
    """Test la mise à la défausse d'une carte donnée"""
    defausse_carte(5)
    if (len(defausse) != 1):
        print("Error 1")
    if (defausse[0] == 5):
        return True


def test_derniere_defausse():
    """Test si la dernière carte de la défausse est bien détectée"""
    global defausse
    if (derniere_defausse() != 5):
        print("Error 1")
    defausse.clear()
    if (derniere_defausse() is None):
        defausse = defausse + [5]
        return True
    else:
        print("Error 2")


def test_affiche():
    return affiche()


def test_serialise():
    """Affiche ce qui sera écrit dans le fichier de sauvegarde"""
    print(serialise())
    
if __name__ == "__main__":
    print(test_initialise() is None)
    print(test_melange())
    print(test_pioche_carte())
    print(test_longueur_pioche())
    print(test_defausse_carte())
    print(test_derniere_defausse())
    test_affiche()
    test_serialise()
