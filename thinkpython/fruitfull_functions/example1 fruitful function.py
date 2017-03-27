Python 3.4.0 (default, Apr 11 2014, 13:05:18) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def func(x,y):
	if x>y:
		return 1
	elif x==y:
		return 0
	else:
		return -1

	
>>> func(3,3)
0
>>> func(3,2)
1
>>> func(2,3)
-1
>>> 
