import tkinter as tk
from customtkinter import *
from CTkTable import CTkTable
from PIL.Image import Image

from admin import *
from models import *
from utils import *


class MCTkButton(CTkButton):
    def __init__(self, tablename, dict_values, *args, **kwargs):
        self.tablename = tablename
        self.dict_values = dict_values
        super().__init__(*args, **kwargs)


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

    def show_warning(self, v_in_text: str):
        self.win = CTkToplevel(self)
        self.win.title("Внимание!")
        self.win.geometry("300x150")
        self.win.grid_columnconfigure(0, minsize=300)
        self.win.rowconfigure(0, minsize=150)
        self.warning_label = CTkLabel(self.win, font=self.BASE_FONT_SETTINGS, text=v_in_text)
        self.warning_label.grid(row=0, column=0, sticky='nswe')


class MainScreenFrame(ScreenFrame):
    l_btns:list[CTkButton] = list()

    def set_grid_configure(self):
        rows = [0.2, 0.8]
        columns = [1]
        for row_ind in range(len(rows)):
            self.frame.grid_rowconfigure(row_ind, minsize=self.height*rows[row_ind], pad=1, weight=1000)

        for col_ind in range(len(columns)):
            self.frame.grid_columnconfigure(col_ind, minsize=self.width*columns[col_ind], weight=100)

    def show_screen(self):
        self.l_btns = list()
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
    l_btns:list[MCTkButton] = list()

    def set_grid_configure(self):
        rows = [0.1, 0.1, 0.15, 0.4, 0.05]
        columns = [1]

        for row_ind in range(len(rows)):
            self.frame.grid_rowconfigure(row_ind, minsize=self.height*rows[row_ind], pad=1, weight=100)

        for col_ind in range(len(columns)):
            self.frame.grid_columnconfigure(col_ind, minsize=self.width*columns[col_ind], weight=100)


    def show_screen(self, model: Model):
        # Создание кнопок

        self.create_button = CTkButton(self.frame, text="Создать")
        self.create_button.grid(row=0, column=0, sticky="nswe", pady=5)

        self.back_button = CTkButton(self.frame, text="Назад к списку")
        self.back_button.grid(row=1, column=0, sticky="nswe", pady=5)

        self.table_header = CTkLabel(self.frame, text=f"Таблица {model.__tablename__}", font=self.BASE_FONT_SETTINGS)
        self.table_header.grid(row=2, column=0, sticky="we")

        self.canvas_frame = CTkFrame(self.frame, bg_color=BASE_BACKGROUND_COLOR)
        self.canvas_frame.grid(column=0, row=3, sticky="nswe", pady=1)

        # Создаем Canvas
        self.canvas = tk.Canvas(self.canvas_frame, highlightthickness=0, bg=BASE_BACKGROUND_COLOR)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Настройка конфигурации Canvas
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_columnconfigure(0, weight=1)

        # Скроллбары
        self.v_scrollbar = CTkScrollbar(self.canvas_frame, orientation="vertical", command=self.canvas.yview, width=20)
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")

        self.h_scrollbar = CTkScrollbar(self.canvas_frame, orientation="horizontal", command=self.canvas.xview)
        self.h_scrollbar.grid(row=1, column=0, sticky="ew")

        # Привязка скроллбаров к Canvas
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

        # Создаем фрейм внутри Canvas
        self.scrollable_frame = CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Настройка конфигурации внутри scrollable_frame
        self.scrollable_frame.grid_rowconfigure(0, weight=1)  # Позволяем строке растягиваться
        self.scrollable_frame.grid_columnconfigure(0, weight=1)  # Позволяем столбцу растягиваться
        l_tuples = get_data_from_table(model)
        headers = [column.name for column in model.__table__.columns]
        headers.insert(0, "R:")
        # Добавляем таблицу в прокручиваемый фрейм
        self.table = CTkTable(self.scrollable_frame, row=len(l_tuples) + 1, column=len(model.__table__.columns) + 1)
        self.table.grid_columnconfigure(0, weight=1)
        self.table.grid(column=0, row=0, sticky="nsew", pady=10)

        # Настройка динамического изменения области прокрутки
        self.scrollable_frame.bind("<Configure>", self.update_scroll_region)

        # Заполнение таблицы данными
        self.feel_table(model.__tablename__, headers, l_tuples)

    def update_scroll_region(self, event):
        # Обновляем область прокрутки канваса
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def feel_table(self, tablename, headers, l_tuples):
        for i in range(len(headers)):
            self.table.insert(row=0, column=i, value=headers[i])

        for tup_index in range(len(l_tuples)):
            current_row_index = tup_index + 1
            btn = MCTkButton(tablename=tablename, dict_values=l_tuples[tup_index], master=self.table.inside_frame, text="Подробнее")
            btn.grid(column=0, row=current_row_index)
            self.l_btns.append(btn)
            for i in range(len(l_tuples[tup_index].keys())):
                self.table.insert(row=current_row_index, column=(i + 1), value=list(l_tuples[tup_index].values())[i])


class EditScreenFrame(ScreenFrame):
    rows = dict()
    tablename: str

    def set_grid_configure(self):
        rows = [0.2, 0.2, 0.6]
        columns = [1]

        for row_ind in range(len(rows)):
            self.frame.grid_rowconfigure(row_ind, minsize=self.height*rows[row_ind], pad=1, weight=100)

        for col_ind in range(len(columns)):
            self.frame.grid_columnconfigure(col_ind, minsize=self.width*columns[col_ind], weight=100)
    
    def try_save(self, model: Model):
        dict_data = {label.text : entry.get for label, entry in self.rows.items()}
        try: 
            save_to_table(model, dict_data)
            self.show_warning("Успешно!")
        except Exception as e:
            err = get_error_by_traceback(str(e))
            self.show_warning(err)

    def show_screen(self, model: Model, dict_values: dict):
        self.save_btn = CTkButton(self.frame, text="Сохранить", command=lambda e: self.try_save(model))
        self.delete_btn = CTkButton(self.frame, text="Удалить")

        self.save_btn.grid(column=0, row=0, sticky="nswe", padx=5)
        self.save_btn.grid(column=0, row=1, sticky="nswe", padx=5)

        self.canvas_frame = CTkFrame(self.frame, bg_color=BASE_BACKGROUND_COLOR)
        self.canvas_frame.grid(column=0, row=2, sticky="nswe", pady=1)

        # Создаем Canvas
        self.canvas = tk.Canvas(self.canvas_frame, highlightthickness=0, bg=BASE_BACKGROUND_COLOR)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Настройка конфигурации Canvas
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_columnconfigure(0, weight=1)

        # Скроллбары
        self.v_scrollbar = CTkScrollbar(self.canvas_frame, orientation="vertical", command=self.canvas.yview, width=20)
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")

        self.h_scrollbar = CTkScrollbar(self.canvas_frame, orientation="horizontal", command=self.canvas.xview)
        self.h_scrollbar.grid(row=1, column=0, sticky="ew")

        # Привязка скроллбаров к Canvas
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

        # Создаем фрейм внутри Canvas
        self.scrollable_frame = CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Настройка конфигурации внутри scrollable_frame
        self.scrollable_frame.grid_columnconfigure(0, minsize=self.width/2, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, minsize=self.width/2, weight=1)

        counter = 0
        for key, item in dict_values.items():
            label = CTkLabel(self.scrollable_frame, text=key)
            label.grid(row=counter, column=0, sticky="we")
            entry = CTkEntry(self.scrollable_frame)
            entry.grid(row=counter, column=1, sticky="we")
            entry.insert(0, str(item))
            self.rows[label] = entry

            counter += 1