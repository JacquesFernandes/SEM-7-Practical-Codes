import threading;

solutions = list();
comp_threads = int();
loc_rowcol_dict = dict();
class Board:
	
	def __init__(self,size):
		global loc_rowcol_dict;
		self.n = size;
		self.board = list(list(0 for i in range(0,self.n)) for i in range(0,self.n));
		if len(loc_rowcol_dict.keys()) == 0:
			print("Generating loc_rowcol_dict");
			self.gen_loc_rc_dict(self.n);
			print(loc_rowcol_dict);
		return;
	
	def gen_loc_rc_dict(self,n):
		global loc_rowcol_dict;
		for row in range(0,n):
			for col in range(0,n):
				i = (row*n)+col;
				loc_rowcol_dict[str(i)] = {"row":row,"col":col};
	
	def display(self):
		string = "";
		for i in range(0,self.n):
			for j in range(0,self.n):
				print(self.board[i][j],end=" ");
			print("");
		return;
	
	def translate_loc_rowcol(self,loc):
		global loc_rowcol_dict;
		loc = str(loc);
		c = loc_rowcol_dict[loc];
		return(c["row"],c["col"]);
	
	def translate_loc_rowcol0(self,loc):
		row = 1;
		col = 1;
		if loc >= 0 and loc <= 2:
			row = 0;
		elif loc >= 3 and loc <= 5:
			row = 1;
		elif loc >= 6 and loc <= 8:
			row = 2;
		
		l1 = list(self.n*i for i in range(0,self.n));
		l2 = list(self.n*i for i in l1);
		#for i in range(0,self.n):
		#	l1.append(self.n*i);
			
		if loc in l1:
			col = 0;
		elif loc in [1,4,7]:
			col = 1;
		elif loc in [2,5,8]:
			col = 2;
		return(row,col);
	
	def set_loc(self,x,y=None):
		if y is None: #loc is given, not x and y
			x,y = self.translate_loc_rowcol(x);
			#print("X : "+str(x)+" Y : "+str(y));
		self.board[x][y] = 1;
		return;
	
	def check_loc(self,loc):
		row,col = self.translate_loc_rowcol(loc);
		if self.board[row][col] == 1:
			return(True); #Occupied
		else:
			return(False); #Free
			
class SolutionThread(threading.Thread):
	
	def __init__(self,position,size):
		threading.Thread.__init__(self);
		self.board = Board(size);
		#self.say(self.board);
		self.s_loc = position; #position of first queen
		self.locations = list();
		self.size = size;
		return;
	
	def run(self):
		global solutions;
		global comp_threads;
		self.board.set_loc(self.s_loc);
		self.locations.append(self.s_loc);
		cpos = self.s_loc; #current position
		n = self.size;
		clear_flag = False;
		for i in range(cpos,n**2):
			for set_loc in self.locations:
				slr, slc = self.board.translate_loc_rowcol(set_loc); #location which is already set
				ir, ic = self.board.translate_loc_rowcol(i); #location being tested
				dr = slr-ir;
				dc = slc-ic;
				if dr != 0 and dr != -0 and dc != 0 and dc != -0 and dr != dc and dr != -dc:
					clear_flag = True;
				else:
					clear_flag = False;
			if clear_flag:
				self.board.set_loc(i);
				self.locations.append(i);
			#self.say("Current board at end of round "+str(i)+":");
			if len(self.locations) == n**(1/2):
				
				self.board.display();
		return;
		'''
					self.say("dr == 0 for "+str(dr)+" @ "+str(i));
					return(False);
				elif dc == 0:
					self.say("dc == 0 for "+str(dr)+" @ "+str(i));
					return(False);
				elif dr == dc:
					self.say("dr == dc for "+str(dr)+" @ "+str(i));
					return(False);
				else:
					return(True);
		
		for i in range(0,n**2):
			if self.check_state(i) == True:
				self.board.set_loc(i);
				self.locations.append(i);
				#self.say(self.locations);
				self.board.display();
			else:
				#self.say("check failed for: "+str(i)+"\n");
				pass;
			self.say("Pass "+str(i)+" completed");
		solutions.append(self.locations);
		comp_threads+=1;
		return;
		'''
	
	def say(self,msg):
		print(self.name+" : "+str(msg));
		return;
	
	def check_state(self,loc):
		loc=int(loc);
		lr,lc = self.board.translate_loc_rowcol(loc);
		
		#self.say("checking "+str(row)+","+str(col));
		temp_board = self.board.board;
		n = len(temp_board[0]);
		self.say("----");
		#re try
		for i in range(0,n**2):
			if self.board.check_loc(i) == True:
				tr,tc = self.board.translate_loc_rowcol(i);
				dr = lr-tr;
				dc = lc-tc;
				if dr == 0:
					self.say("dr == 0 for "+str(dr)+" @ "+str(loc));
					return(False);
				elif dc == 0:
					self.say("dc == 0 for "+str(dr)+" @ "+str(loc));
					return(False);
				elif dr == dc:
					self.say("dr == dc for "+str(dr)+" @ "+str(loc));
					return(False);
				else:
					return(True);	
		'''
		#check vertical
		for i in range(0,n):
			#elf.say("row -> "+str(i));
			if temp_board[i][col] == 1:
				self.say("Vertical hit at "+str(i)+","+str(col)+" from "+str(loc));
				return(False);
				
		#check horizontal
		for i in range(0,n):
			if temp_board[row][i] == 1:
				self.say("Horizontal hit at "+str(row)+","+str(i)+" from "+str(loc));
				return(False);
				
		#check right-diagonal
		#up
		i = 1;
		while (loc-(n+1)*i) >= 0:
			t = (loc-(n+1)*i);
			tr,tc = self.board.translate_loc_rowcol(t);
			print("loc:",loc,"n",n,"n",i,"t",t);
			if self.board.check_loc(t) == True:
				self.say("up-right diagonal hit at "+str(i)+","+str(col)+" from "+str(loc));
				return(False);
			i+=1;

		#down
		i = 1;
		while (loc+(n+1)*i) <= (n**2)-1:
			t = (loc+(n+1)*i);
			if self.board.check_loc(t) == True:
				self.say("down-right diagonal hit at "+str(i)+","+str(col)+" from "+str(loc));
				return(False);
			i+=1;
		
		#check left-diagonal
		#up
		i = 1;
		while (loc-(n-1)*i) >= 0:
			t = (loc-(n-1)*i);
			if self.board.check_loc(t) == True:
				self.say("up-left diagonal hit at "+str(i)+","+str(col)+" from "+str(t));
				return(False);
			i+=1;
		
		#down
		i = 1;
		while (loc+(n-1)*i) <= (n**2)-1:
			t = (loc+(n-1)*i);
			if self.board.check_loc(t) == True:
				self.say("down-left diagonal hit at "+str(i)+","+str(col)+" from "+str(t));
				return(False);
			i+=1;
		#self.say("...");
		#all tests passed
		self.say("Passed w/ "+str(loc));
		return(True);
		'''

def NQueen():
	global solutions;
	global comp_threads;
	threads = list();
	size = int(input("Number of Queens: "));
	for i in range(0,size**2):
		st = SolutionThread(i,size);
		st.start();
		st.join();
		threads.append(st);
	'''
	while comp_threads != len(threads):
		pass;
	'''
	
	print("Done!");
	print(solutions);
	
if __name__ == "__main__":
	NQueen();
