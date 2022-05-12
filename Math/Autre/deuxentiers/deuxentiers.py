def deuxEntiers() :
    # On commence par définir x et y
    x = 0
    y = 36

    for i in range(36):
        # On reduit l'ecart entre x et y pour chaque iteration (x > y comme dans le systeme)
        y -= 1
        x += 1

        # Si les deux conditions sont remplies (si y-x=8 et x+y=36) alors on affiche le resultat
        if y - x == 8 and x + y == 36:
            print("Pour deux entiers : x =", x, "et y =", y)

deuxEntiers() # On lance la fonction