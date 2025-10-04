from utils.DANLY import DANLY
from utils.DATAGEN import DATAGEN
from utils.DEPGEN import DEPGEN
from utils.PROJM import PROJM
from utils.NLEGEN import NLEGEN
from utils.UTILITIES import UTILS
from utils import TEXTS as AVZTX
import os, tkinter, time, sys, pkg_resources
from tkinter import font, ttk
from PIL import Image, ImageTk

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
            text=AVZTX.splashOne,
            fg="white",
            bg="#2b2b2b",
            font=splash_logofont
        )
        self.splash_label.place(relx=0.5, rely=0.37, anchor="center")
        splash_avztext = font.Font(family='Gantari ExtraLight', size=18)
        spaced_text = "  ".join(AVZTX.mame_one)
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
            text=AVZTX.mame_two,
            fg="white",
            bg="#2b2b2b",
            font=splash_loadingtext
        )
        self.status_label.place(relx=0.0367, rely=0.975, anchor="sw")
        self.version_label = tkinter.Label(
            self.splash_window,
            text=AVZTX.mame_three,
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

    def check_folder_structure(self):
        try:
            if not os.path.exists(os.path.join(os.path.expanduser("~"), "Documents", "AvantZero")):
                os.makedirs(os.path.join(os.path.expanduser("~"), "Documents", "AvantZero"))
                with open(os.path.join(os.path.expanduser("~"), "Documents", "AvantZero", '_AvantZero_Documentation.url'), 'w') as file:
                    file.write(f"[InternetShortcut]\nURL=https://avantzero-docs.vercel.app")
        except PermissionError:
            UTILS.show_error(AVZTX.err_four_a_title, AVZTX.err_four_a_msg, AVZTX.err_four_a_link)
            exit(1)
        except Exception as e:
            UTILS.show_error(AVZTX.err_four_b_title, f"{AVZTX.err_four_b_msg} {e}", AVZTX.err_four_b_link)
            exit(1)
        else:
            return True
        
    def check_dependencies(self):
        try:
            cores = ['DANLY.py', 'DATAGEN.py', 'DEPGEN.py', 'NLEGEN.py', 'PROJM.py', 'SYSTEM.py', 'UTILITIES.py', 'TEXTS.py']
            script_dir = os.path.dirname(os.path.abspath(__file__))
            missing_cores = []
            for core in cores:
                file_path = os.path.join(script_dir, core)
                if not os.path.isfile(file_path):
                    missing_cores.append(core)
            if missing_cores:
                raise FileNotFoundError
        except FileNotFoundError:
            UTILS.show_error({AVZTX.err_one_a_title}, f'{AVZTX.err_one_a} {", ".join(missing_cores)}', {AVZTX.err_one_a_link})
            exit(1)
        except Exception as e:
            UTILS.show_error(AVZTX.err_one_b_title, f"{AVZTX.err_one_b_msg} {e}", AVZTX.err_four_b_link)
            exit(1)
        else:
            return True
    
    def update_splash(self, progress_val: int, status_text=""):
        if self.splash_window and self.splash_label:
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
        missing = []
        script_dir = os.path.dirname(os.path.abspath(__file__)) 
        requirements_path = os.path.abspath(os.path.join(script_dir, "../../requirements.txt")) 
        with open(requirements_path, 'r', encoding='UTF-16') as req:            
            for line in req:
                package = line.strip()
                try:
                    pkg_resources.require(package)
                except pkg_resources.DistributionNotFound:
                    missing.append(package)
                except pkg_resources.VersionConflict as e:
                    missing.append(f"{package} (version conflict: {e})")
            try:
                if missing:
                    raise ImportError
            except ImportError:
                UTILS.show_error(AVZTX.err_two_title, f'{AVZTX.err_two_msg} {" ".join(missing)}', AVZTX.err_two_link)
                exit(1)
        return True
    
    def main_menu(self):
        self.main_window = tkinter.Tk()
        self.main_window.title(AVZTX.mame_one)
        self.main_window.geometry("500x720")
        self.main_window.configure(bg="#2b2b2b")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "..", "assets", "ico", "AvantZeroIco.ico")
        self.main_window.iconbitmap(icon_path)
        self.menu_frame = tkinter.Frame(self.main_window, bg="#2b2b2b")
        self.menu_frame.pack(fill="both", expand=True)
        main_title = "  ".join(AVZTX.mame_one)
        title_label = tkinter.Label(
            self.menu_frame,
            text=main_title,
            fg="white",
            bg="#2b2b2b",
            font=("Gantari ExtraLight", 25)
        )
        title_label.pack(pady=(80, 3)) 
        payoff_label = tkinter.Label(
            self.menu_frame,
            text=AVZTX.mame_nine,
            fg='white',
            bg='#2b2b2b',
            font=("Gantari ExtraLight", 12)
        )
        payoff_label.pack(pady=(0, 40))
        menu_buttons_frame = tkinter.Frame(self.menu_frame, bg="#2b2b2b")
        menu_buttons_frame.pack(pady=25)
        project_manager_button = tkinter.Button(
            menu_buttons_frame, 
            text=AVZTX.mame_four, 
            command=self.boot_project_manager,
            width=20, 
            height=2, 
            bg="#006D77", 
            fg="white", 
            font=("Gantari Regular", 14)
        )
        project_manager_button.pack(pady=15)
        data_generator_button = tkinter.Button(
            menu_buttons_frame, 
            text=AVZTX.mame_five, 
            command=self.boot_data_generator,
            width=20, 
            height=2, 
            bg="#006D77", 
            fg="white", 
            font=("Gantari Regular", 14)
        )
        data_generator_button.pack(pady=15)
        about_button = tkinter.Button(
            menu_buttons_frame, 
            text=AVZTX.mame_six, 
            command=self.boot_about,
            width=20, 
            height=2, 
            bg="#006D77", 
            fg="white", 
            font=("Gantari Regular", 14)
        )
        about_button.pack(pady=15)
        credits_button = tkinter.Button(
            menu_buttons_frame, 
            text=AVZTX.mame_seven, 
            command=self.boot_credits,
            width=20, 
            height=2, 
            bg="#006D77", 
            fg="white", 
            font=("Gantari Regular", 14)
        )
        credits_button.pack(pady=15)
        exit_button = tkinter.Button(
            menu_buttons_frame, 
            text=AVZTX.mame_eight, 
            command=lambda: self.exit_avantzero(0),
            width=20, 
            height=2, 
            bg="#990404", 
            fg="white", 
            font=("Gantari Regular", 14)
        )
        exit_button.pack(pady=15)
        self.main_window.protocol("WM_DELETE_WINDOW", lambda: self.exit_avantzero(0))
        self.main_window.mainloop()

    def boot_project_manager(self):
        self.menu_frame.pack_forget()

        if not hasattr(self, 'manager_frame'):
            self.manager_frame = tkinter.Frame(self.main_window, bg="#2b2b2b")
            self.manager_frame.pack(fill="both", expand=True)

            title_label = tkinter.Label(
                self.manager_frame,
                text=AVZTX.proj_title_one,
                fg="white",
                bg="#2b2b2b",
                font=("Gantari ExtraLight", 25)
            )
            title_label.pack(pady=50)

            content_label = tkinter.Label(
                self.manager_frame,
                text=AVZTX.proj_title_two,
                fg="white",
                bg="#2b2b2b",
                font=("Gantari Regular", 14)
            )
            content_label.pack(pady=20)

            back_button = tkinter.Button(
                self.manager_frame,
                text=AVZTX.back_button,
                command=lambda: (self.manager_frame.pack_forget(), self.menu_frame.pack(fill="both", expand=True)),
                width=10,
                height=1,
                bg="#006D77",
                fg="white"
                )
            back_button.pack(pady=30)
        else:
            self.manager_frame.pack(fill="both", expand=True)

    
    def boot_data_generator(self):
        self.menu_frame.pack_forget()

        if not hasattr(self, 'data_frame'):
            self.data_frame = tkinter.Frame(self.main_window, bg="#2b2b2b")
            self.data_frame.pack(fill="both", expand=True)

            title_label = tkinter.Label(
                self.data_frame,
                text=AVZTX.data_title_one,
                fg="white",
                bg="#2b2b2b",
                font=("Gantari ExtraLight", 25)
            )
            title_label.pack(pady=50)

            content_label = tkinter.Label(
                self.data_frame,
                text=AVZTX.data_title_two,
                fg="white",
                bg="#2b2b2b",
                font=("Gantari Regular", 14)
            )
            content_label.pack(pady=20)

            back_button = tkinter.Button(
                self.data_frame,
                text=AVZTX.back_button,
                command=lambda: (self.data_frame.pack_forget(), self.menu_frame.pack(fill="both", expand=True)),
                width=10,
                height=1,
                bg="#006D77",
                fg="white"
                )
            back_button.pack(pady=30)
        else:
            self.data_frame.pack(fill="both", expand=True)

    def boot_about(self):
        self.menu_frame.pack_forget()

        if not hasattr(self, 'about_frame'):
            self.about_frame = tkinter.Frame(self.main_window, bg="#2b2b2b")
            self.about_frame.pack(fill="both", expand=True)

            title_label = tkinter.Label(
                self.about_frame,
                text=AVZTX.about_title_one,
                fg="white",
                bg="#2b2b2b",
                font=("Gantari ExtraLight", 25)
            )
            title_label.pack(pady=50)

            content_label = tkinter.Label(
                self.about_frame,
                text=AVZTX.about_title_two,
                fg="white",
                bg="#2b2b2b",
                font=("Gantari Regular", 14)
            )
            content_label.pack(pady=20)

            back_button = tkinter.Button(
                self.about_frame,
                text=AVZTX.back_button,
                command=lambda: (self.about_frame.pack_forget(), self.menu_frame.pack(fill="both", expand=True)),
                width=10,
                height=1,
                bg="#006D77",
                fg="white"
                )
            back_button.pack(pady=30)
        else:
            self.about_frame.pack(fill="both", expand=True)
    
    def boot_credits(self):
        self.menu_frame.pack_forget()

        if not hasattr(self, 'credits_frame'):
            self.credits_frame = tkinter.Frame(self.main_window, bg="#2b2b2b")
            self.credits_frame.pack(fill="both", expand=True)

            title_label = tkinter.Label(
                self.credits_frame,
                text=AVZTX.credits_title_one,
                fg="white",
                bg="#2b2b2b",
                font=("Gantari ExtraLight", 25)
            )
            title_label.pack(pady=50)

            content_label = tkinter.Label(
                self.credits_frame,
                text=AVZTX.credits_title_two,
                fg="white",
                bg="#2b2b2b",
                font=("Gantari Regular", 14)
            )
            content_label.pack(pady=20)

            back_button = tkinter.Button(
                self.credits_frame,
                text=AVZTX.back_button,
                command=lambda: (self.credits_frame.pack_forget(), self.menu_frame.pack(fill="both", expand=True)),
                width=10,
                height=1,
                bg="#006D77",
                fg="white"
                )
            back_button.pack(pady=30)
        else:
            self.credits_frame.pack(fill="both", expand=True)

    def exit_avantzero(self, code: 0 | 1):
        sys.exit(code)