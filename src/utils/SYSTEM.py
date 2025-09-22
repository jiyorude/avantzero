from utils.DANLY import DANLY
from utils.DATAGEN import DATAGEN
from utils.DEPGEN import DEPGEN
from utils.PROJM import PROJM
from utils.NLEGEN import NLEGEN
from utils.UTILITIES import UTILS
import os, tkinter, time, sys
from tkinter import font, ttk
from PIL import Image, ImageTk

class SYSTEM:
    COREDANLY, COREDATAGEN, COREDEPGEN, COREPROJM, CORENLEGEN, COREUTILS = DANLY, DATAGEN, DEPGEN, PROJM, NLEGEN, UTILS 
    
    #DONE
    def __init__(self):
        self.splash_window = None
        self.splash_label = None
        self.creator_label = None
        self.status_label = None
        self.version_label = None
        self.progress = None
        self.license_label = None
    
    #DONE
    def center_window(self, window: str, width=500, height=500):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        window.geometry(f"{width}x{height}+{x}+{y}") 
    
    #DONE
    def show_splash(self, width=500, height=500):
        self.splash_window = tkinter.Tk()
        self.splash_window.overrideredirect(True)
        self.center_window(self.splash_window, width, height)
        self.splash_window.configure(bg="#2b2b2b")
        script_dir = os.path.dirname(os.path.abspath(__file__)) 
        assets_path = os.path.join(script_dir, "..", "assets", "images", "APPOV_logo.png")
        self.logo_image = Image.open(assets_path)
        self.logo_image = self.logo_image.resize((42, 44))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tkinter.Label(
            self.splash_window,
            image=self.logo_image,
            bg="#2b2b2b"
        )
        self.logo_label.place(relx=0.0367, rely=0.0287, anchor="nw")
        splash_logofont = font.Font(family='Quantum', size=175, weight="bold")
        self.splash_label = tkinter.Label(
            self.splash_window,
            text='A',
            fg="white",
            bg="#2b2b2b",
            font=splash_logofont
        )
        self.splash_label.place(relx=0.5, rely=0.37, anchor="center")
        splash_avztext = font.Font(family='Gantari ExtraLight', size=18)
        text = "AVANTZERO"
        spaced_text = "  ".join(text)
        self.splash_logotitle = tkinter.Label(
            self.splash_window,
            text=spaced_text,
            fg="white",
            bg="#2b2b2b",
            font=splash_avztext
        )
        self.splash_logotitle.place(relx=0.494, rely=0.67, anchor="center")
        splash_loadingtext = font.Font(family='Gantari Regular', size=10)
        self.status_label = tkinter.Label(
            self.splash_window,
            text="Starting...",
            fg="white",
            bg="#2b2b2b",
            font=splash_loadingtext
        )
        self.status_label.place(relx=0.0367, rely=0.975, anchor="sw")
        self.version_label = tkinter.Label(
            self.splash_window,
            text='v0.2.0',
            fg="white",
            bg="#2b2b2b",
            font=splash_loadingtext
        )
        self.version_label.place(relx=0.967, rely=0.975, anchor="se")
        style = ttk.Style(self.splash_window)
        style.theme_use("clam")
        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor="#2b2b2b",
            background="#16ad8f", 
            bordercolor="#383838",
            lightcolor="#16ad8f",
            darkcolor="#16ad8f",
            thickness=10
        )
        self.progress = ttk.Progressbar(
            self.splash_window,
            orient="horizontal",
            length=width - 40,
            mode="determinate",
            style="Custom.Horizontal.TProgressbar"
        )
        self.progress.place(relx=0.5, rely=0.92, anchor="s")
        self.splash_window.update()


    # WIP
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
    
    # DONE
    def update_splash(self, progress_val: int, status_text=""):
        if self.splash_window and self.splash_label:
            self.status_label.config(text=status_text)
            if self.progress:
                self.progress["value"] = progress_val
            self.splash_window.update_idletasks()

    # DONE
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
        time.sleep(5)
        sys.exit(0)
        return False



# LATER LMAO
    
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
    
    def exit_avantzero(self, code: 0 | 1):
        print("Exiting AvantZero...")
        sys.exit(code)