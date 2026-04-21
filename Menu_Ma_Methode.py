from Ma_Methode import Arbre
import os


def gerer_un_arbre(arbre):
    """Sous-menu pour s'occuper d'un arbre précis"""
    while True:
        print(f"\n--- GESTION DE : {arbre.getNom().upper()} ---")
        print(arbre)
        print("1. Faire pousser | 2. Couper | 3. Renommer | 4. Retour au jardin")

        action = input("Votre choix : ")
        if action == "1":
            arbre.pousser()
        elif action == "2":
            arbre.couper_arbre()
        elif action == "3":
            nouveau = input("Nouveau nom : ")
            arbre.setNom(nouveau)
        elif action == "4":
            break  # On sort de cette boucle pour revenir au menu principal


def lancer_app():
    mon_jardin = []


    if os.path.exists("save_arbre.csv"):
        reponse = input("📂 Sauvegarde trouvée. Charger ? (O/N) : ")
        if reponse.upper() == "O":
            try:
                with open("save_arbre.csv", "r", encoding="utf-8") as f:
                    for ligne in f:  # On lit chaque ligne (chaque arbre)
                        d = ligne.strip().split(",")
                        if len(d) >= 3:
                            # On crée l'arbre et on l'ajoute direct au jardin
                            a = Arbre(d[0], int(d[1]), 500, int(d[2]), 1000, "Vert", "Pivot", "Gland", 5, "Printemps")
                            mon_jardin.append(a)
                print(f"✅ {len(mon_jardin)} arbre(s) chargé(s) !")
            except Exception as e:
                print(f" Erreur chargement : {e}")

    while True:
        print("\n" + "=" * 30)
        print(f"--- MON JARDIN ({len(mon_jardin)} arbres) ---")
        print("1. Planter un nouvel arbre")
        print("2. Voir et gérer un arbre")
        print("3. Sauvegarder tout le jardin")
        print("4. Quitter")

        choix = input("\nVotre choix : ")

        if choix == "1":
            nom = input("Nom de l'arbre : ")
            fruit = input("Fruit : ")  # Optionnel : tu peux l'ajouter dans ton Arbre()
            nouvel_arbre = Arbre(nom, 50, 500, 0, 1000, "Vert", "Pivot", fruit, 5, "Printemps")
            mon_jardin.append(nouvel_arbre)
            print(f"✅ {nom} planté !")

        elif choix == "2":
            if not mon_jardin:
                print("Le jardin est vide !")
            else:
                for i, arbre in enumerate(mon_jardin):
                    print(f"{i} : {arbre.getNom()}")

                try:
                    index = int(input("Numéro de l'arbre : "))
                    if 0 <= index < len(mon_jardin):
                        # ON LANCE LE SOUS-MENU
                        gerer_un_arbre(mon_jardin[index])
                    else:
                        print("Numéro inconnu.")
                except ValueError:
                    print("Veuillez entrer un chiffre.")

        elif choix == "3":
            try:
                with open("save_arbre.csv", "w", encoding="utf-8") as f:
                    for arbre in mon_jardin:
                        f.write(f"{arbre.getNom()},{arbre.getHauteur()},{arbre.getFeuilles()}\n")
                print("✅ Jardin sauvegardé !")
            except Exception as e:
                print(f" Erreur : {e}")

        elif choix == "4":
            print("Bye !")
            break


if __name__ == "__main__":
    lancer_app()