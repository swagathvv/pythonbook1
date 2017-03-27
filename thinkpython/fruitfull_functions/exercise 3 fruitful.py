Python 3.4.0 (default, Apr 11 2014, 13:05:18) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def is_between(x,y,z):
	if x<=y:
		print('true')
	elif x<=z:
		print('true')
	elif y<=z:
                print('true')
        else:
                print('false')
	
