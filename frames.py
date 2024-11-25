import tkinter as tk
from customtkinter import *
from CTkTable import CTkTable

from admin import *
from models import *
from utils import *

class ScreenFrame:
    def __init__(self, width, height, frame: CTkFrame):
        self.width = width
        self.height = height
        self.BASE_FONT_SETTINGS = CTkFont(size=23)
        self.frame = frame
        self.BASE_FONT_SETTINGS = CTkFont(size=23)  

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


class MainScreenFrame(ScreenFrame):
    l_btns = list()

    def set_grid_configure(self):
        rows = [0.2, 0.8]
        columns = [1]
        for row_ind in range(len(rows)):
            self.frame.grid_rowconfigure(row_ind, minsize=self.height*rows[row_ind], pad=1, weight=1000)

        for col_ind in range(len(columns)):
            self.frame.grid_columnconfigure(col_ind, minsize=self.width*columns[col_ind], weight=100)

    def show_screen(self):
        header = CTkLabel(self.frame, font=self.BASE_FONT_SETTINGS, text="Список таблиц")
        header.grid(column=0, row=0, sticky="nswe")
        tables_frame = CTkScrollableFrame(self.frame)
        tables_frame.columnconfigure(0, minsize=self.width, weight=1000)
        tables_frame.grid(column=0, row=1, sticky="nswe")
        for model_ind in range(len(dict_models.keys())):
            btn = CTkButton(tables_frame, font=self.BASE_FONT_SETTINGS, 
                      text=list(dict_models.keys())[model_ind])
            btn.grid(row=model_ind, column=0, sticky="we")
            self.l_btns.append(btn)

class LoginScreenFrame(ScreenFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_grid_configure(self):
        rows = [0.1, 0.2, 0.1, 0.2, 0.1, 1]
        columns = [1]
        for row_ind in range(len(rows)):
            self.frame.grid_rowconfigure(row_ind, minsize=1, pad=1, weight=100)

        for col_ind in range(len(columns)):
            self.frame.grid_columnconfigure(col_ind, minsize=self.width*columns[col_ind], weight=100)

    def show_screen(self):
        self.login_label = CTkLabel(self.frame, text="Логин", text_color="#ffffff", bg_color=BASE_BACKGROUND_COLOR, font=self.BASE_FONT_SETTINGS)
        self.password_label = CTkLabel(self.frame, text="Пароль", bg_color=BASE_BACKGROUND_COLOR,text_color="#ffffff", font=self.BASE_FONT_SETTINGS)
        self.db_input = CTkEntry(self.frame, bg_color=BASE_BACKGROUND_COLOR)
        self.password_input = CTkEntry(self.frame, bg_color=BASE_BACKGROUND_COLOR)
        self.entry_btn = CTkButton(self.frame, text="Войти", bg_color=BASE_BACKGROUND_COLOR, font=self.BASE_FONT_SETTINGS)
        
        self.db_input.insert(0, "Arslan")
        self.password_input.insert(0, "TestPassword")

        self.login_label.grid(row=1, column=0, pady=30, ipady=10)
        self.db_input.grid(row=2, column=0, pady=0, sticky='we', padx=120)
        self.password_label.grid(row=3, column=0, ipady=40)
        self.password_input.grid(row=4, column=0, sticky='we', padx=120)
        self.entry_btn.grid(row=5, column=0, pady=100)
        

class TableScreenFrame(ScreenFrame):
    def set_grid_configure(self):
        rows = [0.1, 0.9]
        columns = [1]
        for row_ind in range(len(rows)):
            self.frame.grid_rowconfigure(row_ind, minsize=self.height*rows[row_ind], pad=1, weight=100)

        for col_ind in range(len(columns)):
            self.frame.grid_columnconfigure(col_ind, minsize=self.width*columns[col_ind], weight=100)


    def show_screen(self, model: Model):
        # Canvas для прокрутки
        self.create_button = CTkButton(self.frame, text="Создать")
        self.create_button.grid(row=0, column=0, sticky="nswe")

        self.back_button = CTkButton(self.frame, text="Назад к списку")
        self.back_button.grid(row=0, column=0, sticky="nswe")


        self.canvas_frame = CTkFrame(self.frame, width=self.width, bg_color=BASE_BACKGROUND_COLOR)
        self.canvas_frame.grid(column=0, row=1, sticky="nswe")
        self.canvas = tk.Canvas(self.canvas_frame, highlightthickness=0, width=self.width, bg=BASE_BACKGROUND_COLOR)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas_frame.grid_columnconfigure(0, minsize=self.width, weight=100)
        self.canvas_frame.grid_rowconfigure(0, minsize=self.height, weight=100)

        # Скроллбары
        self.v_scrollbar = CTkScrollbar(self.canvas_frame, orientation="vertical", command=self.canvas.yview)
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")

        h_scrollbar = CTkScrollbar(self.canvas_frame, orientation="horizontal", command=self.canvas.xview)
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        # Привязка скроллбаров к Canvas
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Создаем фрейм внутри Canvas
        scrollable_frame = CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=scrollable_frame, anchor="center")

        # Добавляем таблицу в прокручиваемый фрейм
        self.table = CTkTable(scrollable_frame, row=1, column=len(model.__table__.columns))
        self.table.grid(column=0, row=0, sticky="nswe")

        # Добавляем кнопку в конкретную ячейку
        # button = CTkButton(table.inside_frame, text="Hi")
        # button.grid(row=1, column=1)

        # Настройка динамического изменения области прокрутки
        def update_scroll_region(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        scrollable_frame.bind("<Configure>", update_scroll_region)

        # Настройка масштабирования при изменении размеров окна
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.feel_table(model)

    def feel_table(self, v_in_model):
        headers = [column.name for column in v_in_model.__table__.columns]
        print(v_in_model)
        l_tuples = get_data_from_table(v_in_model) 
        print(l_tuples)
        for i in range(len(headers)):
            self.table.insert(row=self.table.rows-1, column=i, value=headers[i])
        for dict_tpl in l_tuples:
            self.table.add_row([])
            for i in range(len(dict_tpl.keys())):
                self.table.insert(row=self.table.rows-1, column=i, value=list(dict_tpl.values())[i])    
            
