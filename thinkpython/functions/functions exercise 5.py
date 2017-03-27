Python 3.4.0 (default, Apr 11 2014, 13:05:18) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def do_four(f):
	f()
	f()
	f()
	f()

>>> def beam():
	print("+ - - - - + - - - - +")

	
>>> def post():
	print("|         |         |")

	
>>> def grid():
	beam()
	do_four(post)
	beam()
	do_four(post)
	beam()

	
>>> grid()
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
>>> 
