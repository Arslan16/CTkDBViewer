import tkinter as tk
from customtkinter import *
from CTkTable import CTkTable
from PIL.Image import Image

from admin import *
from models import *
from utils import *


class MCTkButton(CTkButton):
    def __init__(self, tablename: str, dict_values: dict, dict_columns: dict, *args, **kwargs):
        self.tablename = tablename
        self.dict_values = dict_values
        self.dict_columns = dict_columns
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
        self.win = CTkToplevel(self.frame)
        self.win.title("Внимание!")
        self.win.geometry("300x400")
        self.win.grid_columnconfigure(0, minsize=300)
        self.win.rowconfigure(0, minsize=400)
        self.scroll_warning = CTkScrollableFrame(self.win, width=300, height=400)
        self.warning_label = CTkLabel(self.scroll_warning, text=v_in_text, width=300, font=self.BASE_FONT_SETTINGS)
        self.warning_label.grid(row=0, column=0, sticky='nswe')
        self.scroll_warning.grid(column=0, row=0, sticky="nswe")


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
        self.l_btns = list() 
        dict_columns = {column.name : column for column in model.__table__.columns}
        
        self.create_button = MCTkButton(tablename=model.__tablename__, dict_values={key: "" for key, value in dict_columns.items()}, dict_columns=dict_columns, master=self.frame, font=self.BASE_FONT_SETTINGS, text="Создать")
        self.create_button.grid(row=0, column=0, sticky="nswe", pady=5)

        self.back_button = CTkButton(self.frame, font=self.BASE_FONT_SETTINGS, text="Назад к списку")
        self.back_button.grid(row=1, column=0, sticky="nswe", pady=5)

        self.table_header = CTkLabel(self.frame, text=f"Таблица {model.__tablename__}", font=self.BASE_FONT_SETTINGS)
        self.table_header.grid(row=2, column=0, sticky="we")

        self.canvas_frame = CTkFrame(self.frame, bg_color=BASE_BACKGROUND_COLOR)
        self.canvas_frame.grid(column=0, rowspan=2, row=3, sticky="nswe", pady=1)

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

        # Добавляем таблицу в прокручиваемый фрейм
        self.table = CTkTable(self.scrollable_frame, row=len(l_tuples) + 1, column=len(model.__table__.columns) + 1)
        self.table.grid_columnconfigure(0, weight=1)
        self.table.grid(column=0, row=0, sticky="nsew", pady=1)

        # Настройка динамического изменения области прокрутки
        self.scrollable_frame.bind("<Configure>", self.update_scroll_region)

        # Заполнение таблицы данными
        self.feel_table(model.__tablename__, dict_columns, l_tuples)

    def update_scroll_region(self, event):
        # Обновляем область прокрутки канваса
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def feel_table(self, tablename: str, dict_columns_old: dict, l_tuples: list[dict]):
        dict_columns = {"R": None}
        dict_columns.update(dict_columns_old)
        for i in range(len(dict_columns.keys())):
            self.table.insert(row=0, column=i, value=dict_columns.get(list(dict_columns.keys())[i]))

        for tup_index in range(len(l_tuples)):
            current_row_index = tup_index + 1
            btn = MCTkButton(tablename=tablename, dict_values=l_tuples[tup_index], 
                             dict_columns=dict_columns,
                             master=self.table.inside_frame, text="Подробнее")
            btn.grid(column=0, row=current_row_index)
            self.l_btns.append(btn)
            for i in range(len(l_tuples[tup_index].keys())):
                self.table.insert(row=current_row_index, column=(i + 1), value=list(l_tuples[tup_index].values())[i])


class EditScreenFrame(ScreenFrame):
    rows = dict()
    tablename: str
    back_button: CTkButton
    model: Model
    row_id: int

    def set_grid_configure(self):
        rows = [0.1, 0.1, 0.95, 0.1]
        columns = [1]

        for row_ind in range(len(rows)):
            self.frame.grid_rowconfigure(row_ind, minsize=self.height*rows[row_ind], pad=1, weight=100)

        for col_ind in range(len(columns)):
            self.frame.grid_columnconfigure(col_ind, minsize=self.width*columns[col_ind], weight=100)
    
    def try_delete_row(self, model: Model, row_id: int) -> bool:
        try:
            with Session(DB_ENGINE) as session:
                session.execute(delete(model).where(model.id == row_id))
                session.commit()
            return True
        except Exception as e:
            session.rollback()
            err = get_error_by_traceback(str(e))
            self.show_warning(err)
            return False
        
    def try_save(self, model: Model):
        dict_data = {label.cget("text"): entry.get() for label, entry in self.rows.items()}
        try: 
            save = dict_save_functions.get(model)
            save(dict_data)
            print("frames.py:218 try_save() Успешно!")
            self.show_warning("Успешно!")
        except Exception as e:
            err = get_error_by_traceback(str(e))
            self.show_warning(err)

    def save_file(self, label):
        file = filedialog.askopenfile(
            defaultextension=None,
            filetypes=[("All files", "*.*")],
            title="Выбрать файл"
        )

        if file:
            file_path = file.name  # Получаем путь к выбранному файлу
            file_size = os.path.getsize(file_path) # В байтах
            if file_size > (512 * 1024): # Больше 512 МБ
                self.show_warning("Размер файла слишком большой!")
                return
            entry = CTkEntry(self.scrollable_frame)
            entry.insert(0, str(file.read()))
            self.rows[label] = entry

    def show_screen(self, model: Model, dict_columns: dict, dict_values: dict):
        self.model = model
        self.rows = dict()
        self.save_btn = CTkButton(self.frame, text="Сохранить", font=self.BASE_FONT_SETTINGS, command=lambda: self.try_save(model))
        self.delete_btn = CTkButton(self.frame, font=self.BASE_FONT_SETTINGS, text="Удалить")

        self.save_btn.grid(column=0, row=0, sticky="nswe", padx=5, pady=5)
        self.delete_btn.grid(column=0, row=1, sticky="nswe", padx=5, pady=5)

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
        for column_name, column_value in dict_values.items():
            label = CTkLabel(self.scrollable_frame, font=self.BASE_FONT_SETTINGS, text=column_name)
            label.grid(row=counter, column=0, sticky="we")
            entry = CTkEntry(self.scrollable_frame, font=self.BASE_FONT_SETTINGS) if type(dict_columns.get(column_name).type) != VARBINARY else CTkButton(self.scrollable_frame, text=f"Выбрать файл", command=lambda: self.save_file(label))
            entry.grid(row=counter, column=1, sticky="we")
            if type(dict_columns.get(column_name).type) != VARBINARY: 
                entry.insert(0, str(column_value))
                self.rows[label] = entry
            counter += 1
        
        self.back_button = CTkButton(self.frame, text="Назад", font=self.BASE_FONT_SETTINGS)
        self.back_button.grid(row=3, column=0, sticky="we")

