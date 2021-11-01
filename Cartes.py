from random import shuffle
class Carte:
    """Carte d'un paquet de cartes, pour jouer à différents jeux.
    On reste dans les paquets 32/52/54 cartes ou tarot

    Attributs :
        - couleur : chaine de caractères, en général coeur/carreau/pique/trèfle,
        mais peu aussi être plus exotique batons/coupes/deniers/épées.
        On peut aussi avoir "atout" ou "joker"
        - hauteur : chaine de caractères, en général de "as" à "roi",
            variantes "un" à "vingt et un" pour les atouts, "aucune" pour les jokers
        - valeur : entier (en général), dépend du jeu.
            Dans un langage fortement typé c'est un flottant (valeurs 0.5 au tarot)

    Méthodes :
        init()
        getCouleur()
        getHauteur()
        getValeur()
        setValeur()
        estSuperieure(autre)  : renvoie un booléen vrai si l'objet
        Carte est de valeur supérieure à celle d'un autre objet Carte
        estEgale(autre)
    """

    def __init__(self, couleur, hauteur, valeur=0):
        self._couleur = couleur
        self._hauteur = hauteur
        self._valeur = valeur

    # méthodes
    def estSuperieure(self, autre):
        return self._valeur > autre.getValeur()

    def estEgale(self, autre):
        return self._valeur == autre._valeur

    # méthodes getters/setters
    def getCouleur(self):
        return self._couleur

    def getHauteur(self):
        return self._hauteur

    def getValeur(self):
        return self._valeur

    def setValeur(self, nouvValeur):
        self._valeur = nouvValeur


# def __repr__(self):
# return f'{self._hauteur} de {self._couleur}, valeur {self._valeur}'

roiCarreau = Carte('carreau', 'roi', 13)
septPique = Carte('pique', 'sept', 7)
print(roiCarreau.estSuperieure(septPique))
print(septPique.estSuperieure(roiCarreau))
print(roiCarreau.getHauteur())


class PaquetCartes:
    """
    Paquet de cartes
    Attributs:
        - nom : nom du paquet, de préférence correspondant au nom du jeu pour
            lequel il va être utilisé
        - paquet : liste des cartes
    """
    _hauteurs = ["as", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix",
                 "valet", "dame", "roi"]
    _couleurs = ["coeur", "pique", "carreau", "trèfle"]

    def __init__(self, nom, nbCartes=32):
        """Constructeur du paquet de cartes"""
        self._nom = nom
        self._nbCartes = nbCartes
        self._paquet = []
        if nbCartes == 32:
            for i in range(6, len(self._hauteurs)):
                for j in range(len(self._couleurs)):
                    self._paquet.append(Carte(self._couleurs[j], self._hauteurs[i], i + 1))
            for j in range(len(self._couleurs)):
                self._paquet.append(Carte(self._couleurs[j], self._hauteurs[0], 14))
        else:
            for i in range(1, len(self._hauteurs)):
                for j in range(len(self._couleurs)):
                    self._paquet.append(Carte(self._couleurs[j], self._hauteurs[i], i + 1))
            for j in range(len(self._couleurs)):
                self._paquet.append(Carte(self._couleurs[j], self._hauteurs[0], 14))

    def melange(self):
        shuffle(self._paquet)
        return self
    def distribution(self, nbJoueurs, nbADistribuer = 0):
        assert self._nbCartes > nbADistribuer * 2
        tableauJeu = []
        if nbADistribuer > 0:
            for i in range(nbJoueurs):
                tableauCartes = []
                for y in range(nbADistribuer):
                    tableauCartes.append(self._paquet[y])
                tableauJeu.append(tableauCartes)
        else:
            for i in range(nbJoueurs):
                tableauCartes = []
                for y in range(self._nbCartes):
                    tableauCartes.append(self._paquet[y])
                tableauJeu.append(tableauCartes)
        return tableauJeu

    def getPaquet(self):
        return self._paquet


paquetBataille = PaquetCartes('bataille', 32)

