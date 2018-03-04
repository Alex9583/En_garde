# -*- coding: utf-8 -*-


import cartes as ct
import terrain as tr
from random import randrange
NB_CASES = 23


def initialise(pjoueur1=None, pjoueur2=None):
    """Initialise les paramètres de chaque joueurs dans un dictionnaire"""
    if (pjoueur1 is None) and (pjoueur2 is None):
        j1 = {'pos':0, 'codage':1, 'main':[], 'score':0, 'tour':False, 
              'sens':1, 'gagnetouche':False, 'gagne':False}
        j2 = {'pos':NB_CASES - 1, 'codage':2, 'main':[], 'score':0,
              'tour':False, 'sens':-1, 'gagnetouche':False, 'gagne':False}
        tour = randrange(1,3)
        if (tour == 1):
            j1['tour'] = True
        else:
            j2['tour'] = True
    else:
        j1 = {'pos':pjoueur1['pos'], 'codage':1, 'main':pjoueur1['main'],
              'score':pjoueur1['score'], 'tour':pjoueur1['tour'], 'sens':1, 
              'gagnetouche':pjoueur1['gagnetouche'], 'gagne':pjoueur1['gagne']}
        j2 = {'pos':pjoueur2['pos'], 'codage':2, 'main':pjoueur2['main'],
              'score':pjoueur2['score'], 'tour':pjoueur2['tour'], 'sens':-1, 
              'gagnetouche':pjoueur2['gagnetouche'], 'gagne':pjoueur2['gagne']}
    return (j1, j2)


x = initialise()
j1 = x[0]
j2 = x[1]


def initialise_manche(pioche):
    """Initialise les paramètres de début de manche"""
    ct.initialise()
    pioche_un = ct.melange(pioche)
    mainj1 = []
    mainj2 = []
    if (j1['tour'] == True):
        j1['tour'] = False
        j2['tour'] = True
    else:
        j1['tour'] = True
        j2['tour'] = False
    i = 0
    while (i < 5):
        mainj1 = mainj1 + [ct.pioche_carte(pioche)]
        mainj2 = mainj2 + [ct.pioche_carte(pioche)]
        i = i + 1
    j1['main'] = mainj1
    j2['main'] = mainj2
    tr.place("_", j1['pos'])
    tr.place("_", j2['pos'])
    j1['pos'] = 0
    j2['pos'] = NB_CASES - 1
    tr.place(j1['codage'], j1['pos'])
    tr.place(j2['codage'], j2['pos'])
    j1['gagnetouche'] = False
    j2['gagnetouche'] = False
    j1['gagne'] = False
    j2['gagne'] = False


def carte_selectionnee(pjoueur, pidx_carte):
    """Renvoie la valeur de la carte indicée idx_carte"""
    main = pjoueur['main']
    return main[pidx_carte]


def deplace(pjoueur, pcarte, psens):
    """Modifie la position de joueur de pcarte"""
    if (pjoueur['codage'] == 1):
        autre = j2
    else:
        autre = j1
    if (psens == 1):
        if (pjoueur['codage'] == 1):
            if ((pjoueur['pos'] + (pcarte*psens)) >= autre['pos']):
                return False
        elif (pjoueur['codage'] == 2):
            if ((pjoueur['pos'] - pcarte) <= autre['pos']):
                return False
        if (tr.avance(pjoueur['pos'], pjoueur['sens'], pcarte) != False):
            pjoueur['pos'] += pcarte*pjoueur['sens'] 
        else:
            return False
    else:
        if (tr.recule(pjoueur['pos'], pjoueur['sens'], pcarte) != False):
            pjoueur['pos'] -= pcarte*pjoueur['sens']
        else:
            return False


def attaque_directe(pjoueur, pvaleurs):
    """Effectue une attaque directe"""
    if (pjoueur['codage'] == 1):
        posj2 = j2['pos']
        if (posj2 - pjoueur['pos'] == pvaleurs): #Teste la difference des pos
            pjoueur['gagnetouche'] = True        #entre les 2 joueurs pour voir
            return True                          #si l'attaque est faisable
        else:
            return False
    else:
        posj1 = j1['pos']
        if (pjoueur['pos'] - posj1 == pvaleurs):
            pjoueur['gagnetouche'] = True
            return True
        else:
            return False


def attaque_indirecte(pjoueur, pvaleurs):
    """Effectue un deplacement (pvaleurs[1]) puis une attaque (pvaleurs[2])"""
    mvt = pvaleurs[1]
    attaque = pvaleurs[2]
    sens = pvaleurs[0]
    codage = pjoueur['codage']
    if (codage == 1):
        victime = j2
    else:
        victime = j1
    if ((pjoueur['pos'] + ((mvt*(sens) + 
                            attaque)*pjoueur['sens']) == victime['pos'])):
        deplace(pjoueur, mvt, sens)
        attaque_directe(pjoueur, attaque)
        return True
    else:
        return False


def complete_main(pjoueur,pioche):
    """Redonne les cartes jusqu'à que le joueur en ai cinq"""
    while (len(pjoueur['main']) < 5):
        pjoueur['main'] += [ct.pioche_carte(pioche)]


def gagne_manche(pjoueur,pioche):
    """Verifie les conditions de victoire"""
    if (pjoueur['gagnetouche']):
        pjoueur['score'] += 1
        return True
    elif (len(pioche) == 0):
        if (pjoueur['codage'] == 1):
            autre = j2
        else:
            autre = j1
        if ((len(pjoueur['main']) == 0) and (len(autre['main']) == 0)):
            return True
        elif (len(pjoueur['main']) == 0):
            autre['gagne'] = True
            autre['score'] += 1
            return True
        elif (len(autre['main']) == 0):
            pjoueur['gagne'] = True
            pjoueur['score'] += 1
            return True
    else:
        return False
          

def gagne_partie(pjoueur):
    """Teste si la score d'un joueur est égale à 5"""
    if (pjoueur['score'] == 5):
        return True
    else:
        return False


def serialise():
    """Récupère les données pour les mettre dans un fichier de sauvegarde"""
    chaine = "J: "
    i = 0
    j = 0
    for cle in j1:
        if (cle == 'main'):
            chaine += str(cle) + ": " + \
                ", ".join([str(i) for i in j1['main']])
        else:
            chaine += str(cle) + ": " + str(j1[cle])
        if (i < 7):
            chaine += " & "
        i += 1
    chaine += " ; "
    for cle in j2:
        if (cle == 'main'):
            chaine += str(cle) + ": " + \
                ", ".join([str(i) for i in j2['main']])
        else:
            chaine += str(cle) + ": " + str(j2[cle])
        if (j < 7):
            chaine += " & "
        j += 1
    return chaine                         

def deserialise(pchaine):
    pass



def test_initialise():
    """Teste le placement des joueurs"""
    x = initialise()
    if (x[0] != 0):
        print("Error 1")
    if (x[1] == NB_CASES - 1):
        return True


if __name__ == '__main__':
    print(test_initialise())
    print(serialise())
