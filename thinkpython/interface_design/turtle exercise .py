Python 2.7.6 (default, Mar 22 2014, 22:59:38) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from swampy.TurtleWorld import *
>>> world = TurtleWorld()
>>> bob + Turtle

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    bob + Turtle
NameError: name 'bob' is not defined
>>> bob = Turtle()
>>> def square(t):
	for i in range(4):
		fd(t,100)
		lt(t)

		
>>> square(bob)
>>> def square(t,length):
	for i in range(4):
		fd(t,length)
		lt(t)

		
>>> square(bob,200)
>>> def polygon(t,n,length):
	degree=360/n
	for i in range(n):
		fd(t,length)
		lt(t,degree)

		
>>> polygon(bob,7,70)
>>> pop = Turtle()
>>> rt(pop)
>>> rt(pop)
>>> rt(pop)
>>> rt(pop)
>>> rt(pop)
>>> fd(pop,100)
>>> def circle(t,r):
	import math
	circumfrance= 2*math.pi*r
	n= 50
	length= circumfrance/n
	polygon(t,n,length)

	
>>> circle(pop,7)
>>> def arc(t,r,angle):
	arc_length = 2*math.pi*r*angle/360
	n= int(arc_length/3)+1
	step_length=arc_length/n
	step_angle=float(angle)/n

	
>>> def arc(t,r,angle):
	arc_length = 2*math.pi*r*angle/360
	n= int(arc_length/3)+1
	step_length=arc_length/n
	step_angle=float(angle)/n
	for i in range(n):
		fd(t,step_length)
		lt(t,step_angle)

		
>>> arc(bob,30,45)

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    arc(bob,30,45)
  File "<pyshell#48>", line 2, in arc
    arc_length = 2*math.pi*r*angle/360
NameError: global name 'math' is not defined
>>> import math
>>> arc(bob,30,45)
>>> arc(bob,50,100)
>>> 
