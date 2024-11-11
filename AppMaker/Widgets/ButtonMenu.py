import customtkinter as ctk
from AppMaker.Widgets.SpinBox import SpinBox
from tkinter import *

class ButtonMenu(ctk.CTk):
    def __init__(self, ElementDict):
        super().__init__()
        self.title("AppMaker - Create Button")
        self.geometry("400x350")
        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")
        self.ElementDict = ElementDict

        ctk.CTkLabel(self, text="Text of the button:").pack()
        self.ButtonTextEntry = ctk.CTkEntry(self)
        self.ButtonTextEntry.pack()

        ctk.CTkLabel(self, text="Background color of the Button:").pack()
        self.BgButtonEntry = ctk.CTkEntry(self)
        self.BgButtonEntry.pack()

        ctk.CTkLabel(self, text="Couleur du texte (fg):").pack()
        self.FgButtonEntry = ctk.CTkEntry(self)
        self.FgButtonEntry.pack()

        ctk.CTkLabel(self, text="Taille de la police:").pack()
        self.FontButtonEntry = ctk.CTkEntry(self)
        self.FontButtonEntry.pack()

        ctk.CTkLabel(self, text="State of the Button:").pack()
        self.StateButtonValue = ctk.CTkComboBox(self, state="readonly", values=[NORMAL, DISABLED])
        self.StateButtonValue.pack()

        ctk.CTkLabel(self, text="Relief of the Button:").pack()
        self.ReliefButtonStyle = ctk.CTkComboBox(self, state="readonly", values=[FLAT, GROOVE, RAISED, RIDGE, SUNKEN])
        self.ReliefButtonStyle.pack()

        ctk.CTkLabel(self, text="Width:").pack()
        self.WidthButtonEntry = ctk.CTkEntry(self)
        self.WidthButtonEntry.pack()

        ctk.CTkLabel(self, text="Border width:").pack()
        self.BorderWidthButtonEntry = ctk.CTkEntry(self)
        self.BorderWidthButtonEntry.pack()

        ctk.CTkLabel(self, text="Side of the Button:").pack()
        self.SideButtonStyle = ctk.CTkComboBox(self, state="readonly", values=[LEFT, RIGHT, TOP, BOTTOM, CENTER, NONE])
        self.SideButtonStyle.pack()

        ctk.CTkLabel(self, text="Padding Y:").pack()
        self.PaddingYButtonEntry = ctk.CTkEntry(self)
        self.PaddingYButtonEntry.pack()

        ctk.CTkLabel(self, text="Padding X:").pack()
        self.PaddingXButtonEntry = SpinBox(self, width=250)
        self.PaddingXButtonEntry.pack(fill=BOTH, padx=20)

        self.FunctionButtonEntry = ctk.CTkEntry(self)
        self.FunctionButtonEntry.pack(pady=5)

        create_button_btn = ctk.CTkButton(self, text="Create button", command=lambda: ...)
        create_button_btn.pack(pady=20)

        self.mainloop()


    def CreateButton(self):
        for i in range(len(self.ElementDict["Buttons"]) + 1):
            self.ElementDict["Buttons"][str(i)] = {
                "text": self.ButtonTextEntry.get(),
                "bg": self.BgButtonEntry.get(),
                "fg": self.FgButtonEntry.get(),
                "font": ("Arial", int(self.FontButtonEntry.get())),
                "state": self.StateButtonValue.get(),
                "relief": self.ReliefButtonStyle.get(),
                "width": int(self.WidthButtonEntry.get()),
                "border": int(self.BorderWidthButtonEntry.get()),
                "pady": int(self.PaddingYButtonEntry.get()),
                "padx": int(self.PaddingXButtonEntry.get()),
                "side": self.SideButtonStyle.get(),
                "command": self.FunctionButtonEntry.get()
            }

        return self.ElementDict
