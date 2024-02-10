from tkinter import *
import json
from tkinter import messagebox

bg_color = "#EFEFEF"
button_color = "#3498db"
label_color = "#2ecc71"
x = 0


def run():
    from inter import inter
    root.quit()
    inter()


def get_selection():
    indices = projectList.curselection()
    for i in indices:
        print(data["ProjectPath"]["".join(projectList.get(i))])


root = Tk()
root.title("AppMaker Launcher")
root.geometry("550x350")
root.resizable(False, False)
root.config(bg=bg_color)

Label(root, text="AppMaker", font=("New Time Roman", 20)).pack(side=TOP)

projectList = Listbox(root, relief="groove", height=10)

f = open('recent_project.json')
data = json.load(f)

for i in data['ProjectPath']:
    x += 1
    projectList.insert(x, i)

f.close()

projectList.pack(fill="both", padx=55, pady=5)

startBtn = Button(root, text="New Project", relief='groove', bg=button_color, command=run)
startBtn.pack(side=BOTTOM, fill='both', padx=55, pady=15)

openBtn = Button(root, text="Open Project", relief='groove', bg=button_color, command=get_selection)
openBtn.pack(side=BOTTOM, fill='both', padx=55, pady=15)

root.mainloop()
