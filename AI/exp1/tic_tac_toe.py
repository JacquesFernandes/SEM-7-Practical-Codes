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
	
	def get_occupied_list(self):
		ret = list();
		for i in range(1,10):
			if self.check_loc(i) == False:
				ret.append(i);
		return(ret);
	
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
			return;
		if grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] and grid[1][0] != " ": #horizontal match row 1
			print(grid[1][0]+" Wins!");
			self.finished = True;
			return;
		if grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] and grid[2][0] != " ": #horizontal match row 2
			print(grid[2][0]+" Wins!");
			self.finished = True;
			return;
		if grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] and grid[0][0] != " ": #vertical match column 0
			print(grid[0][0]+" Wins!");
			self.finished = True;
			return;
		if grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] and grid[0][1] != " ": #vertical match column 1
			print(grid[0][1]+" Wins!");
			self.finished = True;
			return;
		if grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] and grid[0][2] != " ": #vertical match column 2
			print(grid[0][2]+" Wins!");
			self.finished = True;
			return;
		if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != " ": #top-left diagonal match
			print(grid[0][0]+" Wins!");
			self.finished = True;
			return;
		if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] != " ": #top-left diagonal match
			print(grid[0][2]+" Wins!");
			self.finished = True;
			return;
		
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
			return;
		
		
	def going(self):
		self.check_state();
		if self.finished:
			return(False); #end game loop
		else:
			return(True); #continue game loop
	
	def translate_loc_xy(self,loc):
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
			else:
				return(False);
			return(x,y);
	
	def translate_xy_loc(self,x,y):
		x = int(x);
		y = int(y);
		loc = int();
		if x >= 0 and x <=2 and y >= 0 and y <= 2:
			if x == 0 and y = 0:
				loc = 1;
			elif x == 0 and y = 1:
				loc = 2;
			elif x = 0 and y = 2:
				loc = 3;
			elif x = 1 and y = 0:
				loc = 4;
			elif x = 1 and y = 1:
				loc = 5;
			elif x = 1 and y = 2:
				loc = 6;
			elif x = 2 and y = 0:
				loc = 7;
			elif x = 2 and y = 1:
				loc = 8;
			elif x = 2 and y = 2:
				loc = 9;
			else:
				return(False);
			return(loc);
	
	def check_loc(self,loc):
		loc = translate(loc);
		if loc == False:
			return(False);
		x = loc[0];
		y = loc[1];
		if self.grid[x][y] == " ": 
			return(loc); #unoccupied
		else:
			return(False); #occupied
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
	bot = game_bot.Bot(verbose=True);
	
	game = Grid();
	game.sample_display();		
	print("Input format for location: enter the number corresponding to that cell...");
	print("Player -> X");
	print("Bot -> O");
	
	ran = random.Random();
	toss = int(ran.random()*10);
	turn = "";
	if toss%2 == 0:
		print("Player goes first");
		turn = "player";
	else:
		print("Bot goes first");
		turn = "bot";
	
	try:
		while game.going() == True:
			
			#first move of round
			game.display();
			
			if turn == "bot":
				print("Bot Turn...");
				loc = bot.act_on(game);
				x,y = game.translate_loc_xy(loc);
				game.set_loc(x,y,"O");
				turn = "player";
			elif turn == "player":
				c_loc = False;
				while c_loc is False:
					loc = input("Player (X) : ");
					c_loc = game.check_loc(loc);
				game.set_loc(c_loc[0],c_loc[1],"X");
				turn = "bot";

			if game.going() == False:
				game.display();
				exit();
			'''	
			#second move of round
			game.display();
			
			if first == "player":
				print("Bot Turn...");
				bot.see_grid(game);
				pass;
			elif first == "bot":
				c_loc = False;
				while c_loc is False:
					loc = input("Player (X) : ");
					c_loc = game.check(loc);
				game.set_loc(c_loc[0],c_loc[1],"X");
				pass;
			'''
				
	except KeyboardInterrupt:
		print("\n\nGame force quit...");
		exit();
