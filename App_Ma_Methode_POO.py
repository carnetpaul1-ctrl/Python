# App_Ma_Methode_POO.py

class Chene:
    def __init__(self, nom, saison="Hiver"):
        self.nom = nom
        self.saison = saison

    def __str__(self):
        return f"L'arbre {self.nom} est actuellement en saison : {self.saison}"