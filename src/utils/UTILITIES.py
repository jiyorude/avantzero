import tkinter
from tkinter import messagebox

class UTILS:
    def return_to_main_menu(self):
        return True
    
    def show_error(self, code, message, link):
        root = tkinter.Tk()
        root.withdraw()
        if link:
            message += f"\n\nMore info at: {link}"
        messagebox.showerror(f"Error {code}", message, link)
        root.destroy()