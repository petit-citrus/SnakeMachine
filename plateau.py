from random import randint


def plateau(taille = 10): 
    """"
    Fonction permettant de créer le plateau de jeu en fonction de la 
    taille +2 passée en paramètre (par défault 10)
    Le plateau est un tableau (liste) à double entrée (liste de liste)
    Pour chaque valeur est à quelque chose (serpent, vide, pomme, mur/obstacle)
    associer à une coordonnée (dans le tableau)
    0 = vide
    1 = serpent (possible modification)
    2 = Pomme 
    3 = Mur/Obstacle
    Chaque bord de plateau sera forcément un obstacle (d'où le " taille +2 ")
    """
    l = []
    for i in range(taille+2):
        l.append([])
        for _ in range(taille +2):
            l[i].append(None)
    return l
    
def mur(l):
    for m in range(len(l)):
        l[0][m] = 3
        l[len(l)-1][m] = 3
        l[m][0] = 3
        l[m][len(l)-1] = 3
    return l
        
def pomme(l):
    """Génère une pomme aléatoirement sur le plateau"""
    x = randint(1, len(l)-2)
    y = randint(1, len(l)-2)
    l[x][y] = 2
    return l

def jeu(taille = 10):
    l = plateau(taille)
    l = mur(l)
    l = pomme(l)
    return l

def verif(l):
    for i in range(len(l)):
        #print("ici")
        for j in range(len(l)):
            #print("coucou")
            if l[i][j] == 2:
                return True
    return False