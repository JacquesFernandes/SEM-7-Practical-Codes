import random;
import threading;

poss_moves = list();

class ScenarioThread(threading.Thread):
	
	def __init__(self,history,game):
		threading.Thread.__init__(self);
		self.last = history.copy().pop();
		self.human_history = history;
		self.game = game;
		self.free_spaces = free_spaces;
	
	def run(self):
		global poss_moves;
		anticipate
	
	def preempt(self):
		poss = list();
		for move in self.human_history():
			if move == 5: #center
				pass;
			if move in [1,3,7,9]: #corners
				
				pass;
			
	
	def anticipate(self): #return list of possible moves
		game_grid = self.game.get_grid();
		possible_loss = list(); #places which could let player win
		for space in self.free_spaces:
			fs_x, fs_y = self.grid.translate_loc_xy(space);
			north = bool(); #up
			south = bool(); #down
			east = bool(); #right
			west = bool(); #left
			north_west = bool();
			north_east = bool();
			south_west = bool();
			south_east = bool();
			
			if self.grid.check_loc(space+3) != False: #space below is unoccupied
				north = True;
			if self.grid.check_loc(space-3) != False: #space above is unoccupied
				south = True;
			if self.grid.check_loc(space+1) != False: #space right is unoccupied
				east = True;
			if self.grid.check_loc(space-1) != False: #space left is unoccupied
				west = True;
			
			if north and south and east and west:
				pass;
		return;

class Memory:
	def __init__(self,game):
		self.store = dict();
		self.rno = 0; #round number
		self.free_spaces = list(i*1 for i in range(1,10));
		self.possible_loss = list(); #list of possible loss places
		self.human_history = list();
		self.last_game = None;
		self.new_game = game;
	
	def get_free_spaces(self):
		board = self.grid;
		for i in range(1,10):
			if board.check_loc(i) == False and i in self.free_spaces:
				self.free_spaces.remove(i);
				self.human_history.append(i);
		return(self.free_spaces);
	
	def set_memory(self,game):
		self.rno += 1;
		self.last_game = self.new_grid;
		self.new_game = game;
	
	def get_human_history(self):
		return(self.human_history);
		

class Bot:
	
	def __init__(self, verbose=False, grid):
		self.verbose = verbose;
		self.grid = None;
		self.rand_no_gen = random.Random();
		self.memory = Memory(grid); # memory for the bot
		self.say("Ready!");
		return;
	
	def rng(self,mx=1): #random number generator
		return(int(self.rand_no_gen.random()*mx));
	
	def say(self,message):
		if self.verbose:
			print("BOT :: "+str(message));
		return;
	
	def get_latest_move(self):
		mem = self.memory();
		
	
	def act_on(self,game):
		self.memory.init_memory(game);
		history = self.get_human_history();
		last = history.copy().pop();
		for move in history:
			st = ScenarioThread(history,game);
			st.join();
		self.say("Finished analysis... I have predicted all your moves >:)");


if __name__ == "__main__":
	print("bot...");
