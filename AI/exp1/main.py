'''
Main module for Tic Tac Toe game
'''
import os;
import bot as game_bot;
import random;

class Grid:
	
	def __init__(self):
		self.grid = list(list(" " for i in range(3)) for i in range(3)); #grid
		self.finished = False;
	
	def get_grid(self):
		return(self.grid);
	
	def display(self):
		for row in self.grid:
			for column in row:
				print("|"+column+"|",end="");
			print("");
	
	def set_loc(self,row,col,value):
		self.grid[row][col] = value;
		self.check_state();
		
	def check_state(self):
		grid = self.grid;
		if grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] and grid[0][0] != " ": #horizontal match row 0
			print(grid[0][0]+" Wins!");
			self.finished = True;
		if grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] and grid[1][0] != " ": #horizontal match row 1
			print(grid[1][0]+" Wins!");
			self.finished = True;
		if grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] and grid[2][0] != " ": #horizontal match row 2
			print(grid[2][0]+" Wins!");
			self.finished = True;
		if grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] and grid[0][0] != " ": #vertical match column 0
			print(grid[0][0]+" Wins!");
			self.finished = True;
		if grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] and grid[0][1] != " ": #vertical match column 1
			print(grid[0][1]+" Wins!");
			self.finished = True;
		if grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] and grid[0][2] != " ": #vertical match column 2
			print(grid[0][2]+" Wins!");
			self.finished = True;
		if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != " ": #top-left diagonal match
			print(grid[0][0]+" Wins!");
			self.finished = True;
		if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] != " ": #top-left diagonal match
			print(grid[0][2]+" Wins!");
			self.finished = True;
		
		all_filled = 0;
		for i in range(0,3):
			for j in range(0,3):
				if grid[i][j] != " ":
					all_filled += 1;
				if grid[i][j] == " ":
					all_filled = 0;
		
		if all_filled is 9:
			self.finished = True;
		else:
			self.finished = False;
		
		
	def going(self):
		if self.finished:
			return(False); #end game loop
		else:
			return(True); #continue game loop

	def check(self,loc):
		loc = int(loc);
		if loc >= 1 and loc <= 9:
			x = 0;
			y = 0;
			if loc is 1:
				x = 0;
				y = 0;
			elif loc is 2:
				x = 0;
				y = 1;
			elif loc is 3:
				x = 0;
				y = 2;
			elif loc is 4:
				x = 1;
				y = 0;
			elif loc is 5:
				x = 1;
				y = 1;
			elif loc is 6:
				x = 1;
				y = 2;
			elif loc is 7:
				x = 2;
				y = 0;
			elif loc is 8:
				x = 2;
				y = 1;
			elif loc is 9:
				x = 2;
				y = 2;
			if self.grid[x][y] == " ":
				return(x,y);
			else:
				return(False);
		else:
			return(False);
		'''
		if x <= 2 and x >= 0 and y <= 2 and y >= 0 and self.grid[x][y] == " ":
			return(x,y);
		else:
			return(False);
		'''
	def sample_display(self):
		sample_grid = list(list(" " for i in range(3)) for i in range(3)); #grid
		counter = 1;
		for row in sample_grid:
				for column in row:
					print("|"+str(counter)+"|",end="");
					counter += 1;
				print("");


'''MAIN'''	
if __name__ == "__main__":
	#vars
	bot_enable = False;
	bot = None;
	
	
	game = Grid();
	game.sample_display();		
	print("Input format for location: enter the number corresponding to that cell...");
	print("Player 1 -> X");
	print("Player 2 as bot or player?");
	choice = input("-> ");
	if choice == "bot":
		bot_enable=True;
		bot = game_bot.Bot();
	
	ran = random.Random();
	toss = int(ran.random()*10);
	if toss%2 == 0:
		print("Player goes first");
	else:
		print("Bot goes first");
		
	print("Player 2 -> O");
	try:
		while game.going():
			game.display();
			#Player 1
			#loc = input("Player 1 (X) : ");
			c_loc = False;
			while c_loc is False:
				loc = input("Player 1 (X) : ");
				c_loc = game.check(loc);
			game.set_loc(c_loc[0],c_loc[1],"X");
			#os.system("clear");
			game.display();
			#Now, player 2
			#loc = input("Player 2 (O) : ");
			if bot_enable == False:
				c_loc = False;
				while c_loc is False:
					loc = input("Player 2 (O) : ");
					c_loc = game.check(loc);
				game.set_loc(c_loc[0],c_loc[1],"O");
			else: #bot section
				print("Bot Turn...");
				bot.see_grid(game);
	except KeyboardInterrupt:
		print("\n\nGame force quit...");
		exit();
