from tkinter import *

class WindowPreview(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(height=400)
        self.title = "My First App"

        header_frame = Frame(self, bg="gray80")
        header_frame.pack(fill=X)

        title_label = Label(header_frame, bg="gray80", text=self.title, font=("Arial", 14, "bold"))
        title_label.pack(side=LEFT, padx=2, pady=5)

        button3 = Button(header_frame, text="X")
        button3.pack(side=RIGHT, padx=2, pady=2)

        button2 = Button(header_frame, text="-")
        button2.pack(side=RIGHT, padx=2, pady=2)

        button1 = Button(header_frame, text="□")
        button1.pack(side=RIGHT, padx=2, pady=2)


        self.button_container = Frame(self)
        self.button_container.pack(pady=10, padx=5)

        Button(self.button_container, text="fdfdsfds").pack()

        Button(self.button_container, text="fdsfds").pack()

        Button(self.button_container, text="trey").pack()

        Button(self.button_container, text="nbcv").pack()

        Button(self.button_container, text="ioupo").pack()
