import datetime
from tkinter import *
from tkinter import messagebox, filedialog, colorchooser
from tkinter.filedialog import asksaveasfile
from tkinter.simpledialog import askstring
from tkinter.ttk import Combobox, Notebook, Treeview
import customtkinter as ctk

from AppMaker.Node import *
from AppMaker.Variables import *
from AppMaker.Variables import BASE_DICT
from AppMaker.Widgets.WindowGUI import WindowPreview


class AppMaker(Tk):
    def __init__(self):
        super().__init__()
        self.ctrl_pressed = False
        self.geometry("1080x680")
        self.ProjectName = "UnNamed_1"
        self.title(f'AppMaker - {self.ProjectName}')
        self.ProjectPATH = NONE
        self.ProjectData = NONE
        self.ElementDict = BASE_DICT
        self.ElementColor = "black"
        self.ConsoleList = []
        self.saved = False

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")
        ctk.deactivate_automatic_dpi_awareness()

        self.FrameRight = ctk.CTkFrame(self, width=250)
        self.FrameRight.pack(side=RIGHT, fill=BOTH)

        self.FrameMiddle = ctk.CTkFrame(self, width=450)
        self.FrameMiddle.pack(expand=1, fill=BOTH)

        self.FrameBottom = ctk.CTkFrame(self, height=200, corner_radius=0)
        self.FrameBottom.pack(side=BOTTOM, fill=BOTH)

        # Console Panel

        self.ConsoleTabView = ctk.CTkTabview(self.FrameBottom, anchor="nw")
        self.ConsoleTabView.pack(fill=BOTH)

        self.ConsoleTabView.add("Console")
        self.ConsoleTabView.add("Debug")

       # self.ClearButton = ctk.CTkButton(self.ConsoleTabView, width=30, text="x", bg_color="#2f2f2f", command=lambda: self.ConsoleList.clear())
       # self.ClearButton.pack(pady=5, padx=10)

        self.ConsoleFrame = ctk.CTkScrollableFrame(self.ConsoleTabView.tab("Console"))
        self.ConsoleFrame.pack(padx=10, pady=10, expand=True, fill="both")


        # WindowPreview and NodeEditor

        self.TabViewEdit = ctk.CTkTabview(self.FrameMiddle, anchor="nw")
        self.TabViewEdit.pack(fill=BOTH, expand=True)

       #self.WindowPreviewEdit = ctk.CTkFrame(self.TabViewEdit)
       #self.WindowPreviewEdit.pack(fill=BOTH, expand=True)
       #self.NodeEditor = ctk.CTkFrame(self.TabViewEdit)
       #self.NodeEditor.pack(fill=BOTH, expand=True)

        self.TabViewEdit.add("Window Preview")
        self.TabViewEdit.add("Node Editor")


        self.WindowPreview = WindowPreview(master=self.TabViewEdit.tab("Window Preview"), fg_color="gray40")
        self.WindowPreview.pack(pady=20, padx=20, fill=BOTH, expand=True)

        self.NodeCanvas = NodeCanvas(self.TabViewEdit.tab("Node Editor"))
        self.NodeCanvas.pack(fill="both", expand=True)

        NodeValue(self.NodeCanvas, text="Function1", x=0, y=10)
        NodeOperation(self.NodeCanvas, text="Combine to", x=150, y=1)
        NodeCompile(self.NodeCanvas, text="Run", x=300, y=10)

        self.NodeMenu = NodeMenu(self.NodeCanvas)  # right click or press <space> to spawn the node menu
        self.NodeMenu.add_node(label="Function", command=self.AddNodeFunction)
        self.NodeMenu.add_node(label="Node Operation", command=lambda: NodeOperation(self.NodeCanvas))
        self.NodeMenu.add_node(label="Node Compile", command=lambda: NodeCompile(self.NodeCanvas))


        # Tools Box
        self.TabViewTool = ctk.CTkTabview(self.FrameRight, anchor="nw", fg_color="gray20", border_width=2)
        self.TabViewTool.pack(fill="both", expand=True)

       # self.WindowInfo = ctk.CTkFrame(self.TabViewTool)
       # self.ElementsSettings = ctk.CTkFrame(self.TabViewTool)
       # self.ProjectSettings = ctk.CTkFrame(self.TabViewTool)

       # self.WindowInfo.pack(fill='both', expand=False)
       # self.ElementsSettings.pack(fill='both', expand=True)
       # self.ProjectSettings.pack(fill='both', expand=True)

        self.TabViewTool.add('Project')
        self.TabViewTool.add('Window')
        self.TabViewTool.add('Elements')


        # Project Panel
        self.ApplicationTree = ctk.CTkScrollableFrame(self.TabViewTool.tab("Project"))
        self.ApplicationTree.pack(padx=10, pady=10, fill="both")

        ctk.CTkLabel(self.TabViewTool.tab("Project"), text="Project Name").pack(pady=5)
        ctk.CTkEntry(self.TabViewTool.tab("Project"), placeholder_text=self.ProjectName).pack(padx=5, pady=5, fill=BOTH)


        # Window Panel
        ctk.CTkLabel(self.TabViewTool.tab("Window"), text="Application Name", font=("New Time Roman", 12)).pack()

        def on_value_change(*args):
            self.ElementDict["Window"]["title"] = self.AppName.get()
            self.ElementDict["Window"]["bg"] = self.BgApp.get()
            self.ElementDict["Window"]["geometry"] = f"{AppWithValue.get()}x{AppHeightValue.get()}"
            self.ElementDict["Window"]["resizable"] = [WidthBool.get(), HeightBool.get()]


        EntryNameValue = StringVar()
        EntryBgValue = StringVar()
        AppWithValue = IntVar()
        AppHeightValue = IntVar()
        WidthBool = BooleanVar()
        HeightBool = BooleanVar()

        EntryNameValue.trace_add("write", on_value_change)
        EntryBgValue.trace_add("write", on_value_change)
        AppWithValue.trace_add("write", on_value_change)
        AppHeightValue.trace_add("write", on_value_change)
        WidthBool.trace_add("write", on_value_change)
        HeightBool.trace_add("write", on_value_change)

        self.AppName = ctk.CTkEntry(self.TabViewTool.tab("Window"), placeholder_text="Application name", textvariable=EntryNameValue)
        self.AppName.pack(padx=5, fill=BOTH)

        ctk.CTkLabel(self.TabViewTool.tab("Window"), text="Background Color", font=("New Time Roman", 12)).pack()
        self.BgApp = ctk.CTkEntry(self.TabViewTool.tab("Window"), placeholder_text="Application background", textvariable=EntryBgValue)
        self.BgApp.pack(padx=5, fill=BOTH)

        ctk.CTkLabel(self.TabViewTool.tab("Window"), text="Icon Path", font=("New Time Roman", 12)).pack()
        self.button_icon = ctk.CTkButton(self.TabViewTool.tab("Window"), text="Open Icon", width=17)
        self.button_icon.pack(padx=5, fill=BOTH)

        ctk.CTkLabel(self.TabViewTool.tab("Window"), text="Width App", font=("New Time Roman", 12)).pack()
        self.SliderWidth = ctk.CTkSlider(self.TabViewTool.tab("Window"), variable=AppWithValue, from_=200, to=1080)
        self.SliderWidth.set(720)
        self.SliderWidth.pack()

        ctk.CTkLabel(self.TabViewTool.tab("Window"), text="Height App", font=("New Time Roman", 12)).pack()
        self.SliderHeight = ctk.CTkSlider(self.TabViewTool.tab("Window"), variable=AppHeightValue, from_=200, to=1080)
        self.SliderHeight.set(460)
        self.SliderHeight.pack()

        ctk.CTkLabel(self.TabViewTool.tab("Window"), text="Resizable", font=("New Time Roman", 10)).pack()
        self.CheckboxWidth = ctk.CTkCheckBox(self.TabViewTool.tab("Window"), text='Width', variable=WidthBool, onvalue=True, offvalue=False)
        self.CheckboxWidth.pack(pady=5)

        self.CheckboxHeight = ctk.CTkCheckBox(self.TabViewTool.tab("Window"), text='Height', variable=HeightBool, onvalue=True, offvalue=False)
        self.CheckboxHeight.pack()

        # Element Panel
        ctk.CTkButton(self.TabViewTool.tab("Elements"), text="Create Button", cursor="hand2",command=self.CreateButton).pack(fill=X, padx=10, pady=10)
        ctk.CTkButton(self.TabViewTool.tab("Elements"), text="Create Label", cursor="hand2", command=self.CreateLabel).pack(fill=X, padx=10, pady=10)
        ctk.CTkButton(self.TabViewTool.tab("Elements"), text="Create Entry", cursor="hand2").pack(fill=X, padx=10, pady=10)

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
        self.EditMenu.add_command(label="Create Label", command=self.CreateLabel)
        self.EditMenu.add_command(label="Create Entry")


        self.RunMenu = Menu(self.MenuBar, tearoff=0)
        self.RunMenu.add_command(label="Run", command=self.RunPreview)
        self.RunMenu.add_command(label="Debug")
        self.RunMenu.add_command(label="Show Log")

        self.MenuBar.add_cascade(label="File", menu=self.FileMenu)
        self.MenuBar.add_cascade(label="Edit", menu=self.EditMenu)
        self.MenuBar.add_cascade(label="Run", menu=self.RunMenu)

        self.ButtonXPos = Button(self, width=1, height=50, bg="black")
        self.ButtonYPos = Button(self, width=120, height=1, bg="black")

        # self.bind("<Motion>", self.test)

        self.mainloop()



    def addReturn(self, info):
        self.ConsoleList.append(f"{str(info)}")
        self.ShowConsole()

    def ShowConsole(self):
        for widget in self.ConsoleFrame.winfo_children():
            widget.destroy()

        for i, element in enumerate(self.ConsoleList):
            label = ctk.CTkLabel(self.ConsoleFrame, text=element, anchor="w")
            label.pack(fill="x", padx=5, pady=2)

    def AddNodeFunction(self):
        dialog = ctk.CTkInputDialog(text="Enter a name for the function:", title="Function Node")
        text = dialog.get_input()
        if text is not None:
            if text.isdigit():
                NodeValue(self.NodeCanvas, text=f"{str(text)}", value=str(text))

    def PosEvent(self, event):
        if event.x > 840:
            self.ButtonXPos.place(x=0, y=0)
        self.ButtonXPos.place(x=event.x / 1, y=0)
        self.ButtonYPos.place(x=0, y=event.y)
        print(event.x, event.y)


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
                self.title(f'AppMaker - {self.ProjectName}')


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
                command=str(FunctionButtonEntry.get())
            )
            button.pack(pady=int(PaddingYButtonEntry.get()), padx=int(PaddingXButtonEntry.get()),
                        side=SideButtonStyle.get())

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
                    "side": SideButtonStyle.get(),
                    "command": FunctionButtonEntry.get()
                }

            self.ApplicationTree.insert("", END, text=f"Button {len(self.ElementDict["Buttons"])}")

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

        Label(ButtonApp, text="Side of the Button:").pack()
        SideButtonStyle = Combobox(ButtonApp, state="readonly", values=[LEFT, RIGHT, TOP, BOTTOM, CENTER, NONE])
        SideButtonStyle.pack()

        Label(ButtonApp, text="Padding Y:").pack()
        PaddingYButtonEntry = Entry(ButtonApp)
        PaddingYButtonEntry.pack()

        Label(ButtonApp, text="Padding X:").pack()
        PaddingXButtonEntry = Entry(ButtonApp)
        PaddingXButtonEntry.pack()

        FunctionButtonEntry = Entry(ButtonApp)
        FunctionButtonEntry.pack(pady=5)

        create_button_btn = Button(ButtonApp, text="Create button", command=create_button)
        create_button_btn.pack(pady=20)

        ButtonApp.mainloop()

    def CreateLabel(self):
        def ColorChooser():
            self.ElementColor = colorchooser.askcolor(title="Choose color for the background")

        def create_label():
            (Label(LabelApp, text=LabelTextEntry.get(), bg=self.ElementColor, fg=FgLabelEntry.get(), font=("Arial", int(FontLabelEntry.get())),
                  wraplength=int(WrapLabelValue.get()), underline=int(UnderlineLabelStyle.get()), relief=ReliefLabelCombobox.get(),
                  border=BorderWidthLabelEntry.get(), width=WidthLabelStyle.get())
            .pack(pady=int(PaddingYLabelEntry.get()), padx=int(PaddingXLabelEntry.get()),
                  side=SideLabelCombobox.get()))

            for i in range(len(self.ElementDict["Buttons"]) + 1):
                self.ElementDict["Buttons"][str(i)] = {
                    "text": LabelTextEntry.get(),
                    "bg": self.ElementColor,
                    "fg": FgLabelEntry.get(),
                    "font": ("Arial", int(FontLabelEntry.get())),
                    "wraplength": WrapLabelValue.get(),
                    "underline": UnderlineLabelStyle.get(),
                    "relief": ReliefLabelCombobox.get(),
                    "border": int(BorderWidthLabelEntry.get()),
                    "pady": int(PaddingYLabelEntry.get()),
                    "padx": int(PaddingXLabelEntry.get()),
                    "side": SideLabelCombobox.get()
                }

            self.ApplicationTree.insert("", END, text=f"Label {len(self.ElementDict["Labels"])}")

            print(self.ElementDict["Labels"])

        LabelApp = Tk()
        LabelApp.title("AppMaker - Create Label")
        LabelApp.geometry("400x350")

        Label(LabelApp, text="Text of the button:").pack()
        LabelTextEntry = Entry(LabelApp)
        LabelTextEntry.pack()

        Label(LabelApp, text="Background color of the Button:").pack()
        BgLabelEntry = Button(LabelApp, text="Choose color",
                              command=ColorChooser)
        BgLabelEntry.pack()

        Label(LabelApp, text="Couleur du texte (fg):").pack()
        FgLabelEntry = Entry(LabelApp)
        FgLabelEntry.pack()

        Label(LabelApp, text="Taille de la police:").pack()
        FontLabelEntry = Entry(LabelApp)
        FontLabelEntry.pack()

        Label(LabelApp, text="Wrap of the Button:").pack()
        WrapLabelValue = Spinbox(LabelApp, from_=0, to=128)
        WrapLabelValue.pack()

        Label(LabelApp, text="Underline of the Label:").pack()
        UnderlineLabelStyle = Spinbox(LabelApp, from_=-1, to=5)
        UnderlineLabelStyle.pack()

        Label(LabelApp, text="Width of the Label:").pack()
        WidthLabelStyle = Spinbox(LabelApp, from_=0, to=256)
        WidthLabelStyle.pack()

        Label(LabelApp, text="Relief of the Label:").pack()
        ReliefLabelCombobox = Combobox(LabelApp, state="readonly", values=[FLAT, GROOVE, RAISED, RIDGE, SUNKEN])
        ReliefLabelCombobox.pack()

        Label(LabelApp, text="Border width:").pack()
        BorderWidthLabelEntry = Spinbox(LabelApp, from_=0, to=64)
        BorderWidthLabelEntry.pack()

        Label(LabelApp, text="Side of the label:").pack()
        SideLabelCombobox = Combobox(LabelApp, state="readonly", values=[LEFT, RIGHT, TOP, BOTTOM])
        SideLabelCombobox.pack()

        Label(LabelApp, text="Padding Y:").pack()
        PaddingYLabelEntry = Entry(LabelApp)
        PaddingYLabelEntry.pack()

        Label(LabelApp, text="Padding X:").pack()
        PaddingXLabelEntry = Entry(LabelApp)
        PaddingXLabelEntry.pack()

        create_label_btn = Button(LabelApp, text="Create label", command=create_label)
        create_label_btn.pack(pady=20)

        LabelApp.mainloop()

    def RunPreview(self):
        self.addReturn(f"Preview is running - {str(datetime.date.today())}")
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

            (Label(PreviewApp, text=self.ElementDict["Labels"][str(i)]["text"])
             .pack(side=self.ElementDict["Labels"][str(i)]["side"],
                   padx=self.ElementDict["Labels"][str(i)]["padx"], pady=self.ElementDict["Labels"][str(i)]["pady"]))

        PreviewApp.mainloop()



    def SavedAsProject(self):
        saveAsFile = asksaveasfile(initialfile=f'{self.ProjectName}.appmaker', defaultextension=".appmaker",
                                        filetypes=[("AppMaker Project Files", "*.appmaker"),
                                                   ("All Files", "*.*")])

        saveAsFile.write(str(self.ElementDict))

        messagebox.showinfo("AppMaker", "Project saved !")


if __name__ == "__main__":
    AppMaker()
