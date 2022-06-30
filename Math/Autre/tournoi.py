import random as rd

def generate_players(nbr_players):

    duos = {}

    for i in range(nbr_players-1):
        # Génère la liste des jouers et leur duo
        duos[str("duo" + str(i+1))] = ["player" + str(i+1), "player" + str(i+2)]

    # Empeche la génération d'un joueur inexistant (player17)
    duos[str("duo" + str(i+2))] = ["player" + str(i+2), "player" + str(1)]

    return duos

def tournoi(nbr_players):

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

tournoi(16)