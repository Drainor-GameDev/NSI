from typing import List
from Cartes import *
from Files import *
class JeuBataille:
    """
    Jeu de bataille
    Attributs:
        - nom_joueur1 : chaine
        - nom_joueur2 : chaine
        - paquetBataille : liste des cartes
        - cartes_j1 : pile des cartes du joueur 1
        - cartes_j2 : pile des cartes du joueur 2
        - defausse : pile des cartes de la défausse
        - nb_tours : entier, nombre de tours de jeu
        - nb_batailles : entier, nombre de cas d'égalité lors des tirages simultanés

    Méthodes :
        - __init__
        - jouer : jeu de l'oridnateur contre lui-même. Il est conseillé:
            soit de mettre très peu de cartes (8 au total max)
            soit de préciser un nombre maximal de tours de jeu
            Renvoie :
                match_nul : booléen au nom explicite
                gagnant : chaîne de caractères
                self.nb_batailles
                self.nb_tours
    """

    def __init__(self, nom_joueur1='ordi1', nom_joueur2='ordi2'):
        """Constructeur du jeu"""
        self._nomjoueur1 = nom_joueur1
        self._nomjoueur2 = nom_joueur2
        self._paquetBataille = PaquetCartes('bataille', 20)
        donne = self._paquetBataille.melange().distribution(2)
        self._cartesj1 = File(donne[0])
        self._cartesj2 = File(donne[1])
        self._defausse = File()
        self._nb_tours = 0
        self._nb_batailles = 0
        print("Cartes j1")
        self._cartesj1.printFile()
        print("Cartes j2")
        self._cartesj2.printFile()

    def jouer(self):
        # jouez avec très peu de cartes (4 à 10).
        # Fixez un maximum de nombre de tours de jeu
        prize = File()
        matchNull = False
        while self._nb_tours < 50 and not self._cartesj1.estFileVide() and not self._cartesj2.estFileVide():
            self._nb_tours += 1
            carte1 = self._cartesj1.premier()
            carte2 = self._cartesj2.premier()
            if carte2.estSuperieure(carte1):
                self._cartesj2.enfiler(self._cartesj1.defiler())
                self._cartesj2.enfiler(self._cartesj2.defiler())
                #self._cartesj1.defiler()
                #self._cartesj2.defiler()
                while not prize.estFileVide():
                    self._cartesj1.enfiler(prize.defiler())
            elif carte1.estSuperieure(carte2):
                self._cartesj1.enfiler(self._cartesj2.defiler())
                self._cartesj1.enfiler(self._cartesj1.defiler())
                while not prize.estFileVide():
                    self._cartesj1.enfiler(prize.defiler())
            else:
                self._nb_batailles += 1
                for i in range(2):
                    if not self._cartesj2.estFileVide():
                        prize.enfiler(self._cartesj2.defiler())
                    if not self._cartesj1.estFileVide():
                        prize.enfiler(self._cartesj1.defiler())
        if self._cartesj1.estFileVide():
            gagnant = self._nomjoueur2
        elif self._cartesj2.estFileVide():
            gagnant = self._nomjoueur1
        else:
            matchNull = True
        return (matchNull, gagnant, self._nb_batailles, self._nb_tours)


baston = JeuBataille()
(mat, gagnant, nb_batailles, tours) = baston.jouer()
if mat:
    print("match nul, ce n'est pas fréquent")
else:
    if gagnant == None:
        print("trop de tours de jeu. Il y a eu ", nb_batailles, " batailles")
    else:
        print(gagnant, " a gagné en ", tours, " tours de jeu, et ", nb_batailles, " batailles.")
