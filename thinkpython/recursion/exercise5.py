Python 2.7.6 (default, Mar 22 2014, 22:59:38) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from swampy.TurtleWorld import*
>>> world = TurtleWorld()
>>> bob = Turtle()
>>> def koch(t,length):
	if length<3:
		fd(t,length)
		return
	koch(t,(length/3))
	lt(t,60)
	koch(t,(length/3))
	rt(t,120)
	koch(t,(length/3))
	lt(t,60)
	koch(t,(length/3))

	
>>> koch(bob,60)
>>> 

>>> def snoeflake(t,length):
	for i in range(3):
		koch(t,length)
		rt(t,120)

		
>>> snoeflake(bob,60)
>>> 
