from tkinter import *
from AppMaker.Variables import bg_color, button_color


def run():
    root.quit()


root = Tk()
root.title("AppMaker Launcher")
root.geometry("550x350")
root.resizable(False, False)
root.config(bg=bg_color)

Label(root, text="AppMaker", font=("New Time Roman", 20)).pack(side=TOP)

projectList = Listbox(root, relief="groove", height=10)
projectList.pack(fill="both", padx=55, pady=5)

startBtn = Button(root, text="New Project", relief='groove', bg=button_color, command=run)
startBtn.pack(side=BOTTOM, fill='both', padx=55, pady=15)

openBtn = Button(root, text="Open Project", relief='groove', bg=button_color)
openBtn.pack(side=BOTTOM, fill='both', padx=55, pady=15)

root.mainloop()
