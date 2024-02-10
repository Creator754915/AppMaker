from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.simpledialog import askstring
from tkinter.ttk import Combobox, Notebook
import json

root = Tk()
root.geometry("1080x680")
root.title("AppMaker")

title = "unamed_1"

label = Label(root, text=title, font=("New Time Roman", 18))
label.pack()


def create():
    global title
    title = askstring("AppMaker", "Name the Application")



    label.config(text=title)


create()

bg_color = "#EFEFEF"  # Light gray background
button_color = "#3498db"  # Blue button color
label_color = "#2ecc71"  # Green label color

labelVar = False
side = TOP
pady = 0
fontsize = 10
buttonVar = False
side2 = TOP
pady2 = 0
fontsize2 = 10
imageVar = False
textL = ""

value_ctb = ""

project_file = "C:/"
path_ico = "C:/"
path_image = "C:/"


def create_label():
    global labelVar, side, pady, fontsize, textL

    if labelVar is False:
        labelVar = True
        text = askstring("AppMaker", "Label Text")

        textL = text

        button1.config(text="UPDATE LABEL")
    else:
        side = combo_side.get()
        pady = entry_pady.get()
        fontsize = entry_fontsize.get()

        text = askstring("AppMaker", "Label Text")

        textL = text

        print(labelVar, side, pady, textL)
        messagebox.showinfo("AppMaker", "Label updated !")


def create_button():
    global buttonVar, side2, pady2, fontsize2

    if buttonVar is False:
        buttonVar = True
        button2.config(text="UPDATE BUTTON")
    else:
        side2 = button_combo_side.get()
        pady2 = button_entry_pady.get()
        fontsize2 = button_entry_fontsize.get()
        print(buttonVar, side2, pady2)
        messagebox.showinfo("AppMaker", "BUTTON updated !")


def open_ico():
    global path_ico
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("ico files", "*.ico"),
                                                                                                 ("all files", "*.*")))
    path_ico = root.filename


def open_image():
    global path_image
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("png files", "*.png"),
                                                                                                 ("jpg files", "*.jpg"),
                                                                                                 ("rw2 files", "*.rw2"),
                                                                                                 ("all files", "*.*")))
    path_image = root.filename
    label_image.configure(text=path_image)


def custom_element():
    app_cust = Tk()
    app_cust.title("Custom Element Editor")
    app_cust.geometry("600x500")
    app_cust.resizable(False, False)

    ce_text_box = Text(app_cust, font=("New Time Roman", 12))
    ce_text_box.pack(fill='both', expand=True)

    ce_text_box.insert(INSERT, f'''custom = Button(app, text="Custom Element", relief="groove", bg={bg_color})
custom.pack(side=TOP, pady=10)''')

    def custom_element_create():
        global value_ctb
        value_ctb = ce_text_box.get("1.0", END)
        app_cust.quit()

    create_element = Button(app_cust, text="Create", relief='groove', bg=button_color, command=custom_element_create)
    create_element.pack(fill='both', side=BOTTOM, padx=25, pady=5)

    app_cust.mainloop()


def run_app():
    value1 = slider1.get()
    value2 = slider2.get()
    checkW = chk1.get()
    checkH = chk2.get()
    app_name = entry_name.get()

    text_box.delete("1.0", END)

    text_box.insert(INSERT, f'''from tkinter import *

app = Tk()
app.title("{app_name}")
app.geometry("{value1}x{value2}")
app.resizable({checkW}, {checkH})

label = Label(app, text="{textL}", font=("New Time Roman", {fontsize}), bg="{bg_color}")
label.pack(side={side.upper()}, pady={pady})

button = Button(app, text="Label", font=("New Time Roman", {fontsize2}), relief="groove", bg="{button_color}")
button.pack(side={side2.upper()}, pady={pady2})

{value_ctb}

app.mainloop()
''')

    list_debug.insert(0, "PROCESS: The program still run")

    app_1 = Tk()

    app_1.geometry(f"{value1}x{value2}")
    app_1.title(f"{app_name}")
    app_1.iconbitmap(path_ico)
    app_1.resizable(checkW, checkH)

    if labelVar is True:
        if side == "left":
            label_t = Label(app_1, text=textL, font=("New Time Roman", fontsize))
            label_t.pack(side=LEFT, pady=pady)
        elif side == "top":
            label_t = Label(app_1, text=textL, font=("New Time Roman", fontsize))
            label_t.pack(side=TOP, pady=pady)
        elif side == "right":
            label_t = Label(app_1, text=textL, font=("New Time Roman", fontsize))
            label_t.pack(side=RIGHT, pady=pady)
        elif side == "bottom":
            label_t = Label(app_1, text=textL, font=("New Time Roman", fontsize))
            label_t.pack(side=BOTTOM, pady=pady)
        else:
            label_t = Label(app_1, text="Label", font=("New Time Roman", fontsize))
            label_t.pack(side=TOP, pady=pady)
            list_debug.insert(0, "MISSING: Option side not enter")
    if buttonVar is True:
        if side2 == "left":
            label_t = Button(app_1, text="Label", font=("New Time Roman", fontsize2), relief="groove", bg=button_color)
            label_t.pack(side=LEFT, pady=pady2)
        elif side2 == "top":
            label_t = Button(app_1, text="Label", font=("New Time Roman", fontsize2), relief="groove", bg=button_color)
            label_t.pack(side=TOP, pady=pady2)
        elif side2 == "right":
            label_t = Button(app_1, text="Label", font=("New Time Roman", fontsize2), relief="groove", bg=button_color)
            label_t.pack(side=RIGHT, pady=pady2)
        elif side2 == "bottom":
            label_t = Button(app_1, text="Label", font=("New Time Roman", fontsize2), relief="groove", bg=button_color)
            label_t.pack(side=BOTTOM, pady=pady2)
        else:
            label_t = Button(app_1, text="Label", font=("New Time Roman", fontsize2), relief="groove", bg=button_color)
            label_t.pack(side=TOP, pady=pady2)
            list_debug.insert(0, "MISSING: Option side not enter")


def clear_debug():
    list_debug.delete(0, END)


def import_file():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                               filetypes=(("Python Files", "*.py"),
                                                          ("Console Python Files", "*.pyw")))


def save_file():
    project_file_export = asksaveasfile(initialfile=f'{title}.py', defaultextension=".py",
                                        filetypes=[("Python Files", "*.py"),
                                                   ("Console Python Files", "*.pyw"),
                                                   ("All Files", "*.*")])

    value1 = slider1.get()
    value2 = slider2.get()
    checkW = chk1.get()
    checkH = chk2.get()
    app_name = entry_name.get()

    project_file_export.write(f'''from tkinter import *

app = Tk()
app.title("{app_name}")
app.geometry("{value1}x{value2}")
app.resizable({checkW}, {checkH})

label = Label(app, text="{textL}", font=("New Time Roman", {fontsize}), bg="{bg_color}")
label.pack(side={side.upper()}, pady={pady})

button = Button(app, text="Label", font=("New Time Roman", {fontsize2}), bg="{button_color}")
button.pack(side={side2.upper()}, pady={pady2})

{value_ctb}

app.mainloop()''')


# Right Frame

frame_right = Frame(root, width=150)
frame_right.pack(side=RIGHT, fill=BOTH)

frame_middle = Frame(root, width=400)
frame_middle.pack(expand=1, fill=BOTH)

frame_bottom = Frame(root, height=80)
frame_bottom.pack(side=BOTTOM, fill=BOTH)

button1 = Button(frame_right,
                 text="Create Label", width=12, relief="groove", bg=button_color, command=create_label)
button1.pack()

label1 = Label(frame_right, text="Side of Label", font=("New Time Roman", 12))
label1.pack()

combo_side = Combobox(frame_right, state="readonly", values=["left", "top", "right", "bottom"])
combo_side.pack()

label2 = Label(frame_right, text="Pady of Label", font=("New Time Roman", 12))
label2.pack()

entry_pady = Entry(frame_right)
entry_pady.pack(fill=BOTH)

label2 = Label(frame_right, text="Font size of Label", font=("New Time Roman", 12))
label2.pack()

entry_fontsize = Entry(frame_right)
entry_fontsize.pack(fill=BOTH)

button2 = Button(frame_right, text="Create Button", width=12, relief="groove", bg=button_color, command=create_button)
button2.pack(pady=5)

button_label1 = Label(frame_right, text="Side of Button", font=("New Time Roman", 12))
button_label1.pack()

button_combo_side = Combobox(frame_right, state="readonly", values=["left", "top", "right", "bottom"])
button_combo_side.pack()

button_label2 = Label(frame_right, text="Pady of Button", font=("New Time Roman", 12))
button_label2.pack()

button_entry_pady = Entry(frame_right)
button_entry_pady.pack(fill=BOTH)

button_label2 = Label(frame_right, text="Font size of Button", font=("New Time Roman", 12))
button_label2.pack()

button_entry_fontsize = Entry(frame_right)
button_entry_fontsize.pack(fill=BOTH)

button3 = Button(frame_right, text="Create Image", width=12, relief="groove", bg=button_color, command=open_image)
button3.pack(pady=5)

label_image = Label(frame_right, text=path_image, bg=bg_color)
label_image.pack()

button4 = Button(frame_right, text="Custom Element", width=12, relief="groove", bg=button_color, command=custom_element)
button4.pack(pady=5)

# Middle Frame

notebook = Notebook(frame_middle)
notebook.pack(pady=5, fill="both", expand=True)

general_info = Frame(notebook)
settings = Frame(notebook)

general_info.pack(fill='both', expand=False)
settings.pack(fill='both', expand=True)

notebook.add(general_info, text='General Information')
notebook.add(settings, text='Settings')

# General Information Notebook

label_name = Label(general_info, text="Name App", font=("New Time Roman", 12))
label_name.pack()

entry_name = Entry(general_info)
entry_name.pack()

label_icon = Label(general_info, text="Icon Path", font=("New Time Roman", 12))
label_icon.pack()

button_icon = Button(general_info, text="Open Icon", width=17, command=open_ico)
button_icon.pack()

label_width = Label(general_info, text="Width App", font=("New Time Roman", 12))
label_width.pack()

slider1 = Scale(general_info, from_=200, to=1080, orient=HORIZONTAL, activebackground="gray", length=200, bd=0)
slider1.set(720)
slider1.pack()

label_height = Label(general_info, text="Height App", font=("New Time Roman", 12))
label_height.pack()

slider2 = Scale(general_info, from_=200, to=1080, orient=HORIZONTAL, activebackground="gray", length=200, bd=0)
slider2.set(460)
slider2.pack()

label_height = Label(general_info, text="Resizeable", font=("New Time Roman", 10))
label_height.pack()

chk1 = BooleanVar()
chk2 = BooleanVar()

checkbox1 = Checkbutton(general_info, text='Width', variable=chk1, onvalue=True, offvalue=False)
checkbox1.pack()

checkbox2 = Checkbutton(general_info, text='Height', variable=chk2, onvalue=True, offvalue=False)
checkbox2.pack()

# Setting Notebook

export_button = Button(settings, text="Export project", width=12, relief="groove", bg=button_color,
                       command=save_file)
export_button.pack(pady=5)

import_button = Button(settings, text="Import project", width=12, relief="groove", bg=button_color,
                       command=import_file)
import_button.pack(pady=5)

btn = Button(frame_middle, text="Run", width=17, command=run_app)
btn.pack()

text_box = Text(frame_middle, width=250, font=("New Time Roman", 10))
text_box.pack(fill=BOTH, expand=2)

# Bottom Frame

list_debug = Listbox(frame_bottom, height=100)
list_debug.configure(fg="red")
list_debug.pack(side=LEFT, fill='both', expand=True)

btn_clear = Button(frame_bottom, text="Clear", command=clear_debug)
btn_clear.pack()


def save_projet():
    value1 = slider1.get()
    value2 = slider2.get()
    checkW = chk1.get()
    checkH = chk2.get()
    app_name = entry_name.get()

    save_data = f'''from tkinter import *

app = Tk()
app.title("{app_name}")
app.geometry("{value1}x{value2}")
app.resizable({checkW}, {checkH})

label = Label(app, text="{textL}", font=("New Time Roman", {fontsize}), bg="red")
label.pack(side={side.upper()}, pady={pady})

button = Button(app, text="Label", font=("New Time Roman", {fontsize2}), bg="red")
button.pack(side={side2.upper()}, pady={pady2})

app.mainloop()
    '''
    txt = open(f"{title}.py", "w")

    txt.write(str(save_data))

    txt.close()


menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=create)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save", command=save_projet)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help")
helpmenu.add_separator()
helpmenu.add_command(label="About")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.mainloop()
