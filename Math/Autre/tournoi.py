import random as rd
import itertools as iter
from unittest import result

def generate_players(nbr_players):

    players = {}
    for i in range(nbr_players):
        players.append("player" + str(i))

    return players

def tournoi():
    
    liste_de_joueurs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'] #16 joueurs de 'a' jusqu'a 'p'
    groupe = iter.combinations(liste_de_joueurs , 4)
    result = []
    for equipe in groupe :
        result.append(equipe)

    return result


print(tournoi())

















def tournoi_(nbr_players):

    duos = generate_players(nbr_players)
    print(duos)

    for i in range(len(duos)):

        for j in range(len(duos)):
            
            win = rd.randint(0,1)

            duoA = str("duo" + str(i+1))

            # Empeche que le duo joue contre lui meme
            if str("duo" + str(j+1)) != duoA:
                
                # Empeche que le duo joue contre un duo inexistant (duo17)
                if str("duo" + str(j+1)) not in duos: 
                    duoB = str("duo" + str(1))
                else:
                    duoB = str("duo" + str(j+1))

                # Affiche le vainqueur ou le perdant et acutalise le score du duo gagant
                if win == 0:
                    duos[duoA].append(1)
                    print("Le " + duoA + " a gagné le duel contre le " + duoB)
                else:
                    duos[duoB].append(1)
                    print("Le " + duoA + " a perdu le duel contre le " + duoB)
    
    # Affiche les scores de chaque duo
    for i in range(nbr_players):
        print("Le duo", str(i+1), "a gagné", len(duos["duo" + str(i+1)])-2, "duels")