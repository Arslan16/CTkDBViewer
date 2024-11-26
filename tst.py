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



# Добавляем таблицу в прокручиваемый фрейм
table = CTkTable(frame, row=5, column=2)
table.grid(column=0, row=5, sticky="nswe")
table.add_row([])
# table.update()
for i in range(5):
    current_row = table.rows - 1
    CTkButton(table.inside_frame, text="1", command=lambda: print("Hi")).grid(column=0, row=current_row)
    #
root.mainloop()