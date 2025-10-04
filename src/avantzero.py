from utils.SYSTEM import SYSTEM
from utils import TEXTS as AVZTX
import time

def main():
    try:
        AVANTZERO = SYSTEM()
        AVANTZERO.show_splash()
        time.sleep(0.3)
        AVANTZERO.update_splash(
            progress_val=33,
            status_text=AVZTX.splash_title_one
        )
        AVANTZERO.check_folder_structure()
        time.sleep(0.3)
        AVANTZERO.update_splash(
            progress_val=66,
            status_text=AVZTX.splash_title_two
        )
        AVANTZERO.check_dependencies()
        time.sleep(0.3)
        AVANTZERO.update_splash(
            progress_val=100,
            status_text=AVZTX.splash_title_three
        )
        AVANTZERO.check_packages()
        AVANTZERO.remove_splash()
    except Exception:
        AVANTZERO.exit_avantzero(0)
    else:
        AVANTZERO.main_menu()

if __name__ == "__main__":
    main()