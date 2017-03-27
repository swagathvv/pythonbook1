Python 2.7.6 (default, Mar 22 2014, 22:59:38) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> def draw_spiral(t,n,length=3,a=0.1,b=0.0002):
	theta=0.0
	for i in range(n):
		fd(t,length)
		dtheta=1/(a+b*theta)
		lt(t,dtheta)
		theta+=dtheta

		
>>> from swampy.TurtleWorld import*
>>> world = TurtleWorld()
>>> bob = Turtle()
>>> bob.delay=0
>>> draw_spiral(bob,n=1000)
>>> 
