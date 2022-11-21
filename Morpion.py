#DEBUT
#Importer la bibliothèque random
#Admettre qu'il existe une fonction random qui renvoie un chiffre aleatoire
from random import randint
#Créer la surface de jeu pour le morpion
tableJeu = [['-','-','-'],['-','-','-'],['-','-','-']]
#Définir une fonction qui renvoi la surface de morpion
def showTable(tableJeu):
    #Afficher la 1ère ligne séparatrice
    print("--------------")
    #Pour les lignes dans la Table
    for row in tableJeu :
        #Pour les items dans les lignes
        for item in row:
            #Afficher les items dans les lignes
            print(item, end="  ")
        #Afficher un espace
        print()
    #Afficher la 2ème ligne séparatrice
    print("--------------\n")

#Définir une fonction case remplie qui renvoie en parametre "tablo, posx, posy"
def caseTab(tablo, posx, posy):
    #Si tablo[posx][posy] = '-'
    if tablo[posx][posy] == '-':
        #ALors retourner faux
        return False
    #Sinon
    else:
        #Retourner Vrai
        return True

#Définir une fonction joueurGagnantON avec pour paramètre(tablo, player)
def joueurGagnantON(tablo, player):
    #La variable win vaut none
    win = None
    #La variable esp est égale à la longueur de 'tablo'
    esp = len(tablo)

    #Pour i allant de 0 à esp-1
    for i in range(esp):
        #win est égal vrai
        win = True
        #Pour j allant de 0 à esp-1
        for j in range(esp):
            #Si tablo [i][j] different de player
            if tablo[i][j] != player:
                #Alors win est faux
                win = False
                #Stopper le programme
                break
        #Si win
        if win:
            #Alors retourner Win
            return win

    #Pour i allant de 0 à esp-1
    for i in range(esp):
        #win est vrai
        win = True
        #Pour j allant de 0 à esp-1
        for j in range(esp):
            #Si tablo [j][i] différent de player
            if tablo[j][i] != player:
                #Alors win n'est pas vrai
                win = False
                #Stopper le programme
                break
        #Si win
        if win:
            #Alors retourner win
            return win

    #win égal vrai
    win = True
    #Pour i allant de 0 à esp-1
    for i in range(esp):
        #Si tablo [i][i] différent de joueur
        if tablo[i][i] != player:
            #Alors win est faux
            win = False
            #Stopper le programme
            break
    #Si win
    if win:
        #Alors retourner win
        return win
    #win est vrai
    win = True
    #Pour i allant de 0 à esp-1
    for i in range(esp):
        #Si tablo[i][esp - 1 - i] différent de player
        if tablo[i][esp - 1 - i] != player:
            #Alors win n'est pas vrai 
            win = False
            #Stopper le programme
            break
    #Si win
    if win:
        #Alors retourner win
        return win
    #Retourner faux
    return False
def full(self, table):
        for i in range(self.size):
            for j in range(self.size):
                if table[i][j] == "*":
                    return False
        return True

#Définir la fonction morpionTab avec comme paramettre (tablo)
def morpionTab(tablo):
    #Pour ligne dans 'tablo'
    for row in tablo:
        #Pour item dans ligne
        for item in row:
            #Si item = '-'
            if item == '-':
                #Alors retourner faux
                return False
    #Retourner vrai
    return True

#Définir morpion()
def morpion():
    #Créer un tableau vierge
    global tableJeu
    #Demander à joueur 1 son pseudo
    joueur1 = input("Joueur 1, choisissez votre pseudo : \n")
    #Demander à joueur 2 son pseudo
    joueur2 = input("Joueur 2, choisissez votre pseudo : \n")
    #Joueur 1 a les croix
    joueur1coup = "X"
    #Joueur 2 à les ronds
    joueur2coup = "O"
    #Créer une fonction joueurChoix qui choisira aléatoirement le joueur qui commence
    joueurchoix = randint(1, 2)
    #Si joueurChoix = 1
    if joueurchoix == 1:
        #Alors afficher joueur 1 commence
        print(joueur1 + ", commence \n")
        #Le tour est donc pour le joueur 1
        TourJoueur = joueur1
        #Alors coup joueur est égal à joueur1coup
        CoupJoueur = joueur1coup
    #Sinon
    else:
        #Afficher joueur 2 commence
        print(joueur2 + ", commence \n")
        #Le tour est donc pour le joueur 2
        TourJoueur = joueur2
        #Alors coupJoueur = joueur2coup
        CoupJoueur = joueur2coup
    #Boncoup est égal à faux
    bonCoup = False
    #Joueur gagnant est égal à faux
    joueurGagnant = False 
    #rappeler la fonction showTable avec en parametre(tableJeu)
    showTable(tableJeu)
    #Tant que joueurgagnant est égal à faux
    while joueurGagnant == False:
        #Tant que bon coup est égal à faux
        while bonCoup == False :
            #Afficher 'Au tour de + TourJoueur + "\n"
            print("Au Tour de " + TourJoueur + "\n")
            #Prendre un élément au hasard dansX qui sera egale a int(entrer("Choisissez la ligne à modifier ( 0 ← Ligne 1 ; 1 ← Ligne 2 ; 2 ← Ligne 3)  \n"))
            choixX = int(input("Choisissez la ligne à modifier ( 0 = Ligne 1 ; 1 = Ligne 2 ; 2 = Ligne 3) : \n"))
            #Prendre un élément au hasard dansY qui sera egale a int(entrer("Choisissez la colonne à modifier ( 0 ← Colonne 1 ; 1 ← Colonne 2 ; 2 ← Colonne 3)  \n"))
            choixY = int(input("Choisissez la colonne à modifier ( 0 = Colonne 1 ; 1 = Colonne 2 ; 2 = Colonne 3) : \n"))
            #Si caseTab (tableJeu, prendre un élément au hasard dansX, prendre un élément au hasard dansY) est différent de vrai
            if caseTab(tableJeu, choixX, choixY) != True:
                #Alors tableJeu [prendre un élément au hasard dansX][prendre un élément au hasard dansY] qui sera egale au coupJoueur
                tableJeu[choixX][choixY] = CoupJoueur
                #BonCoup est égal à vrai
                bonCoup = True 
        #Rappeler la fonction showTable avec un parametre(tableJeu)
        showTable(tableJeu)
        #Si joueurgagnanton (tableJeu, coupJoueur)
        if joueurGagnantON(tableJeu, CoupJoueur):
            #Alors afficher le joueur avec son tour à gagné la partie
            print("Le joueur " + TourJoueur +  " à gagné la partie ! :) ")
            #Stopper le programme
            break
        #Si morpionTab(tableJeu)
        if morpionTab(tableJeu):
            #Alors afficher égalité
            print("Egalité ! :/")
            #Stopper le programme
            break
        #Si coup joueur est égal à joueur1coup
        if CoupJoueur == joueur1coup:
            #Alors coupjoueur = joueur2coup
            CoupJoueur = joueur2coup
            #TourJoueur = joueur2
            TourJoueur = joueur2
        #Sinon
        else :
            #CoupJoueur = joueur1coup 
            CoupJoueur = joueur1coup
            #TourJoueur = joueur 1
            TourJoueur = joueur1
        #bonCoup est égal à faux
        bonCoup = False
    
    #NewPartie renvoie un input permettant de savoir si il veulent rejouer ou non avec comme message("Voulez-vous rejouer ? oui ou non : \n")
    NewPartie = input("Voulez-vous rejouer ? oui ou non : \n")
    #Si NewPartie est éagl à oui
    if NewPartie == "oui":
        #Alors afficher "C'est reparti"
        print("C'est reparti !")
        #TableJeu est égal à [['-','-','-'],['-','-','-'],['-','-','-']]
        tableJeu = [['-','-','-'],['-','-','-'],['-','-','-']]
        #Rappeler la focntion morpion()
        morpion()
    #Sinon si NewPartie est égal à "non"
    elif NewPartie == "non":
        #Afficher "A bientôt"
        print("A bientôt !")
    #Sinon
    else: 
        NewPartie = input("Voulez-vous rejouer ? oui ou non : \n")
        if NewPartie == "oui":
            print("C'est reparti !")
            tableJeu = [['-','-','-'],['-','-','-'],['-','-','-']]
            morpion()

        elif NewPartie == "non":
            print("Au bientôt !")

        else:
            NewPartie = input("Voulez-vous rejouer ? oui ou non : \n")
            if NewPartie == "oui":
                print("C'est reparti !")
                tableJeu = [['-','-','-'],['-','-','-'],['-','-','-']]
                morpion()

            elif NewPartie == "non":
                print("Au bientôt !")
            

morpion()

