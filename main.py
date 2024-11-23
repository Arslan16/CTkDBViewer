from customtkinter import *


from frames import *
from admin import *
from models import *


class App(ctk_tk.CTk):
    def __init__(self, width, height):
        super().__init__()
        self.BASE_FONT_SETTINGS = CTkFont(size=23)
        self.width = width
        self.height = height
        self.columnconfigure(0, minsize=self.width, weight=self.width)
        self.rowconfigure(0, minsize=self.height, weight=self.height)
        self.geometry(f"{self.width}x{self.height}")
        self.grid_columnconfigure(0, minsize=self.width)
        self.grid_rowconfigure(0, minsize=self.height)
        self.screen = StartScreenFrame(width=self.width, height=self.height, frame=CTkFrame(self))
        self.screen.frame._set_appearance_mode("dark")
        self.screen.frame.grid(row=0, column=0, sticky="nswe")
        self._set_appearance_mode("dark")
        self.screen.set_startscreen_grid_configure()
        self.screen.show_start_screen()
    

if __name__ == "__main__":
    Base.metadata.create_all
    app = App(500, 500)
    app.mainloop()


