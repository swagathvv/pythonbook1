Python 3.4.0 (default, Apr 11 2014, 13:05:18) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def do_n(s,n):
	if n<=0:
		return
	print(s)
	do_n(s,n-1)

	
>>> do_n(3,5)
3
3
3
3
3
>>> do_n("hello",7)
hello
hello
hello
hello
hello
hello
hello
>>> 
