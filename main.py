# TicTacToe game in python by JustJeeCode.

import os
import time

class Board:
	def __init__(self):
		self.row_1 = ['□','□','□']
		self.row_2 = ['□','□','□']
		self.row_3 = ['□','□','□']
		self.board = [self.row_1, 
					  self.row_2,
					  self.row_3]

	def display(self):
		# Displays board
		print("  Y Y Y")
		for row in self.board:
			print("X",end=" ")
			for cell in row:
				print(cell, end=" ")
			print("\n",end="")
		print()

	def update(self, player, x, y):
		self.player = player
		self.x = x
		self.y = y

		if player == 'Player 1':
			self.cell_value = 'o'
		else:
			self.cell_value = 'x'

		# If the mark can be made
		if x > 3 or y > 3:
			return "Coordinates too big, try again."
		elif x < 1 or y < 1:
			return "Coordinates too small, try again."
		elif self.board[x-1][y-1] == 'o':
			return "Mark already there, try again."
		elif self.board[x-1][y-1] == 'x':
			return "Mark already there, try again."
		else:
			self.board[x-1][y-1] = self.cell_value
			return True

	def check(self):
		self.cell_count = 0

		# Stalemate check
		for row in self.board:
			for cell in row:
				if cell == 'o' or cell == 'x':
					self.cell_count += 1
		if self.cell_count == 9:
			return 'Stalemate'

		# Hor checks
		if self.board[0][0] == self.cell_value and self.board[0][1] == self.cell_value and self.board[0][2] == self.cell_value:
			return self.cell_value
		elif self.board[1][0] == self.cell_value and self.board[1][1] == self.cell_value and self.board[1][2] == self.cell_value:
			return self.cell_value
		elif self.board[2][0] == self.cell_value and self.board[2][1] == self.cell_value and self.board[2][2] == self.cell_value:
			return self.cell_value

		# Ver checks
		if self.board[0][0] == self.cell_value and self.board[1][0] == self.cell_value and self.board[2][0] == self.cell_value:
			return self.cell_value
		elif self.board[0][1] == self.cell_value and self.board[1][1] == self.cell_value and self.board[2][1] == self.cell_value:
			return self.cell_value
		elif self.board[0][2] == self.cell_value and self.board[1][2] == self.cell_value and self.board[2][2] == self.cell_value:
			return self.cell_value

		# Diag checks
		if self.board[0][0] == self.cell_value and self.board[1][1] == self.cell_value and self.board[2][2] == self.cell_value:
			return self.cell_value
		elif self.board[0][2] == self.cell_value and self.board[1][1] == self.cell_value and self.board[2][0] == self.cell_value:
			return self.cell_value
		else:
			return 'Continue'

# Start msg
def start_msg():
	print()
	print(r"___________.__     ___________           ___________            ")
	print(r"\__    ___/|__| ___\__    ___/____    ___\__    ___/___   ____  ")
	print(r"  |    |   |  |/ ___\|    |  \__  \ _/ ___\|    | /  _ \_/ __ \ ")
	print(r"  |    |   |  \  \___|    |   / __ \\  \___|    |(  <_> )  ___/ ")
	print(r"  |____|   |__|\___  >____|  (____  /\___  >____| \____/ \___  >")
	print(r"                   \/             \/     \/                  \/ ")

	time.sleep(1)
	print("\nBy JustJeeCode.")
	time.sleep(1)
	print("\nPress [ENTER] to start.")
	input()
	os.system(clear)

# Variables
board = Board()
player_turn = 1
clear = 'clear' # if windowns change to 'cls'

# Start msg
os.system(clear)
start_msg()

# Game loop
while True:
	board.display()
	# Player 1
	if player_turn == 1:
		print("Player 1's turn.\nPlease select a cell.")
		
		# try the inputs
		try:
			x = int(input("X: "))
			y = int(input("Y: "))
		except:
			os.system(clear)
			print("Please enter a number, try again.\n")
			continue

		# update board
		if board.update('Player 1', x, y) == True:
			pass
		else:
			os.system(clear)
			print(board.update('Player 1', x, y) + "\n")
			continue

		# check board
		if board.check() == 'o':
			os.system(clear)
			board.display()
			print("Player 1, wins!\n")
			break
		elif board.check() == 'Stalemate':
			os.system(clear)
			board.display()
			print("Stalemate.\n")
			break
		else:
			os.system(clear)
			player_turn = 2
	# Player 2
	else:
		print("Player 2's turn.\nPlease select a cell.")
		
		# try the inputs
		try:
			x = int(input("X: "))
			y = int(input("Y: "))
		except:
			os.system(clear)
			print("Please enter a number, try again.\n")
			continue

		# update board
		if board.update('Player 2', x, y) == True:
			pass
		else:
			os.system(clear)
			print(board.update('Player 2', x, y) + "\n")
			continue

		# check board
		if board.check() == 'x':
			os.system(clear)
			board.display()
			print("Player 2, wins!\n")
			break
		elif board.check() == 'Stalemate':
			os.system(clear)
			board.display()
			print("Stalemate.\n")
			break
		else:
			os.system(clear)
			player_turn = 1
