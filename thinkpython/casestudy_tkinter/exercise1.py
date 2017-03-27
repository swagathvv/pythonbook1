from swampy.Gui import *

g = Gui()
g.title = "Gui"

def make_nicejob_button():
    g.bu(text="I make nicejob label", command=make_nicejob_label)

def make_nicejob_label():
    g.la(text="nice job")

button1 = g.bu(text="first button", command=make_nicejob_button)

g.mainloop()
