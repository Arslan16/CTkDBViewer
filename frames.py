from customtkinter import *
from admin import *
from models import *
from CTkTable import CTkTable


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
        for model_ind in range(len(l_models)):
            CTkButton(tables_frame, font=self.BASE_FONT_SETTINGS, text=l_models[model_ind].__tablename__).grid(row=model_ind, column=0, sticky="we")


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
        ...

    def show_screen(self):
        ...














