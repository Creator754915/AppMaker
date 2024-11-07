from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.simpledialog import askstring
from tkinter.ttk import Combobox, Notebook

from AppMaker.Variables import *
from AppMaker.Variables import BASE_DICT, BASE_BTN
from AppMaker.Widgets.WindowGUI import WindowPreview


class AppMaker(Tk):
    def __init__(self, title="AppMaker"):
        super().__init__()
        self.ctrl_pressed = False
        self.title(title)
        self.geometry("1080x680")
        self.ProjectName = "UnNamed_1"
        self.ProjectPATH = NONE
        self.ProjectData = NONE
        self.ElementDict = BASE_DICT
        self.WidthV, self.HeightV = BooleanVar(), BooleanVar()
        self.saved = False

        self.projectLabel = Label(self, text=self.ProjectName, font=("New Time Roman", 18))
        self.projectLabel.pack()

        self.FrameRight = Frame(self, width=250, bg="gray89")
        self.FrameRight.pack(side=RIGHT, fill=BOTH)

        self.FrameMiddle = Frame(self, width=450)
        self.FrameMiddle.pack(expand=1, fill=BOTH)

        self.FrameBottom = Frame(self, height=200, bg="gray89")
        self.FrameBottom.pack(side=BOTTOM, fill=BOTH)

        WindowPreview(master=self).pack(fill=BOTH, expand=True)


        self.NoteBook = Notebook(self.FrameBottom)
        self.NoteBook.pack(pady=5, fill="both", expand=True)

        self.WindowInfo = Frame(self.NoteBook)
        self.ElementsSettings = Frame(self.NoteBook)
        self.ProjectSettings = Frame(self.NoteBook)

        self.WindowInfo.pack(fill='both', expand=False)
        self.ElementsSettings.pack(fill='both', expand=True)
        self.ProjectSettings.pack(fill='both', expand=True)

        self.NoteBook.add(self.WindowInfo, text='Window Information')
        self.NoteBook.add(self.ElementsSettings, text='Elements Settings')
        self.NoteBook.add(self.ProjectSettings, text='Project Settings')

        Label(self.WindowInfo, text="Application Name", font=("New Time Roman", 12)).pack()

        self.AppName = Entry(self.WindowInfo)
        self.AppName.pack()

        Label(self.WindowInfo, text="Background Color", font=("New Time Roman", 12)).pack()

        self.BgApp = Entry(self.WindowInfo)
        self.BgApp.pack()

        Label(self.WindowInfo, text="Icon Path", font=("New Time Roman", 12)).pack()

        self.button_icon = Button(self.WindowInfo, text="Open Icon", width=17, relief="groove", bg=button_color)
        self.button_icon.pack()

        Label(self.WindowInfo, text="Width App", font=("New Time Roman", 12)).pack()

        self.slider1 = Scale(self.WindowInfo, from_=200, to=1080, orient=HORIZONTAL, activebackground="gray", length=200, bd=0)
        self.slider1.set(720)
        self.slider1.pack()

        Label(self.WindowInfo, text="Height App", font=("New Time Roman", 12)).pack()

        self.slider2 = Scale(self.WindowInfo, from_=200, to=1080, orient=HORIZONTAL, activebackground="gray", length=200, bd=0)
        self.slider2.set(460)
        self.slider2.pack()

        Label(self.WindowInfo, text="Resizable", font=("New Time Roman", 10)).pack()

        self.checkbox1 = Checkbutton(self.WindowInfo, text='Width', variable=self.WidthV, onvalue=True, offvalue=False)
        self.checkbox1.pack()

        self.checkbox2 = Checkbutton(self.WindowInfo, text='Height', variable=self.HeightV, onvalue=True, offvalue=False)
        self.checkbox2.pack()

        #self.CreateNewProject()

        self.MenuBar = Menu(self)
        self.config(menu=self.MenuBar)

        self.FileMenu = Menu(self.MenuBar, tearoff=0)
        self.FileMenu.add_command(label="New", command=self.CreateNewProject)
        self.FileMenu.add_command(label="Open", command=self.OpenProject)
        self.FileMenu.add_command(label="Save", command=self.SavedAsProject)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit", command=self.quit)

        self.EditMenu = Menu(self.MenuBar, tearoff=0)
        self.EditMenu.add_command(label="Create Button", command=self.CreateButton)
        self.EditMenu.add_command(label="Create Label")
        self.EditMenu.add_command(label="Create Entry")


        self.RunMenu = Menu(self.MenuBar, tearoff=0)
        self.RunMenu.add_command(label="Run", command=self.RunPreview)
        self.RunMenu.add_command(label="Debug")
        self.RunMenu.add_command(label="Show Log")

        self.MenuBar.add_cascade(label="File", menu=self.FileMenu)
        self.MenuBar.add_cascade(label="Edit", menu=self.EditMenu)
        self.MenuBar.add_cascade(label="Run", menu=self.RunMenu)

        self.mainloop()



    def OpenProject(self):
        self.ProjectData = filedialog.askopenfile(initialdir="/", title="Select A File",
                                              filetypes=(("AppMaker Project Files", "*.appmaker"),
                                              ("All Files", "*.")))

        self.ElementDict = str(self.ProjectData.read())
        print(self.ElementDict)

    def CreateNewProject(self):
        if not self.saved:
            answer = messagebox.askokcancel("AppMaker", "Project unsaved, do you can to continue ?")
            if answer:
                self.ElementDict = BASE_DICT
                self.saved = False
                self.ProjectName = askstring("AppMaker", "Enter the project name:")
                self.ProjectPATH = asksaveasfile(initialfile=f'{self.ProjectName}.appmaker', defaultextension=".appmaker",
                              filetypes=[("AppMaker Project Files", "*.appmaker"),
                                         ("All Files", "*.*")])

                self.ProjectPATH.write(self.ElementDict)


    def CreateButton(self):
        def create_button():
            button = Button(
                ButtonApp,
                text=ButtonTextEntry.get(),
                bg=BgButtonEntry.get(),
                fg=FgButtonEntry.get(),
                font=("Arial", int(FontButtonEntry.get())),
                state=StateButtonValue.get(),
                relief=ReliefButtonStyle.get(),
                width=int(WidthButtonEntry.get()),
                border=int(BorderWidthButtonEntry.get()),
                pady=int(PaddingYButtonEntry.get()),
                padx=int(PaddingXButtonEntry.get()),
                command=str(FunctionButtonEntry.get())
            )
            button.pack(pady=10)

            for i in range(len(self.ElementDict["Buttons"]) + 1):
                self.ElementDict["Buttons"][str(i)] = {
                    "text": ButtonTextEntry.get(),
                    "bg": BgButtonEntry.get(),
                    "fg": FgButtonEntry.get(),
                    "font": ("Arial", int(FontButtonEntry.get())),
                    "state": StateButtonValue.get(),
                    "relief": ReliefButtonStyle.get(),
                    "width": int(WidthButtonEntry.get()),
                    "border": int(BorderWidthButtonEntry.get()),
                    "pady": int(PaddingYButtonEntry.get()),
                    "padx": int(PaddingXButtonEntry.get()),
                    "command": FunctionButtonEntry.get()
                }

            print(self.ElementDict["Buttons"])

        ButtonApp = Tk()
        ButtonApp.title("AppMaker - Create Button")
        ButtonApp.geometry("400x350")

        Label(ButtonApp, text="Text of the button:").pack()
        ButtonTextEntry = Entry(ButtonApp)
        ButtonTextEntry.pack()

        Label(ButtonApp, text="Background color of the Button:").pack()
        BgButtonEntry = Entry(ButtonApp)
        BgButtonEntry.pack()

        Label(ButtonApp, text="Couleur du texte (fg):").pack()
        FgButtonEntry = Entry(ButtonApp)
        FgButtonEntry.pack()

        Label(ButtonApp, text="Taille de la police:").pack()
        FontButtonEntry = Entry(ButtonApp)
        FontButtonEntry.pack()

        Label(ButtonApp, text="State of the Button:").pack()
        StateButtonValue = Combobox(ButtonApp, state="readonly", values=[NORMAL, DISABLED])
        StateButtonValue.pack()

        Label(ButtonApp, text="Relief of the Button:").pack()
        ReliefButtonStyle = Combobox(ButtonApp, state="readonly", values=[FLAT, GROOVE, RAISED, RIDGE, SUNKEN])
        ReliefButtonStyle.pack()

        Label(ButtonApp, text="Width:").pack()
        WidthButtonEntry = Entry(ButtonApp)
        WidthButtonEntry.pack()

        Label(ButtonApp, text="Border width:").pack()
        BorderWidthButtonEntry = Entry(ButtonApp)
        BorderWidthButtonEntry.pack()

        Label(ButtonApp, text="Padding Y:").pack()
        PaddingYButtonEntry = Entry(ButtonApp)
        PaddingYButtonEntry.pack()

        Label(ButtonApp, text="Padding X:").pack()
        PaddingXButtonEntry = Entry(ButtonApp)
        PaddingXButtonEntry.pack()

        FunctionButtonEntry = Entry(ButtonApp)
        FunctionButtonEntry.pack()

        create_button_btn = Button(ButtonApp, text="Create button", command=create_button)
        create_button_btn.pack(pady=20)

        ButtonApp.mainloop()

    def RunPreview(self):
        PreviewApp = Tk()
        PreviewApp.title(self.ElementDict["Window"]["title"])
        PreviewApp.config(bg=self.ElementDict["Window"]["bg"])
        PreviewApp.geometry(self.ElementDict["Window"]["geometry"])
        PreviewApp.resizable(self.ElementDict["Window"]["resizable"][0], self.ElementDict["Window"]["resizable"][1])
        PreviewApp.iconbitmap(self.ElementDict["Window"]["icon"])

        for i in range(len(self.ElementDict["Buttons"]) + 1):
            (Button(PreviewApp, text=self.ElementDict["Buttons"][str(i)]["text"],
                    state=self.ElementDict["Buttons"][str(i)]["state"],
                    bg=self.ElementDict["Buttons"][str(i)]["bg"], fg=self.ElementDict["Buttons"][str(i)]["fg"],
                    relief=self.ElementDict["Buttons"][str(i)]["relief"],
                    borderwidth=self.ElementDict["Buttons"][str(i)]["border"],
                    command=self.ElementDict["Buttons"][str(i)]["command"])
             .pack(side=self.ElementDict["Buttons"][str(i)]["side"], fill=self.ElementDict["Buttons"][str(i)]["fill"],
                   padx=self.ElementDict["Buttons"][str(i)]["padx"], pady=self.ElementDict["Buttons"][str(i)]["pady"]))

        PreviewApp.mainloop()



    def SavedAsProject(self):
        saveAsFile = asksaveasfile(initialfile=f'{self.ProjectName}.appmaker', defaultextension=".appmaker",
                                        filetypes=[("AppMaker Project Files", "*.appmaker"),
                                                   ("All Files", "*.*")])

        saveAsFile.write(str(self.ElementDict))

        messagebox.showinfo("AppMaker", "Project saved !")


if __name__ == "__main__":
    AppMaker()
