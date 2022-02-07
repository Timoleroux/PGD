from matplotlib import pyplot as plt

# Coordonnées des points.
A = [1, 2]
B = [5, 5]
C = [11, 4]
D = [7, 1]

xA = A[0]
yA = A[1]
xB = B[0]
yB = B[1]
xC = C[0]
yC = C[1]
xD = D[0]
yD = D[1]

# Vérifie si les points A, B et C sont alignés.
if xA + xB == xC and yA + yB == yC:
    print("Les points sont alignés")
else:
    print("Les points ne sont pas alignés")


# Vérifie si les droites (AB) et (CD) sont parallèles.
if (xA - xB) * (yC - yD) == (yA - yB) * (xC - xD):
    print("Les droites sont parallèles")
else:
    print("Les droites ne sont pas parallèles")


# Affichage du graphique.

plt.plot(xA, yA, "bo")
plt.plot(xB, yB, "bo")
plt.plot(xC, yC, "bo")
plt.plot(xD, yD, "bo")

plt.annotate("A", (xA+0.15, yA-0.2))
plt.annotate("B", (xB+0.15, yB-0.2))
plt.annotate("C", (xC+0.15, yC-0.2))
plt.annotate("D", (xD+0.15, yD-0.2))

plt.axis('equal')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(color='black', linestyle='-', linewidth=0.5)

try:
    plt.show()
except:
    print("Impossible d'afficher le graphique.")