Python 3.4.0 (default, Apr 11 2014, 13:05:18) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def hypotenuse(a,b):
	x= a**2
	y= b**2
	print("x is",x)
	print("y is ",y)

	
>>> hypotenuse(2,3)
x is 4
y is  9
>>> def hypotenuse(a,b):
	x= a**2
	y= b**2
	hypo=x+y
	print("hypo is",hypo)
	return 0.0

>>> hypotenuse(2,3)
hypo is 13
0.0
>>> def hypotenuse(a,b):
	x=a**2
	y=b**2
	hypo=x+y
	result= math.sqrt(hypo)
	return result

>>> import math
>>> hypotenuse(2,3)
3.605551275463989
>>> 
