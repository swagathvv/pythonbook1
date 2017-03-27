Python 3.4.0 (default, Apr 11 2014, 13:05:18) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def do_twice(f):
	f()
	f()

	
>>> def print_spam():
	print("spam")

>>> do_twice(print_spam)
spam
spam
>>> 

>>> #2
>>> def do_twice(f,x):
	f(x)
	f(x)

	
>>> def print_twice(name):
	print(name)
	print(name)

	
>>> do_twice(print_twice,"spam")
spam
spam
spam
spam
>>> 

>>> def do_four(f,x):
	f(x)
	f(x)
	f(x)
	f(x)

	
>>> do_four(print_twice,"spam")
spam
spam
spam
spam
spam
spam
spam
spam
>>> 
