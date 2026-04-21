

class Arbre:

    __Nom = ""
    __Hauteur = 0
    __Hauteur_Max = 0
    __Feuilles = 0
    __Feuilles_Max = 0
    __Couleur_Feuilles = ""
    __Racines = ""
    __Fruit = ""
    __Branches = 0
    __saison = ["Printemps", "Eté", "Automne", "Hiver"]



    def __init__(self, Nom, Hauteur, Hauteur_Max, Feuilles, Feuilles_Max, Couleur_Feuilles, Racines, Fruit, Branches, saison):
        self.__Nom = Nom
        self.__Hauteur = Hauteur
        self.__Hauteur_Max = Hauteur_Max
        self.__Feuilles = Feuilles
        self.__Feuilles_Max = Feuilles_Max
        self.__Couleur_Feuilles = Couleur_Feuilles
        self.__Racines = Racines
        self.__Fruit = Fruit
        self.__Branches = Branches
        self.__saison = saison

    def __str__(self):
        return f"L'arbre nommé {self.__Nom} fait {self.__Hauteur}cm."

    def pousser(self):
        if self.__Hauteur_Max > self.__Hauteur > 0:
            self.__Hauteur += 5
        else:
            self.__Hauteur = self.__Hauteur_Max

    def couper_arbre(self):
        if self.__Hauteur > 0:
            self.__Hauteur -= 2

    def generer_feuilles(self):
        if self.__saison in ["Printemps", "Eté"]:
            self.__Feuilles += 100


    def tomber(self):
        if self.__saison in ["Automne", "Hiver"]:
            self.__Feuilles -= 100

    def getNom(self):
        return self.__Nom

    def getpousser(self):
        return self.__Hauteur

    def getHauteur(self):
        return self.__Hauteur

    def getFeuilles(self):
        return self.__Feuilles

    def changer_saison(self, nouvelle_saison):
        if nouvelle_saison in self.SAISONS:
            self.__saison = nouvelle_saison

            if nouvelle_saison in ["Automne", "Hiver"]:
                self.tomber()

    def setNom(self, nouveau_nom):
        if len(nouveau_nom) > 0:  # Petite validation : le nom ne doit pas être vide
            self.__Nom = nouveau_nom
            print(f"L'arbre s'appelle désormais {self.__Nom} !")