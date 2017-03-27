Python 2.7.6 (default, Mar 22 2014, 22:59:38) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> def draw_pie(t,n,r):
	polypie(t,n,r)
	pu(t)
	fd(t,r*2+10)
	pd(t)

	
>>> def polypie(t,n,r):
	angle = 360/n
	for i in range(n):
		isosceles(t,r,angle/2)
		lt(t,angle)

		
>>> def isosceles(t,r,angle):
	import math
	y = r*math.sin(angle*math.pi/180)
	rt(t,angle)
	fd(t,r)
	lt(t,90+angle)
	fd(t,2*y)
	lt(t,90+angle)
	fd(t,r)
	lt(t,180-angle)

	
>>> size=40
>>> from swampy.TurtleWorld import*
>>> world = TurtleWorld()
>>> bob = Turtle()
>>> bob.delay = 0
>>> pu(bob)
>>> bk(bob,130)
>>> pd(bob)
>>> size=40
>>> draw_pie(bob,5,size)
>>> draw_pie(bob,6,size)
>>> draw_pie(bob,7,size)
>>> die(bob)
>>> 
