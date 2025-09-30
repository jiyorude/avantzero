import tkinter, os
from tkinter import messagebox
from utils import TEXTS as AVZTX

class UTILS:
    def return_to_main_menu(self):
        #TBA
        return True
    
    def show_error(code, message, link):
        root = tkinter.Tk()
        root.withdraw()
        if "github" in link:
            message += AVZTX.error_github
        if "vercel" in link:
            message += f"{AVZTX.error_vercel} {link}"
        messagebox.showerror(f"ERROR: {code}", message)
        root.destroy()