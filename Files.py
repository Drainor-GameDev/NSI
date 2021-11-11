from Cartes import *

class File:
    """
    Gère les files FIFO
    Attributs :
        - file : liste d'éléments à priori du même type
        - nb_elements : taille de la file
        - premier : premier élément de la file
        - dernier : dernier élément de la file
    Méthodes :
        - __init__(liste = []) : constructeur, renvoie une file vide si liste
        n'est pas renseigné. Sinon renvoie une file constituée des
        éléments de la liste
        - tete : renvoie l'élément en tête de la file, la file étant non vide
        - enfiler(element) : insère element en fin de file
        - defiler : supprime l'élément en tête de la file.
        On peut le renvoyer éventuellement.
            Si la file est vide, renvoie None
        - estFileVide : teste si la file est vide
        - getters pour nb_elements, premier et dernier
    """
    _file = None
    _nb_elements = 0
    _premier = None
    _dernier = None

    def __init__(self, liste=None):
        """Constructeur de la file
        Remarque : écrire self._file = liste copie l'adresse de liste dans self._file.
        Ceci peut poser des problèmes.
        En effet, si par la suite on modifie liste, alors on modifiera aussi self._file
        """
        self._file = []
        if liste is None:
            self._nb_elements = 0
            self._premier = None
            self._dernier = None
        else:
            for i in range(len(liste)):
                self._nb_elements += 1
                self._file.append(liste[i])
                self._dernier = liste[i]
            self._premier = self._file[0]
            


    def estFileVide(self):

        return len(self._file) == 0

    def enfiler(self, element):
        self._dernier = element
        if self._nb_elements == 0:
            self._premier = element
        self._nb_elements += 1
        self._file = [element] + self._file

    def defiler(self):
        self._nb_elements -= 1
        if self._nb_elements > 0:
            self._premier = self._file[1]
        else:
             self._premier = None
             self._dernier = None
        return self._file.pop()

    # getters
    def premier(self):
        return self._premier

    def dernier(self):
        return self._dernier

    def getNb_elements(self):
        return self._nb_elements

    def printFile(self):
        print("Contenu de la file : ")
        for element in self._file:
            if isinstance(element, Carte):
                print(element)
            else:
                print(element, "n'est pas une carte")
