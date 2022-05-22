from random import randint

def createEmptyTable(size):
     """The table is a square."""
     size = int(size)
     table = [[0 for x in range(size)] for y in range(size)]
     return table

def displayTable(table,view):
     """
          Display the table in command-line mode.
          View option displays boats that one player should be able to see.
     """
     for y in range(len(table)):
          for x in range(len(table)):
               if view == None:
                    print(f"{table[y][x]} ")
               elif table[y][x] == view:
                    print(f"{view} ")
               elif table[y][x] != view:
                    print("0 ")
               else:
                    return None
     print()

def prepareTable(size,nbBoats):
     """Create an empty table, then put boats on the table."""
     table = createEmptyTable(size)
     nbBoats = int(nbBoats)
     for player in range(1,3):
          boats = 0
          while boats < nbBoats:
               x = randint(0,nbBoats-1)
               y = randint(0,nbBoats-1)
               if table[x][y] == 0:
                    table[x][y] = player
                    boats += 1
     return table

def boatHere(table,player,position):
     """
          table is table of the play
          player is 1 or 2 according to user identifiant (who call this function)
          position is a tuple. First is x (left - right), and second is y (top - bottom)
          Remember in Python, lists start from 0. So remember to move 1 from the position !
     """
     x = position[0]
     y = position[1]
     if (table[y][x] != player) and (table[y][x] != 0):
          return "opposite"
     elif table[y][x] == player:
          return "same"
     elif table[y][x] == 0:
          return "empty"
     else:
          return None

def shoot():
     """Shoot on a position"""
     x = input("x : ")
     y = input("y : ")
     return (x,y)

def destroyBoat(table,player,x,y):
     """Remove a opposite boat"""
     if boatHere(table,player,x,y) == "opposite":
          table[x][y] = 0
          return "success"
     else:
          return "error"

def someoneWon(boats):
     """Return if someone won, if it's yes, so return who"""
     if 0 in boats:
          who = boats.index(0)
          return who
     else:
          return None

def run():
     size = input("How size for the grid : ")
     nbBoats = input("How many boats per player : ")
     boats = [nbBoats for player in range(2)]
     gameRun = True
     table = prepareTable(size,nbBoats)
     player = randint(0,1)
     while gameRun:
          print(f"Player {player} is going to play.")
          displayTable(table,player)
          position = shoot()
          outcome = boatHere(table,player,position)
          if outcome == "opposite":
               if player == 0:
                    boats[1] -= 1
               elif player == 1:
                    boats[0] -= 1
               else:
                    return None
               print("You have destoyed an opposite boat.")
          elif outcome == "same":
               boats[view] -= 1
               print("You have destoyed one of your own boats.")
          elif outcome == "empty":
               print("You have not destoyed anything.")
     result = someoneWon(boats)
     if result == None:
          pass
     elif type(result) == "int":
          print(f"Player {result} won !")
          gameRun = False
          return

run()