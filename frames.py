from customtkinter import *
from admin import *


class ScreenFrame:
    def __init__(self, width, height, frame: CTkFrame):
        self.width = width
        self.height = height
        self.BASE_FONT_SETTINGS = CTkFont(size=23)
        self.frame = frame    

    def clear_frame(self):
        for widget in self.frame.winfo_children:
            widget.destroy()


class MainScreenFrame(ScreenFrame):
    def set_mainscreen_grid_configure(self):
        rows = [0.1, 0.2, 0.1, 0.2, 0.1, 1]
        columns = [1]
        for row_ind in range(len(rows)):
            self.frame.grid_rowconfigure(row_ind, minsize=1, pad=1, weight=100)

        for col_ind in range(len(columns)):
            self.frame.grid_columnconfigure(col_ind, minsize=self.width*columns[col_ind], weight=100)

    def show_main_screen(self):
        header = CTkLabel(text="Список таблиц")
        


class StartScreenFrame(ScreenFrame):
    def set_startscreen_grid_configure(self):
        rows = [0.1, 0.2, 0.1, 0.2, 0.1, 1]
        columns = [1]
        for row_ind in range(len(rows)):
            self.frame.grid_rowconfigure(row_ind, minsize=1, pad=1, weight=100)

        for col_ind in range(len(columns)):
            self.frame.grid_columnconfigure(col_ind, minsize=self.width*columns[col_ind], weight=100)

    def show_start_screen(self):
        login_label = CTkLabel(self.frame, text="Логин", text_color="#ffffff", bg_color=BASE_BACKGROUND_COLOR, font=self.BASE_FONT_SETTINGS)
        password_label = CTkLabel(self.frame, text="Пароль", bg_color=BASE_BACKGROUND_COLOR,text_color="#ffffff", font=self.BASE_FONT_SETTINGS)
        db_input = CTkEntry(self.frame, bg_color=BASE_BACKGROUND_COLOR)
        password_input = CTkEntry(self.frame, bg_color=BASE_BACKGROUND_COLOR)
        entry_btn = CTkButton(self.frame, text="Войти", bg_color=BASE_BACKGROUND_COLOR, font=self.BASE_FONT_SETTINGS)

        login_label.grid(row=1, column=0, pady=30, ipady=10)
        db_input.grid(row=2, column=0, pady=0, sticky='we', padx=120)
        password_label.grid(row=3, column=0, ipady=40)
        password_input.grid(row=4, column=0, sticky='we', padx=120)
        entry_btn.grid(row=5, column=0, pady=100)