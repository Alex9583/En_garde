# -*- coding:utf-8 -*-


import terrain as tr
import cartes as ct
import joueurs as jr
import interface as it


def tours():
    """Gere les tours en fin d'action """
    if (j1['tour'] == True):
        j1['tour'] = False
        j2['tour'] = True
        return (j1['codage'], j1)
    elif (j2['tour'] == True):
        j2['tour'] = False
        j1['tour'] = True
        return (j2['codage'], j2)


def sauvegarde_partie(pfichier):
    """Gère la partie sauvegarde dans le fichier choisi par l'utilisateur"""
    fichier = open(pfichier,"w")
    fichier.write(ct.serialise() + "\n")
    fichier.write(jr.serialise())
    fichier.close()

def charge_partie(pfichier):
    pass


def serialise():
    pass


def deserialise(pchaine):
    pass


x = ct.initialise()  #Création de la pioche et de la défausse
pioche = x[0]
defausses = x[1]
jr.initialise()
jr.initialise_manche(pioche)
j1 = jr.j1           #Import des dictionnaires j1 et j2
j2 = jr.j2
gagne_manche_j1 = False
gagne_manche_j2 = False
while (not (it.partie_finie(j1) or it.partie_finie(j2))):
    while (not (gagne_manche_j1 or gagne_manche_j2)):
        it.rafraichi(pioche,defausses)
        possible = True     #Regarde la possibilité d'action
        infos = tours()     #Récupère les infos de jeu (tour de joueur)
        tour = infos[0]
        joueur = infos[1]
        print("Tour du joueur",tour)
        action = it.choisi_action()
        if (action == "i"):
            carte_un = it.choisi_cartes(joueur)
            carte_deux = it.choisi_cartes(joueur)
            direction = it.choisi_sens()
            if (direction == "a"):
                sens = 1
            elif (direction == "r"):
                sens = -1
            possible = jr.attaque_indirecte(joueur,(sens
                                                    ,jr.carte_selectionnee(
                                                        joueur,carte_un),
                                                    jr.carte_selectionnee(
                                                        joueur,carte_deux)))
            while (not(possible)):
                print("Action impossible veuillez rechoisir des cartes : ")
                carte_un = it.choisi_cartes(joueur)
                carte_deux = it.choisi_cartes(joueur)
                direction = it.choisi_sens()
                if (direction == "a"):
                    sens = 1
                elif (direction == "r"):
                    sens = -1
                possible = jr.attaque_indirecte(joueur,(sens
                                                        ,jr.carte_selectionnee(
                                                            joueur,carte_un),
                                                        jr.carte_selectionnee(
                                                            joueur,carte_deux)))
            defausses += ct.defausse_carte(jr.carte_selectionnee(joueur,
                                                                 carte_un),
                                           defausses)
            defausses += ct.defausse_carte(jr.carte_selectionnee(joueur,
                                                                 carte_deux),
                                           defausses)
            joueur['main'].pop(carte_un)
            joueur['main'].pop(carte_deux)
        elif (action == "d"):
            carte_un = it.choisi_cartes(joueur)
            direction = it.choisi_sens()
            if (direction == "a"):
                sens = 1
            elif (direction == "r"):
                sens = -1
            possible = (jr.deplace(joueur,
                                   jr.carte_selectionnee(joueur,carte_un),sens)
                        is not False)
            while (not possible):
                print("Déplacement impossible veuillez changer")
                carte_un = it.choisi_cartes(joueur)
                direction = it.choisi_sens()
                if (direction == "a"):
                    sens = 1
                elif (direction == "r"):
                    sens = -1
                possible = (jr.deplace(joueur,
                                       jr.carte_selectionnee(joueur,
                                                             carte_un),sens)
                            is not False)
            defausses += ct.defausse_carte(jr.carte_selectionnee(joueur,
                                                                 carte_un),
                                           defausses)
            joueur['main'].pop(carte_un)
        elif (action == "a"):
            carte_un = it.choisi_cartes(joueur)
            possible = jr.attaque_directe(joueur,
                                          jr.carte_selectionnee(joueur,
                                                                carte_un))
            while (not(possible)):
                print("Attaque impossible veuillez rechoisir une carte : ")
                carte_un = it.choisi_cartes(joueur)
                possible = jr.attaque_directe(joueur,
                                              jr.carte_selectionnee(joueur,
                                                                    carte_un))
            defausses += ct.defausse_carte(jr.carte_selectionnee(joueur,
                                                                 carte_un),
                                           defausses)
            joueur['main'].pop(carte_un)
        if (len(pioche) != 0):
            jr.complete_main(joueur,pioche)
        gagne_manche_j1 = jr.gagne_manche(j1,pioche)
        gagne_manche_j2 = jr.gagne_manche(j2,pioche)
    if (gagne_manche_j1 == True and gagne_manche_j2 == True):
        it.manche_finie_nulle(j1,j2,pioche,gagne_manche_j1,gagne_manche_j2)
    if (gagne_manche_j1):
        it.manche_finie_touche(j1,pioche,gagne_manche_j1)
    if (gagne_manche_j2):
        it.manche_finie_touche(j2,pioche,gagne_manche_j2)
    if ((j1["score"] != 5) and (j2["score"] != 5)):
        recommence = input("Voulez vous passer à la manche suivante: o/n/s ? ")
        if (recommence == "o"):
            x = ct.initialise()
            pioche = x[0]
            defausses = x[1]
            jr.initialise_manche(pioche)
            gagne_manche_j1 = jr.gagne_manche(j1,pioche)
            gagne_manche_j2 = jr.gagne_manche(j2,pioche)
        elif (recommence == "s"):
            choix_s = it.choisi_fichier()
            sauvegarde_partie(choix_s)
            it.affiche_partie_sauvegardee()
        else:
            if (j1["score"] > j2["score"]):
                j1["score"] = 5
            elif (j2["score"] > j1["score"]):
                j2["score"] = 5
            else:
                print("Egalité")
                break
