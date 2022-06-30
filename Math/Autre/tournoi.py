import random as rd

def generate_players(nbr_players):
    duos = {}
    for i in range(nbr_players-1):
        duos[str("duo" + str(i+1))] = ["player" + str(i+1), "player" + str(i+2)]
    duos[str("duo" + str(i+2))] = ["player" + str(i+2), "player" + str(1)]
    return duos

def tournoi(nbr_players):

    duos = generate_players(nbr_players)
    print(duos)

    for i in range(len(duos)):

        for j in range(len(duos)):
            
            win = rd.randint(0,1)

            duoA = str("duo" + str(i+1))

            if str("duo" + str(j+1)) != duoA:
                duoB = str("duo" + str(j+1))

                if win == 0:
                    duos[duoA].append(1)
                    print("Le " + duoA + " a gagné le duel contre le " + duoB)
                else:
                    duos[duoB].append("1")
                    print("Le " + duoA + " a perdu le duel contre le " + duoB)

            elif str("duo" + str(j+1)) not in duos:
                duoB = str("duo" + str(1))

                if win == 0:
                    duos[duoA].append(1)
                    print("Le " + duoA + " a gagné le duel contre le " + duoB)
                else:
                    duos[duoB].append("1")
                    print("Le " + duoA + " a perdu le duel contre le " + duoB)
            
            else:
                duoB = str("duo" + str(1))


            


tournoi(16)