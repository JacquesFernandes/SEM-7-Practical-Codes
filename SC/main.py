'''
run with python3

formulae
di => given
lambda => given
c => given
neti = matrix_prod(w_trans, xi)
oi = (2/(1+exp((0-1)*lambda*neti)))-1
delta_wi = (0.5)*c*(di-oi)*(1-oi^2)*xi


order
for iteration i
1) neti
2) oi
3) delta_wi
4) wi+1 = wi + delta_wi
'''
from math import exp;

def get_settings():
	values = dict();
	f = open("settings.txt","r");
	lines = f.readlines();
	for line in lines:
		parts = line.split("=");
		for i in range(0,len(parts)):
			parts[i] = parts[i].strip(" ").strip("\n").split(","); #cleanup and splitting values
		key = parts[0][0];
		values[key] = list();
		for val in parts[1]:
			values[key].append(float(val));
	f.close();
	return(values);
	
def get_neti(w_trans,xi): #proper
	op = 0;
	#print("w_trans",w_trans);
	#print("xi",xi);
	for i in range(0,len(w_trans)): #since we are essentially taking the sum of products of array
		op += w_trans[i]*xi[i];
	return(op);
	
def get_oi(lmbda,net_i): #proper
	val = (0-1)*lmbda*net_i;
	op = exp(val) + 1;
	op = 2/op;
	op = op - 1;
	return(op);

def get_delta_wi(c,di,oi,xi):
	op = list();
	for x in xi:
		f_neti = (0.5)*(1-(oi**2));
		delta_wi = c * (di-oi) * f_neti *x;
		op.append(delta_wi);
	return(op);

def get_next_wi(wi,delta_wi):
	op = list();
	for i in range(0,len(wi)):
		op.append(wi[i]+delta_wi[i]);
	return(op);
	
'''MAIN'''

if __name__ == "__main__":
	values = get_settings(); #returns a dictionary of all values
	lmbda = values["lambda"][0];
	c = values["c"][0];
	num_iter = int(values["iterations"][0]);
	wi = list();
	xi = list();
	d = list();
	for i in range(1,num_iter+1):
		print(values["x"+str(i)]);
		xi.append(values["x"+str(i)]);
	wi.append(values["w1"]);
	for i in range(1,num_iter+1):
		#print(values["d"+str(i)]);
		d.append(values["d"+str(i)][0]);
	''' #MANUAL INPUT
	lmbda = float(input("Value of lambda: "));
	c = float(input("Value of c: "));
	num_iter = int(input("Number of iterations: "));
	
	d = list(); #list of values of d
	xi = list(); # list of x arrays
	wi = list(); # list of weight arrays
	
	#get values for di and xi arrays
	for i in range(1,num_iter+1):
		d.append(float(input("Enter value of d"+str(i)+" : ")));
		x_temp = input("Enter the values of x"+str(i)+" (separate using <,>): ");
		x_temp.strip(" ");
		x_temp = x_temp.split(",");
		for j in range(0,len(x_temp)):
			x_temp[j] = float(x_temp[j]);
		xi.append(x_temp);
	
	#Get the weight arrays
	w_temp = input("Enter the values of w1 (separate using <,>): ");
	w_temp.strip(" ");
	w_temp = w_temp.split(",");
	for j in range(0,len(w_temp)):
		w_temp[j] = float(w_temp[j]);
	wi.append(w_temp);
	'''
	
	#begin calculations
	for i in range(0,num_iter):
		neti = get_neti(wi[i],xi[i]);
		oi = get_oi(lmbda,neti)
		delta_wi = get_delta_wi(c,d[i],oi,xi[i]);
		next_wi = get_next_wi(wi[i],delta_wi);
		wi.append(next_wi);

	print("Weight values: ");
	for w in wi:
		print(w);
	'''
	print(" :: DEBUG ::");
	print("Values for d");
	print(d);
	print("-------------");
	print("Values for x");
	print(xi);
	print("--------------");
	print("Values for w");
	print(wi);
	'''
