from tkinter import *
import customtkinter as ctk

class WindowPreview(ctk.CTkFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "My First App"
        self._corner_radius = 0

        header_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="gray30")
        header_frame.pack(fill=X)

        title_label = ctk.CTkLabel(header_frame, text=self.title, font=("Arial", 12, "bold"))
        title_label.pack(side=LEFT, padx=2, pady=5)

        closeWindow = ctk.CTkButton(header_frame, text="X", font=("Arial",8, "bold"), width=2)
        closeWindow.pack(side=RIGHT, padx=2, pady=2)

        fullscreenWindow = ctk.CTkButton(header_frame, text="□", font=("Arial", 12, "bold"), width=2)
        fullscreenWindow.pack(side=RIGHT, padx=2, pady=2)

        hideWindow = ctk.CTkButton(header_frame, text="-", font=("Arial", 10, "bold"), width=2)
        hideWindow.pack(side=RIGHT, padx=2, pady=2)


        self.button_container = ctk.CTkFrame(self, corner_radius=0)
        self.button_container.pack(fill=BOTH, expand=True)

        ctk.CTkButton(self.button_container, text="LEFT").pack(side=LEFT)

        ctk.CTkButton(self.button_container, text="TOP").pack(side=TOP)

        ctk.CTkButton(self.button_container, text="RIGHT").pack(side=RIGHT)

        ctk.CTkButton(self.button_container, text="BOTTOM").pack(side=BOTTOM)
