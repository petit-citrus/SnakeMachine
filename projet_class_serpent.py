# -*- coding: utf-8 -*-

class Serpent:
    """La classe permettant de créer le serpent. 
    La direction indique dans laquel direction il doit aller pour son prochain coup. 
    La tête pour donner un skin différent et ainsi voir vers ou il se dirige.
    Le nombre de tour restant pour savoir quand effacer le corps concerner pour eviter qu'il reste sans disparaitre"""
    
    def __init__(self):
        self.direction = None
        self.tete = None
        self.tour_restant = None
    
    def rajout_vie(self):
        """parcours tout les morceaux du corps pour augmenter tour_restant de 1"""
        self.tour_restant += 1

    def set_tete(self):
        """Passe tete de True à False et change la texture"""
        Serpent.tete = False
        pass

    def go(self):
        """Fait avancer le serpent dans la bonne direction (A voir avec Esteban et moi)"""
        #si il y a un 2 à cote le prendre sinon aller à la case 0
        Serpent.direction = 0 or 2
        pass

s = Serpent()

