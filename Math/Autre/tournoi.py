import random as rd

def generate_players(nbr_players):
    duos = {}
    for i in range(nbr_players):
        duos[str("duo" + str(i+1))] = ["player" + str(i+1), "player" + str(i+2)]
    return duos

def tournoi(nbr_players):

    duos = generate_players(nbr_players)

    for i in range(len(duos)):

        for j in range(len(duos)):
            
            win = rd.randint(0,1)

            if win == 0:
                duos[str("duo" + str(i+1))].append(duos[])
            else:
                duos[str("duo" + str(i+2))].append("1")


tournoi(16)