import math;
import os;
import sys;
htend=float();#//Declaration
htend=0.000000000000001;#//initialization while htend-->0 

def derivative():
	"""
f(x)=sin x
where:
x€{Radian}
****************************************

f'(x) = lim  f(x+h)-f(x)
        h->0  ----------
                 h
****************************************
	"""
	degree=float();
	radian=float();
	fx_plus_h=float();
	fx=float();
	derivated=float();
	fx_minus=float();

	degree=float(input("\n\n[*] Enter x value (angle) :"));
	radian=((math.pi)/(180))*(degree)
	fx_plus_h=math.sin(radian+htend);
	fx=math.sin(radian);
	
	#fx_minus=fx_plus_h-fx;
	
	derivated=((fx_plus_h)-(fx))/(htend);
	print("\n\n f'(x) = lim  f(x+h)-f(x)  ");
	print("         h->0  ---------- ");
	print("                   h  ");
	
	
	
	
	print("\n\n\n f'({}) = lim  f({}+{})-f({})  ".format(degree,degree,htend,degree));
	print("            h->0     --------------- ");
	print("                        {}  ".format(htend));
	
	
	
	
	
	
	
	print("\n\n\n f'({}) = lim  {} - {}  ".format(degree,fx_plus_h,fx));
	print("            h->0     ------------------------------- ");
	print("                        \t{}  ".format(htend));
	
	
	
	
#	print("\n\n\n f'({}) = lim     {}  ".format(00));
#	print("            h->0     --------------- ");
#	print("                        \t{}  ".format(htend));
#	
#	

	print("\n\n\n f'({}) = lim    {}  ".format(degree,fx_plus_h-fx));
	print("            h->0     --------------- ");
	print("                        {}  ".format(htend));
	



	print("\n\n\n f'({}) =".format(degree),derivated);
	


















def decorate():
	print("       _")
	print("    __| |")
	print("   / _` |");
	print("  | (_| |");
	print("   \__,_|");
	print(" ____________");
	print("|____________|")
	print("     _")
	print("  __| | __  __")
	print(" / _` | \ \/ /")
	print("| (_| |  >  < ")
	print(" \__,_| /_/\_\ ");

def main():
	decorate();
	derivative();
	pass
main();
#while True:
#print(0.001/htend)