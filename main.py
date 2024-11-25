from customtkinter import *


from frames import *
from admin import *
from models import *


class WindowsManager:
    def __init__(self, login_frame: LoginScreenFrame, main_frame: MainScreenFrame, table_frame: TableScreenFrame):
        self.start_screen_frame = login_frame
        self.main_frame = main_frame
        self.table_frame = table_frame        

    def show_start_window(self):
        self.start_screen_frame.clear_frame()
        self.start_screen_frame.set_grid_configure()
        self.start_screen_frame.show_screen()

    def show_main_window(self):
        self.main_frame.clear_frame()
        self.main_frame.set_grid_configure()
        self.main_frame.show_screen()

    def show_table_window(self):
        ...


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
            table_frame=TableScreenFrame(self.width, self.height, self.screen)
        )
        self.columnconfigure(0, minsize=self.width, weight=self.width)
        self.rowconfigure(0, minsize=self.height, weight=self.height)
        self.geometry(f"{self.width}x{self.height}")
        self.grid_columnconfigure(0, minsize=self.width)
        self.grid_rowconfigure(0, minsize=self.height)
        self.screen.grid(column=0, row=0, sticky="nswe")
        self._set_appearance_mode("dark")
        self.windows_manager.show_start_window()
        self.windows_manager.start_screen_frame.entry_btn.bind("<Button-1>", self.autentificate)
        print("aa")

    def autentificate(self, event=None):
        login = self.windows_manager.start_screen_frame.db_input.get()
        password = self.windows_manager.start_screen_frame.password_input.get()
        if login == "Arslan" and password == "TestPassword":
            print("auth complete")
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
    app = App(500, 500)
    app.mainloop()
