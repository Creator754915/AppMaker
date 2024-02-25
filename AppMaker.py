from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.simpledialog import askstring
from tkinter.ttk import Combobox, Notebook
import json

root = Tk()
root.geometry("1080x680")
root.title("AppMaker")

title = "Unamed_1"

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
          'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
          'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
          'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
          'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
          'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
          'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
          'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
          'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
          'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
          'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
          'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

label = Label(root, text=title, font=("New Time Roman", 18))
label.pack()


def create():
    global title

    try:
        while True:
            title = askstring("AppMaker", "Name of the Application")

            if title == "":
                messagebox.showerror("Error", "Please enter a name !")
            elif len(title) < 3:
                messagebox.showerror("Error", "The name is to short !")
            else:
                label.config(text=title)
                break
    except Exception as e:
        messagebox.showerror("Error", f"{e}")


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
bg_app = "snow"
fg_app = "black"

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
        quit(app_cust)

    create_element = Button(app_cust, text="Create", relief='groove', bg=button_color, command=custom_element_create)
    create_element.pack(fill='both', side=BOTTOM, padx=25, pady=5)

    app_cust.mainloop()


def run_app():
    value1 = slider1.get()
    value2 = slider2.get()
    checkW = chk1.get()
    checkH = chk2.get()
    app_name = entry_name.get()
    bg_app = combo_bg.get()
    fg_app = combo_fg.get()

    text_box.delete("1.0", END)

    text_box.insert(INSERT, f'''from tkinter import *

app = Tk()
app.title("{app_name}")
app.geometry("{value1}x{value2}")
app.resizable({checkW}, {checkH})
app.config(bg="{bg_app}", fg="{fg_app}")

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
    app_1.config(bg=bg_app)

    if labelVar is True:
        if side == "left":
            label_t = Label(app_1, text=textL, font=("New Time Roman", fontsize), fg=fg_app, bg=bg_app)
            label_t.pack(side=LEFT, pady=pady)
        elif side == "top":
            label_t = Label(app_1, text=textL, font=("New Time Roman", fontsize), fg=fg_app, bg=bg_app)
            label_t.pack(side=TOP, pady=pady)
        elif side == "right":
            label_t = Label(app_1, text=textL, font=("New Time Roman", fontsize), fg=fg_app, bg=bg_app)
            label_t.pack(side=RIGHT, pady=pady)
        elif side == "bottom":
            label_t = Label(app_1, text=textL, font=("New Time Roman", fontsize), fg=fg_app, bg=bg_app)
            label_t.pack(side=BOTTOM, pady=pady)
        else:
            label_t = Label(app_1, text="Label", font=("New Time Roman", fontsize), fg=fg_app, bg=bg_app)
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


def change_autosave():
    f = open('appmaker_config.json')
    data = json.load(f)

    if data["Settings"]["Autosave"] is True:
        messagebox.showinfo("AppMaker", "The Autosave is active")
        data["Settings"]["Autosave"] = False
        autosave_button.config(text="True")
    else:
        messagebox.showinfo("AppMaker", "The Autosave isn't active")
        data["Settings"]["Autosave"] = True
        autosave_button.config(text="False")


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
app.config(bg="{bg_app}")

label = Label(app, text="{textL}", font=("New Time Roman", {fontsize}), bg="{bg_color}", fg="{fg_app}")
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
project = Frame(notebook)

general_info.pack(fill='both', expand=False)
settings.pack(fill='both', expand=True)
project.pack(fill='both', expand=True)

notebook.add(general_info, text='General Information')
notebook.add(settings, text='Settings')
notebook.add(project, text='Project')

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

bg_label = Label(settings, text="Background Color", font=("New Time Roman", 12))
bg_label.pack()

combo_bg = Combobox(settings, state="readonly", values=COLORS)
combo_bg.pack()

fg_label = Label(settings, text="General Text Color", font=("New Time Roman", 12))
fg_label.pack()

combo_fg = Combobox(settings, state="readonly", values=COLORS)
combo_fg.pack()

# Project Notebook

export_button = Button(project, text="Export project", width=12, relief="groove", bg=button_color,
                       command=save_file)
export_button.pack(pady=5)

import_button = Button(project, text="Import project", width=12, relief="groove", bg=button_color,
                       command=import_file)
import_button.pack(pady=5)

Label(project, text="Autosave").pack(pady=5)

autosave_button = Button(project, text="", width=12, relief="groove", bg=button_color,
                         command=change_autosave)
autosave_button.pack(pady=5)

btn = Button(frame_middle, text="Run", width=25, relief='groove', bg=button_color, command=run_app)
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
