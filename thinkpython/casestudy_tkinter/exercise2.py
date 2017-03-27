from swampy.Gui import *

g = Gui()
g.title = "Gui"

def make_circle():
    canvas.circle([0, 0], 55, fill="orange", outline="white", width=3)

canvas = g.ca(500, 500, bg="black")

g.bu(text="make me a circle", command=make_circle)

g.mainloop()
