def debut():
    print("==============================")
    print("L'AVENTURE MYSTÉRIEUSE")

    nom = input("Quel est votre nom, jeune aventurier: ")
    print("Bienvenue", nom)

    print("Tu débutes ton aventure devant un vieux château.")
    print("1. Entrer dans le vieux château")
    print("2. Entrer dans la forêt hantée")

    choix = input("Ton choix : ")

    if choix == "1":
        print("Tu entres dans le vieux château.")
        print("Tu vois deux portes devant toi.")
        print("1. Ouvrir la porte rouge")
        print("2. Ouvrir la porte noire")

        choix_chateau = input("Ton choix : ")

        if choix_chateau == "1":
            print("Tu trouves un trésor caché !")
        elif choix_chateau == "2":
            print("Tu découvres un passage secret rempli d'ossements.")
        else:
            print("Choix invalide ")

    elif choix == "2":
        print("Tu entres dans les bois de la forêt hantée.")
        print("Tu entends des bruits dans les arbres.")
        print("Une lumière apparaît entre les branches.")
        print("1. Suivre la lumière dans la forêt")
        print("2. Explorer une grotte")
        print("3. Faire demi-tour")

        choix_foret = input("Ton choix : ")

        if choix_foret == "1":
            print("Tu trouves une potion magique !")
        elif choix_foret == "2":
            print("Un gros monstre garde un trésor dans la grotte !")
        elif choix_foret == "3":
            print("Tu retournes devant le château.")
        else:
            print("Choix invalide !")
    else:
        print("Choix invalide !")

    print("\nTu continues ton aventure...")
    print("Soudain, tu aperçois un vieux village abandonné.")
    print("Tu entends un bruit étrange provenant d'une maison.")
    print("1. Entrer dans la maison")
    print("2. Explorer le village")

    choix_village = input("Ton choix : ")

    if choix_village == "1":
        print("Tu entres lentement dans la maison.")
        print("Tu découvres une vieille bibliothèque.")
        print("Un livre brille sur une table.")
        print("1. Lire le livre")
        print("2. Ouvrir un coffre")

        choix_maison = input("Ton choix : ")

        if choix_maison == "1":
            print("Le livre contient une ancienne prophétie.")
            print("Elle parle d'un trésor caché sous le château.")
        elif choix_maison == "2":
            print("Tu ouvres le coffre.")
            print("Tu trouves une mystérieuse clé en argent.")
        else:
            print("Choix invalide !")

    elif choix_village == "2":
        print("Tu explores les rues du village.")
        print("Tu découvres une vieille fontaine.")
        print("Une pièce mystérieuse se trouve dans l'eau.")
        print("1. Prendre la pièce")
        print("2. Continuer ton exploration")

        choix_exploration = input("Ton choix : ")

        if choix_exploration == "1":
            print("Tu récupères une pièce ancienne.")
            print("Une porte secrète commence à s'ouvrir.")
        elif choix_exploration == "2":
            print("Tu décides de continuer dans le village.")
            print("Tu aperçois une silhouette au loin.")
        else:
            print("Choix invalide !")
    else:
        print("Choix invalide !")

    print("Tu remarques une étrange lumière au loin.")
    print("Elle semble provenir d'une montagne.")
    print("Tu décides de t'en approcher.")
    print("\nTu arrives au pied de la montagne.")
    print("Tu aperçois une vieille tour abandonnée.")
    print("Une porte semble légèrement ouverte.")
    print("1. Entrer dans la tour")
    print("2. Monter sur le chemin de la montagne")

    choix_montagne = input("Ton choix : ")

    if choix_montagne == "1":
        print("Tu entres dans la vieille tour.")
        print("Tu découvres un coffre mystérieux.")
        print("1. Ouvrir le coffre")
        print("2. Continuer à monter les escaliers")

        choix_tour = input("Ton choix : ")

        if choix_tour == "1":
            print("Tu trouves une épée magique !")
        elif choix_tour == "2":
            print("Tu découvres une pièce secrète !")
        else:
            print("Choix invalide !")

    elif choix_montagne == "2":
        print("Tu commences à monter la montagne.")
        print("Tu découvres un ancien temple.")
        print("Une mystérieuse porte bloque ton chemin.")
        print("1. Ouvrir la porte")
        print("2. Faire demi-tour")

        choix_temple = input("Ton choix : ")

        if choix_temple == "1":
            print("Tu découvres un trésor légendaire !")
        elif choix_temple == "2":
            print("Tu retournes dans la forêt.")
        else:
            print("Choix invalide !")
    else:
        print("Choix invalide !")

    print("\nAprès toutes ces aventures, tu arrives devant une immense porte.")
    print("La porte semble protéger un trésor légendaire.")
    print("Une voix mystérieuse te demande de faire un dernier choix.")
    print("1. Ouvrir la porte et découvrir le trésor.")
    print("2. Quitter les lieux et retourner chez toi.")

    choix_final = input("Ton choix : ")

    if choix_final == "1":
        print("\nLa porte s'ouvre lentement.")
        print("Tu découvres un immense trésor rempli d'or et de pierres précieuses !")
        print("Tu as réussi toutes les épreuves.")
        print("FÉLICITATIONS ! TU AS TERMINÉ L'AVENTURE MYSTÉRIEUSE !")

    elif choix_final == "2":
        print("\nTu décides de rentrer chez toi.")
        print("Tu garderas le souvenir de cette incroyable aventure.")
        print("FIN DE L'AVENTURE !")

    else:
        print("Choix invalide !")
        print("Tu quittes finalement les lieux.")
        print("FIN DE L'AVENTURE !")


if __name__ == "__main__":
    debut()
