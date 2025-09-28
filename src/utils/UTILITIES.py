import tkinter, os
from tkinter import messagebox

class UTILS:
    def return_to_main_menu(self):
        #TBA
        return True
    
    def show_error(code, message, link):
        root = tkinter.Tk()
        root.withdraw()
        if "github" in link:
            message += f"\n\nCheck out the Issues section on GitHub to see whether the issue has been reported."
        if "vercel" in link:
            message += f"\n\nMore info at: {link}"
        messagebox.showerror(f"ERROR: {code}", message)
        root.destroy()