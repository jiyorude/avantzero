from utils.DANLY import DANLY
from utils.DATAGEN import DATAGEN
from utils.DEPGEN import DEPGEN
from utils.PROJM import PROJM
from utils.NLEGEN import NLEGEN
from utils.UTILITIES import UTILS
import utils.TEXTS as AVZTX
import os, tkinter, time, sys
from tkinter import font, ttk

class SYSTEM:
    COREDANLY, COREDATAGEN, COREDEPGEN, COREPROJM, CORENLEGEN, COREUTILS = DANLY, DATAGEN, DEPGEN, PROJM, NLEGEN, UTILS 
    
    def __init__(self):
        self.splash_window = None
        self.splash_label = None
        self.creator_label = None
        self.status_label = None
        self.version_label = None
        self.progress = None
        self.license_label = None
    
    def center_window(self, window: str, width=500, height=500):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        window.geometry(f"{width}x{height}+{x}+{y}") 
    
    # ADD FIXES FOR SHOW SPLASH 
    def show_splash(self, initext: str, font_name: str, size: int, width=500, height=500, version: str = "", copyright: str = ""):
        self.splash_window = tkinter.Tk()
        self.splash_window.overrideredirect(True)
        self.center_window(self.splash_window, width, height)
        self.splash_window.configure(bg="#2b2b2b")

        # Logo / Title in center
        splash_font = font.Font(family=font_name, size=size, weight="bold")
        self.splash_label = tkinter.Label(
            self.splash_window,
            text=initext,
            fg="white",
            bg="#2b2b2b",
            font=splash_font
        )
        self.splash_label.pack(expand=True)

        # Creator + copyright (stacked bottom-left)
        self.creator_label = tkinter.Label(
            self.splash_window,
            text="Created by A Pixelated Point of View",
            fg="#fafafa",
            bg="#2b2b2b",
            font=font.Font(size=9)
        )
        self.creator_label.place(relx=0.01, rely=0.87, anchor="sw")

        self.license_label = tkinter.Label(
            self.splash_window,
            text=copyright if copyright else "Licensed under MIT",
            fg="#fafafa",
            bg="#2b2b2b",
            font=font.Font(size=9)
        )
        self.license_label.place(relx=0.01, rely=0.91, anchor="sw")

        # Status text bottom-left
        self.status_label = tkinter.Label(
            self.splash_window,
            text="Starting...",
            fg="white",
            bg="#2b2b2b",
            font=font.Font(size=10)
        )
        self.status_label.place(relx=0.01, rely=0.97, anchor="sw")

        # Version bottom-right
        self.version_label = tkinter.Label(
            self.splash_window,
            text=version,
            fg="white",
            bg="#2b2b2b",
            font=font.Font(size=10)
        )
        self.version_label.place(relx=0.99, rely=0.97, anchor="se")

        # Progress bar just above bottom items
        self.progress = ttk.Progressbar(
            self.splash_window,
            orient="horizontal",
            length=width - 40,
            mode="determinate"
        )
        self.progress.place(relx=0.5, rely=0.93, anchor="s")

        self.splash_window.update()

    def check_folder_structure(self):
        try:
            if not os.path.exists(os.path.join(os.path.expanduser("~"), "Documents", "AvantZero")):
                os.makedirs(os.path.join(os.path.expanduser("~"), "Documents", "AvantZero"))
                with open(os.path.join(os.path.expanduser("~"), "Documents", "AvantZero", '_AvantZero_Documentation.url'), 'w') as file:
                    file.write(f"[InternetShortcut]\nURL=https://avantzero-docs.vercel.app")
            else:
                return True
        except PermissionError:
            err = UTILS.show_error('004A')
            return err
        except Exception:
            err = UTILS.show_error('004B')
            return err

    def check_dependencies(self):
        return True
    
    def update_splash(self, text: str, font_name: str, font_size: int, progress_val: int, status_text=""):
        if self.splash_window and self.splash_label:
            splash_font = font.Font(family=font_name, size=font_size, weight="bold")
            self.splash_label.config(text=text, font=splash_font)
            self.status_label.config(text=status_text)
            if self.progress:
                self.progress["value"] = progress_val
            self.splash_window.update_idletasks()

    def remove_splash(self):
        if self.splash_window:
            self.splash_window.destroy()
            self.splash_window = None
            self.splash_label = None
            self.status_label = None
            self.version_label = None
            self.progress = None    
    
    def check_packages(self):
        return True
    
    def main_menu(self):
        print("You made it to the main menu!")
        return False

    
    def boot_project_manager(self):
        print("Booting Project Manager...")
        time.sleep(1)
        return True
    
    def boot_data_generator(self):
        print("Booting Data Generator...")
        time.sleep(1)
        return True
    
    def boot_about(self):
        print("Booting about...")
        time.sleep(1)
        return True
    
    def boot_credits(self):
        print("Booting Credits...")
        time.sleep(1)
        return True
    
    def exit_avantzero(self, code):
        print("Exiting AvantZero...")
        time.sleep(2)
        sys.exit(code)