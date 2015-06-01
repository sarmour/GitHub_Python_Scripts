#create a simple GUI

from Tkinter import *

###create window
##root = Tk()
##
###modify root window
##root.title("Snake Game")
##root.geometry("200x200")
##
##app = Frame(root) #need to create a frame
##app.grid()
##
###create grid
##label = Label(app, text = "This is a test")
##label.grid()
##
##button1 = Button(app, text = "This is a button")
##button1.grid()
##
##
###kick off the event loop
##root.mainloop()

class Application(Frame):
    """ A GUI application with three buttons."""

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text = "This is button 1")
        self.button1.grid()

        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text = "this is the second button")

        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"] = "This will also work"

root = Tk()
app = Application(root)
root.mainloop()
