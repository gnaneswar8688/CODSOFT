import customtkinter as ctk

from modules.ui import CalculatorUI

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()

root.title(
    "Professional Calculator"
)

root.geometry(
    "430x650"
)

root.configure(
    fg_color="#050b18"
)

root.resizable(
    False,
    False
)

CalculatorUI(root)

root.mainloop()