Python 2.7.6 (default, Mar 22 2014, 22:59:38) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from swampy.TurtleWorld import*
>>> world = TurtleWorld()
>>> bob = Turtle()
>>> def draw(t,length,n):
	if n==0:
		return
	angle=50
	fd(t,length*n)
	lt(t,angle)
	draw(t,length,n-1)
	rt(t,2*angle)
	draw(t,length,n-1)
	lt(t,angle)
	bk(t,length*n)

	
>>> drwa(bob,120,3)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    drwa(bob,120,3)
NameError: name 'drwa' is not defined
>>> draw(bob,15,3)
>>> 
