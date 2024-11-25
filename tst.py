import tkinter as tk
from customtkinter import *
from CTkTable import CTkTable


root = ctk_tk.CTk()


"""
Код добавления кнопки в конкретную ячейку
"""
"""
main_frame = CTkFrame(root)

table = CTkTable(scrollable_frame, row=5, column=10)
btn = CTkButton(table.inside_frame, text="Hi")
btn.grid(column=1, row=1)
table.grid(row=0, column=0)
scrollable_frame.grid(column=0, row=0)
scrollable_frame.grid(row=0, column=0)
root.mainloop()
"""


import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkButton, CTkScrollbar
from CTkTable import CTkTable

root = CTk()
root.geometry("600x400")

# Основной фрейм
main_frame = CTkFrame(root)
main_frame.grid(row=0, column=0)

# Canvas для прокрутки
canvas = tk.Canvas(main_frame, highlightthickness=0)
canvas.grid(row=0, column=0, sticky="nsew")

# Скроллбары
v_scrollbar = CTkScrollbar(main_frame, orientation="vertical", command=canvas.yview)
v_scrollbar.grid(row=0, column=1, sticky="ns")

h_scrollbar = CTkScrollbar(main_frame, orientation="horizontal", command=canvas.xview)
h_scrollbar.grid(row=1, column=0, sticky="ew")

# Привязка скроллбаров к Canvas
canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

# Создаем фрейм внутри Canvas
scrollable_frame = CTkFrame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nwse")

# Добавляем таблицу в прокручиваемый фрейм
table = CTkTable(scrollable_frame, row=25, column=20)
table.grid(column=0, row=0)

# Добавляем кнопку в конкретную ячейку
button = CTkButton(table.inside_frame, text="Hi")
button.grid(row=1, column=1)

# Настройка динамического изменения области прокрутки
def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", update_scroll_region)

# Настройка масштабирования при изменении размеров окна
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

root.mainloop()
