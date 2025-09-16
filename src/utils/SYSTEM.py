from utils.DANLY import DANLY
from utils.DATAGEN import DATAGEN
from utils.DEPGEN import DEPGEN
from utils.PROJM import PROJM
from utils.NLEGEN import NLEGEN
from utils.UTILITIES import UTILS
import utils.TEXTS as AVZTX
import os

class SYSTEM:
    COREDANLY, COREDATAGEN, COREDEPGEN, COREPROJM, CORENLEGEN, COREUTILS = DANLY, DATAGEN, DEPGEN, PROJM, NLEGEN, UTILS 
    
    def init(self):
        return True
    
    def show_splash(self):
        return True
    
    def check_folder_structure(self):
        try:
            if not os.path.exists(os.path.join(os.path.expanduser("~"), "Documents", "AvantZero")):
                os.makedirs(os.path.join(os.path.expanduser("~"), "Documents", "AvantZero"))
                with open(os.path.join(os.path.expanduser("~"), "Documents", "AvantZero", '_AvantZero_Documentation.url'), 'w') as file:
                    file.write(f"[InternetShortcut]\nURL=https://avantzero-docs.vercel.app")
            else:
                return True
        except Exception:
            return '004'

    def check_dependencies(self):
        return True
    
    def update_splash(self):
        return True
    
    def remove_splash(self):
        return True
    
    def check_packages(self):
        return True
    
    def main_menu(self):
        return True
    
    def boot_project_manager(self):
        return True
    
    def boot_data_generator(self):
        return True
    
    def boot_about(self):
        return True
    
    def boot_credits(self):
        return True
    
    def exit_avantzero(self):
        return True
    
    