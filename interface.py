# -*- coding:utf-8 -*-


import joueurs as jr
import cartes as ct
import terrain as tr


def choisi_action():
    """Récupère l'action à effectuer"""
    print("Action: [d]éplacer/[a]ttaque directe/attaque [i]ndirecte/[p]asse ?")
    choix = input()
    return choix


def choisi_cartes(pjoueur):
    """Récupère l'indice de la carte sélectionnée"""
    choix = int(input("Carte à jouer (son indice) ?"))
    return choix


def choisi_sens():
    """Récupère le sens de déplacement"""
    choix = input("[a]vancer ou [r]eculer ?")
    return choix


def choisi_fichier():
    """Récupère le nom de fichier où sauvegarder/charger la partie"""
    choix = input("Nom du fichier où sauvegarder/charger la partie : ")
    return choix


def rafraichi(pioche,defausse):
    """Affiche les informations de jeu """
    plateau = ""
    i = 0
    while (i < len(tr.terrain)):
        if (tr.terrain[i] == 1):
            plateau += "\x1b[32;1m""1""\x1b[0m"
        elif (tr.terrain[i] == 2):
            plateau += "\x1b[31;1m""2""\x1b[0m"
        else:
            plateau += "_"
        i += 1
    print("\x1b[33;1m""******************************""\x1b[0m")
    print("\x1b[33;1m""*""\x1b[0m")
    print("\x1b[33;1m""*  ""\x1b[0m",plateau)
    print("\x1b[33;1m""*""\x1b[0m")
    print("\x1b[33;1m""******************************""\x1b[0m")
    print("\x1b[33;1m""* ""\x1b[0m""score: ""\x1b[32;1m""j1",
          jr.j1["score"],"\x1b[0m"" -  ""\x1b[31;1m""j2",
          jr.j2["score"],"\x1b[0m")
    print("\x1b[33;1m""* ""\x1b[0m""\x1b[32;1m""Joueur 1:""\x1b[0m",
          jr.j1['main'])
    print("\x1b[33;1m""* ""\x1b[0m""\x1b[31;1m""Joueur 2:""\x1b[0m",
          jr.j2['main'])
    print("\x1b[33;1m""* ""\x1b[0m""longueur pioche:", len(pioche))
    print("\x1b[33;1m""* ""\x1b[0m""dernière carte jetée:",
          ct.derniere_defausse(defausse))
    print("\x1b[33;1m""******************************""\x1b[0m")
    

def manche_finie_touche(pjoueur,pioche,gagne_manche):
    """Permet l'affichage de la fin d'une manche """
    if (gagne_manche):
        if (pjoueur['gagnetouche']):
            print("Le joueur",pjoueur['codage'],"à gagné sur touche")
            pjoueur['gagnetouche'] = False
        elif (pjoueur['gagne']):
            print("Le joueur",pjoueur['codage'],
                  "à gagné par impossibilité d'action du joueur adverse")
            pjoueur['gagne'] = False
            pjoueur['score'] -= 1           #Corrige un bug de score 
        else:
            return True
    else:
        return False


def manche_finie_nulle(j1, j2, pioche, gagne_manche_j1, gagne_manche_j2):
    """Affiche l'égalité quand les 2 joueurs ne peuvent plus joueur"""
    if ((manche_finie_touche(j1,pioche,gagne_manche_j1) == True) and 
        (manche_finie_touche(j2,pioche,gagne_manche_j2) == True)):
        print("Egalité")
    else:
        return False


def partie_finie(pjoueur):
    """Affiche la victoire du joueur en fin de partie"""
    if (jr.gagne_partie(pjoueur)):
        print("Le joueur", pjoueur['codage'], "à gagné la partie")
        return True
    else:
        return False


def affiche_partie_sauvegardee():
    """Affiche que la sauvegarde a bien été effectuée"""
    print("La partie à été sauvegardée avec succès")


def affiche_partie_chargee():
    """Affiche que la partie a bien été chargée"""
    print("La partie à été chargée avec succès")


if __name__ == '__main__':
    pass
