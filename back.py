from random import randint

grid = [] # With this method, this variable will be accessible everywhere.
def error(message):
	"""
		Display an agreable error.
	"""
	assert message != "", "message is empty"
	text = f"Error : {message}"
	return text
assert error('Coucou Milan !') == 'Error : Coucou Milan !'

def createEmptyGrid(size):
	"""
		The grid is a square.
		size define width/height of the grid.
		size must be between 3 and 15.
	"""
	assert type(size) is int, "type of size must be int"
	assert size > 2, "the size of the grid is too small"
	assert size < 16, "the size of the grid is too big"
	grid = [[0 for x in range(size)] for y in range(size)]
	return grid
assert createEmptyGrid(3) == [[0,0,0],[0,0,0],[0,0,0]]

def displayGrid(grid,view):
	"""
		Displays the grid with command-line style.
		view displays only ships which player should be able to see.
	"""
	assert type(grid) is list, "type of grid must be list"
	assert type(view) is int, "type of view must be int"
	legendTop = ""
	for i in range(len(grid)):
		legendTop = legendTop + str(i) + " "
	print('-',end=" ")
	print(legendTop)
	for x in range(len(grid)):
		print(x,end=" ")
		for y in range(len(grid)):
			if view == None:
				# All ships
				print(f"{grid[x][y]}",end=" ")
			elif grid[x][y] == view:
				# Only own ships
				print("X",end=" ")
			elif grid[x][y] != view:
				# Opposite ships or empty places
				print("-",end=" ")
			else:
				print(error("view must be an user identifiant (1 or 2)"))
				exit()
		print()
	print()

def prepareGrid(size,nbShips):
	"""
		Creates an empty grid, then put ships on the grid.
		size is the width/height of the grid.
		nbShips is the number of ships per player.
	"""
	assert type(size) is int, "type of size must be int"
	assert type(nbShips) is int, "type of nbShips must be int"
	assert (nbShips*2)/(size**2) < 0.7, "there are too many ships"
	assert (nbShips*2)/(size**2) > 0.1, "there is not enough ships"
	grid = createEmptyGrid(size)
	for player in range(1,3):
		ships = 0
		while ships < nbShips:
			x = randint(0,size-1)
			y = randint(0,size-1)
			if grid[x][y] == 0:
				# If this place is not already taken
				grid[x][y] = player
				ships += 1
	return grid

def shipHere(grid,player,position,ships):
	"""
		player is 1 or 2 according to user identifiant (who call this function)
		position is a tuple. First is x (left - right), and second is y (top - bottom)
		Remember in Python, lists start from 0. So remember to move 1 from the position !
	"""
	assert type(grid) is list, "type of grid must be list"
	assert type(player) is int, "type of player must be int"
	assert type(position) is tuple, "type of position must be tuple"
	assert type(ships) is list, "type of ships must be list"
	x = position[0] # left - right
	y = position[1] # top - bottom
	if (grid[x][y] != player) and (grid[x][y] != 0):
		# Remind that opposite player loose a ship !
		if player == 1:
			ships[1] -= 1
		elif player == 2:
			ships[0] -= 1
		else:
			print(error("player must be 1 or 2."))
			exit()
		print("You have destoyed an opposite ship.")
	elif grid[x][y] == player:
		ships[player-1] -= 1
		print("You have destoyed one of your own ships.")
	elif grid[x][y] == 0:
		print("You have not destoyed anything.")
	else:
		print(error("A value in grid is incorrect. Must be 0 or 1 or 2. "))
		exit()
	return ships

def shoot(size):
	"""
		Shoot somewhere
		Player write his shoot's position. X is left-right and Y is top-bottom.
		size is the width/height of the grid. This function use the size to know if the user's input is correct.
	"""
	assert type(size) is int, "type of size must be int"
	inputCorrect = False
	while not(inputCorrect):
		x = int(input("x (left - right) : "))
		y = int(input("y (top - bottom) : "))
		if (x+1 > size) or (y+1 > size) or (x < 0) or (y < 0):
			print("Position is out of the grid.")
		else:
			inputCorrect = True
	print()
	return (x,y)

def autoshot(size):
	assert type(size) is int, "type of size must be int"
	posx = randint(0,size)
	posy = randint(0,size)
	print()
	return (x,y)


def destroyShip(grid,position):
	"""
		Remove a ship from the grid
	"""
	assert type(grid) is list, "type of grid must be list"
	assert type(position) is tuple, "type of position must be tuple"
	x = position[0]
	y = position[1]
	grid[x][y] = 0
	return grid

def changePlayer(player):
	"""
		Reverse the player id.
	"""
	assert type(player) is int, "type of player must be int"
	if player == 1:
		player = 2
	elif player == 2:
		player = 1
	else:
		print(error("player must be 1 or 2"))
		exit()
	return player

def someoneWon(ships):
	"""
		Stop the game if someone has won.
	"""
	if 0 in ships:
		player = ships.index(0)
		player += 1
		player = changePlayer(player)
		print(f"Player {player} won !")
		exit()

def run():
	"""
		This function represents a entire game.
	"""
	choose = False
	if choose:
		size = int(input("How size for the grid : "))
		nbShips = int(input("How many ships per player : "))
	else:
		size = int(10)
		nbShips = int(10)
	ships = [nbShips for player in range(2)] # Give ships to players
	grid = prepareGrid(size,nbShips)
	player = randint(1,2) # Player who begin first
	while True:
		# This while bucle represents a round
		print(f"Player {player} is going to play. \n")
		displayGrid(grid,player)
		position = autoshoot(size)
		ships = shipHere(grid,player,position,ships)
		grid = destroyShip(grid,position)
		someoneWon(ships)
		player = changePlayer(player)
