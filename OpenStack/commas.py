import sys

def commify():
	a = sys.argv[1]
	b=''
	for x in range(1,len(a)+1):
	    if (x %3 == 0):
	        if (x != len(a)):
	            b = ','+a[len(a)-x]+b
	        else:
	            b = a[len(a)-x]+b
	    else:
	        b = a[len(a)-x]+b
	print b



	


