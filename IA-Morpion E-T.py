#DEBUT
# Import des bibliotheques necessaires au programme
from Morpion import *
from copy import *
from random import *

# Selectionner la meilleure possibilitee de jeu
def bestMove(joueur2coup, esp, tablo, full):
        # On cree une liste vide pour y ajouter nos possibilitees avec leur score
        moves = list()
        # On parcours le tableau pour classer chaque possibilitee
        for i in range(esp):
            for j in range(esp):
                # Si la case est disponible
                if tablo[i][j] == "*":
                    # On fait une copie du tableau dans laquelle on joue
                    copy = deepcopy(tablo)
                    copy[i][j] = joueur2coup
                    # Et on recupere le resultat
                    win = win(copy)
                    # Si le tableau est plein et que personne ne gagne, on le grade 0
                    if win == "*" and full(copy):
                        score = 0
                    # Si il permet de gagner, on le grade 1
                    elif win == joueur2coup:
                        score = 1
                    # Sinon, on le grade avec l'oppose du score pour le joueur adverse
                    # pour son meilleur coup dans son jeu suivant
                    else:
                        score = 0 - bestMove()[1]
                    result = ((i, j), score)

                    # Si le score est 1, on joue ce coup
                    if score == 1:
                        return result
                    # Sinon on l'ajout dans la liste avec les autres et on continue
                    moves.append(result)

        # Une fois tous les coups dans la liste, on les trie par score
        shuffle(moves)
        moves.sort(key=lambda move: move[1], reverse=True)
        # Et on joue le meilleur
        return moves[0]
