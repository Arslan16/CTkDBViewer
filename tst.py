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

create_button = CTkButton(frame, text="Создать")
create_button.grid(row=0, column=0, sticky="nswe")

canvas_frame = CTkFrame(frame, width=width, bg_color=BASE_BACKGROUND_COLOR)
canvas_frame.grid(column=0, row=1, sticky="nswe")
canvas = tk.Canvas(canvas_frame, highlightthickness=0, width=width, bg=BASE_BACKGROUND_COLOR)
canvas.grid(row=0, column=0, sticky="nsew")
canvas_frame.grid_columnconfigure(0, minsize=width, weight=100)
canvas_frame.grid_rowconfigure(0, minsize=height, weight=100)

# Скроллбары
v_scrollbar = CTkScrollbar(canvas_frame, orientation="vertical", command=canvas.yview)
v_scrollbar.grid(row=0, column=1, sticky="ns")

h_scrollbar = CTkScrollbar(canvas_frame, orientation="horizontal", command=canvas.xview)
h_scrollbar.grid(row=1, column=0, sticky="ew")

# Привязка скроллбаров к Canvas
canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

# Создаем фрейм внутри Canvas
scrollable_frame = CTkFrame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="center")

# Добавляем таблицу в прокручиваемый фрейм
table = CTkTable(scrollable_frame, row=1, column=len(Employee.__table__.columns))
table.grid(column=0, row=0, sticky="nswe")

# Добавляем кнопку в конкретную ячейку
# button = CTkButton(table.inside_frame, text="Hi")
# button.grid(row=1, column=1)

# Настройка динамического изменения области прокрутки
def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", update_scroll_region)

# Настройка масштабирования при изменении размеров окна
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)


headers = [column.name for column in Employee.__table__.columns]
l_tuples = get_data_from_table(Employee) 
for i in range(len(headers)):
    table.insert(row=table.rows-1, column=i, value=headers[i])
for dict_tpl in l_tuples:
    table.add_row([])
    for i in range(len(dict_tpl.keys())):
        table.insert(row=table.rows-1, column=i, value=list(dict_tpl.values())[i])    
    
root.mainloop()