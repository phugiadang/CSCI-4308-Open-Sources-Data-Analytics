import sys

def commify():
	for line in sys.stdin:
            a = line
            break
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


commify()
	


