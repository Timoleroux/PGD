from random import randint
import matplotlib.pyplot as plt
import time
plt.clf()

univers = int(input("Nombre d'issue possible : "))
N = int(input("Défnir N : "))

result = {}

def proba():
    # Initialise les valeur dans le dictionnaire
    for i in range(univers):
        result[i+1] = 0
    # On réalise l'experience aleatoire
    for i in range(N):
        issue = randint(1, univers)
        result[issue] += 1

    # On affiche le resultat sous forme textuel
    for i in range(univers):
        print(f"L'issue {i+1} avec une fréquence de {result[i+1]}")

    # On affiche le resultat sous forme graphique
    x = []
    y = []
    for i in range(univers):
        x.append(f"Issue {i+1}")
        y.append(result[i+1])

    plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    plt.title("Probabilité d'obtenir une issue")
    plt.ylabel("Frequence")
    plt.show()

proba()