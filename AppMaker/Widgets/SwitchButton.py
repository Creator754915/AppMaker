from tkinter import *

class Switch(Button):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.State = True
        self.config(width=8, text="On", command=self.Switch)


    def Switch(self):
        if self.State:
            self.config(text="Off")
            self.State = False
        else:
            self.config(text="On")
            self.State = True
