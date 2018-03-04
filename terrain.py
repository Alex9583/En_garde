# -*- coding:utf-8 -*-

NB_CASES = 23
CASE_VIDE = 0
def initialise():
    """Initialise un terrain de NB_CASES de valeur CASE_VIDE=0"""
    terrain = [CASE_VIDE]*NB_CASES
    return terrain

terrain = initialise()

def place(pval, ppos):
    """Remplace la valeur de la position ppos par la valeur pval
    si ppos est hors terrain retourne None"""
    if (-1 < ppos < NB_CASES):
        terrain[ppos] = pval
    else:
        return None


def contenu(ppos):
    """Renvoie le contenu de la position ppos 
    et si hors terrain retourne None  """
    if (-1 < ppos < NB_CASES):
        return terrain[ppos]
    else:
        return None


def est_occupee(ppos):
    """Renvoie False si la case est vide sinon retourne True"""
    if (contenu(ppos) == CASE_VIDE):
        return False
    else:
        return True


def avance(ppos, psens, pn=1):
    """Déplace la valeur contenu dans ppos de pn cases de sens psens (1 pour 
    droite et -1 pour gauche)"""
    if (-1 < (ppos + (pn*psens)) < NB_CASES):
        terrain[ppos + (pn*psens)] = contenu(ppos)
        terrain[ppos] = CASE_VIDE
    else:
        return False


def recule(ppos, psens, pn=1):
    """Déplace la valeur contenu dans ppos de pn cases de sens psens (-1 pour 
    droite et 1 pour gauche)"""
    return avance(ppos, -1*psens, pn)


def affiche():
    """Affiche le terrain en chaîne de caractère"""
    print(''.join(['_' if val == 0 else str(val) for val in terrain]))


def test_initialise():
    """Teste la création du terrain """
    x = initialise()
    return (len(x) == 23) and (all([val == 0 for val in x]))


def test_place():
    """Teste la possibilité de modifier la valeur d' une case et 
    de vérifier si la modification est faîtes"""
    if (place(1, -2) is not None):
        print("Erreur 1")
    if (place(1, NB_CASES + 10) is not None):
        print("Erreur 2")
    terrain[10] = 0
    place(1, 10)
    if (terrain[10] != 1):
        print("Erreur 3")
        exit()


def test_contenu():
    """Teste si le contenu d'une case est bien détecté"""
    place(1, 5)
    if (contenu(NB_CASES + 2) is not None):
        print("Erreur 1")
    if (contenu(5) != 1):
        print("Erreur 2")
        exit()
    place(2, 4)
    if (contenu(4) == 2):
        return True


def test_est_occupee():
    """Teste si la position occupée est bien détecté et 
    de même pour une position vide"""
    place(1, 6)
    if not (est_occupee(6)):
        print("Erreur 1")
    place(0, 8)
    if (est_occupee(8)):
        print("Erreur 2")
        exit()
    if (est_occupee(6)):
        return True


def test_avance():
    """Teste la possibilité de déplacement et si le déplacement s'effectue"""
    place(1, 2)
    place(0, 3)
    if (avance(NB_CASES ,1 ,2) is not False):
        print("Erreur 1")
    avance(2 ,1 ,1)
    if (contenu(3) != 1):
        print("Erreur 2")
    place(2, 10)
    place(0, 5)
    avance(10, -1, 5)
    if (contenu(5) != 2):
        print("Erreur 3")
    place(0 ,5)
    avance(3 ,1, 2)
    if (contenu(5) == 1):
        return True


def test_recule():
    """Teste la possibilité de déplacement et si le déplacement s'effectue"""
    place(1, 2)
    place(0, 3)
    if (recule(0, 1, 2) is not False):
        print("Erreur 1")
    recule(2 ,1 ,1)
    if (contenu(1) != 1):
        print("Erreur 2")
    place(2, 10)
    place(0, 15)
    recule(10, -1, 5)
    if (contenu(15) != 2):
        print("Erreur 3")
    place(0 ,1)
    place(1, 3)
    recule(3 ,1, 2)
    if (contenu(1) == 1):
        return True


if __name__ == "__main__":
    print(test_initialise())
    print(test_place() == None)
    print(test_contenu())
    print(test_est_occupee())
    print(test_avance())
    print(test_recule())
    affiche()
