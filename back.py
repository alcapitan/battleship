from random import randint

table = [[0 for j in range(10)] for i in range(10)]

def displayTable(table):
    for i in range(len(table)):
        print(table[i])
    print()

def putBoatRandomly(table):
    for player in range(1,3):
        boatNb = 0
        while boatNb < 10:
            x = randint(0,9)
            y = randint(0,9)
            if table[x][y] == 0:
                table[x][y] = player
                boatNb += 1
    return table

putBoatRandomly(table) # Put
displayTable(table) # Start

def boatHere(table,player,x,y):
    # player est l'identifiant (1 ou 2) de celui qui envoie la fonction (= celui qui joue lz tour)
    if (table[x][y] != player) and (table[x][y] != 0):
        print("Joueur adverse.")
    elif table[x][y] == player:
        print("But contre son camp.")
    elif table[x][y] == 0:
         print("Mer.")
    else:
         print("Error.")

boatHere(table,1,8,4)