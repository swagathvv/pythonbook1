Python 2.7.6 (default, Mar 22 2014, 22:59:38) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> def square(t,length):
	for i in range(4):
		fd(t,length)
		lt(t)

		
>>> def polyine(t,n,length,angle):
	for i in range(n):
		fd(t,length)
		lt(t,angle)

		
>>> def polygon(t,n,length):
	angle=360/n
	polyine(t,n,length,angle)

	
>>> def arc(t,r,angle):
	import math
	arc_length= 2*math.pi*r* abs(angle)/360
	n=int(arc_length/4)+1
	step_length=arc_length/n
	step_angle=float(angle)/n

	
>>> def circle(t,r)
SyntaxError: invalid syntax
>>> def circle(t,r):
	arc(t,r,360)

	
>>> from polygon import*

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    from polygon import*
ImportError: No module named polygon
>>> def petal(t,r,angle):
	for i in range(2):
		arc(t,r,angle)
		lt(t,180-angle)

		
>>> def flower(t,n,r,angle):
	for i in range(n):
		petal(t,r,angle)
		lt(t,360/n)

		
>>> def move(t,length):
	pu(t)
	fd(t,length)
	pd(t)

	
>>> from swampy.TurtleWorld import*
>>> world = TurtleWorld()
>>> bob = Turtle()
>>> bob.delay=0.01
>>> move(bob,-100)
>>> flower(bob,7,60,60)
>>> move(bob,100)
>>> flower(bob,10,40,80)
>>> move(bob,100)
>>> flower(bob,20,140,20)
>>> die(bob)
>>> 
