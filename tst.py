import tkinter as tk
from CTkTable import CTkTable
from customtkinter import *

from models import *
from admin import *
from utils import *

width = 1000
height = 500
root = ctk_tk.CTk()
frame = CTkFrame(root)
root.grid_columnconfigure(0, minsize=width, weight=100)
root.grid_rowconfigure(0, minsize=height)
frame.grid(column=0, row=0, sticky="nswe")

label = CTkEntry(root)
label.insert(0, "AAAAAA")
label.grid(column=0, row=0)
print(label.get().encode("utf-8"))

root.mainloop()