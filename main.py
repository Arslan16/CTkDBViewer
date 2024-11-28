from customtkinter import *
from functools import partial

from frames import *
from admin import *
from models import *
CTk

class WindowsManager:
    def __init__(self, login_frame: LoginScreenFrame, main_frame: MainScreenFrame, 
                 table_frame: TableScreenFrame, edit_frame: EditScreenFrame):
        self.start_screen_frame = login_frame
        self.main_frame = main_frame
        self.table_frame = table_frame
        self.edit_frame = edit_frame        

    def show_start_window(self):
        self.start_screen_frame.clear_frame()
        self.start_screen_frame.set_grid_configure()
        self.start_screen_frame.show_screen()

    def show_main_window(self):
        self.main_frame.clear_frame()
        self.main_frame.set_grid_configure()
        self.main_frame.show_screen()
        for main_btn in self.main_frame.l_btns:
            main_btn.unbind("<Button-1>")
            model = dict_models.get(main_btn.cget("text"))
            main_btn.bind("<Button-1>", lambda e, model=model: self.show_table_window(model))

    def show_table_window(self, model: Model, event=None):
        self.table_frame.clear_frame()
        self.table_frame.set_grid_configure()
        self.table_frame.show_screen(model)
        self.table_frame.back_button.unbind("<Button-1>")
        self.table_frame.back_button.bind("<Button-1>", lambda e: self.show_main_window())
        dict_values = self.table_frame.create_button.dict_values
        dict_columns = self.table_frame.create_button.dict_columns
        self.table_frame.create_button.unbind("<Button-1>")
        self.table_frame.create_button.bind("<Button-1>", lambda e, model=model, dict_columns=dict_columns, dict_values=dict_values: self.show_edit_window(model, dict_columns, dict_values))
       
        for edit_btn in self.table_frame.l_btns:
            edit_btn.unbind("<Button-1>")
            model = dict_models.get(edit_btn.tablename)
            dict_values = edit_btn.dict_values
            dict_columns = edit_btn.dict_columns
            edit_btn.bind("<Button-1>", lambda e, model=model, 
                          dict_values=dict_values, dict_columns=dict_columns: self.show_edit_window(model, dict_columns, dict_values))
            
    def show_table_after_delete(self, model: Model, row_id: int):
        successful = self.edit_frame.try_delete_row(model, row_id)
        if successful: 
            self.show_table_window(model)
            self.table_frame.table.delete_row(row_id-1)

    def show_edit_window(self, model, dict_columns: dict, dict_values: dict):
        self.edit_frame.clear_frame()
        self.edit_frame.set_grid_configure()
        self.edit_frame.show_screen(model, dict_columns, dict_values)
        self.edit_frame.back_button.unbind("<Button-1>")
        self.edit_frame.back_button.bind("<Button-1>", lambda e: self.show_table_window(self.edit_frame.model))
        self.edit_frame.delete_btn.unbind("<Button-1>")
        self.edit_frame.delete_btn.bind("<Button-1>", lambda e, model=model, row_id=dict_values.get("id"): self.show_table_after_delete(model, row_id))


class App(ctk_tk.CTk):
    def __init__(self, width, height):
        super().__init__()
        self.BASE_FONT_SETTINGS = CTkFont(size=23)
        self.width = width
        self.height = height
        self.screen = CTkFrame(self, self.width, self.height)
        self.windows_manager = WindowsManager(
            login_frame=LoginScreenFrame(self.width, self.height, self.screen),
            main_frame=MainScreenFrame(self.width, self.height, self.screen),
            table_frame=TableScreenFrame(self.width, self.height, self.screen),
            edit_frame=EditScreenFrame(self.width, self.height, self.screen)
        )
        self.columnconfigure(0, minsize=self.width, weight=self.width)
        self.rowconfigure(0, minsize=self.height, weight=self.height)
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(True, True)
        self.grid_columnconfigure(0, minsize=self.width)
        self.grid_rowconfigure(0, minsize=self.height)
        self.screen.grid(column=0, row=0, sticky="nswe")
        self._set_appearance_mode("dark")
        self.windows_manager.show_start_window()
        self.windows_manager.start_screen_frame.entry_btn.bind("<Button-1>", self.autentificate)

    def autentificate(self, event=None):
        login = self.windows_manager.start_screen_frame.db_input.get()
        password = self.windows_manager.start_screen_frame.password_input.get()
        if login == "Arslan" and password == "TestPassword":
            self.windows_manager.show_main_window()
        else:
            self.show_warning()
            
    def show_warning(self):
        self.win = CTkToplevel(self)
        self.win.title("Внимание!")
        self.win.geometry("300x150")
        self.win.grid_columnconfigure(0, minsize=300)
        self.win.rowconfigure(0, minsize=150)
        self.warning_label = CTkLabel(self.win, font=self.BASE_FONT_SETTINGS, text="Неверный логин или пароль!")
        self.warning_label.grid(row=0, column=0, sticky='nswe')


if __name__ == "__main__":
    Base.metadata.create_all
    app = App(1000, 500)
    app.mainloop()
