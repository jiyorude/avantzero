from utils.SYSTEM import SYSTEM
import utils.TEXTS as AVZTX
import time

def main():
    try:
        AVANTZERO = SYSTEM()
        AVANTZERO.show_splash(
            initext=AVZTX.splashOne,
            font_name="Helvetica",
            size=48,
            width=500,
            height=500,
            version="v0.2.0",
        )
        time.sleep(2)
        AVANTZERO.update_splash(
            text=AVZTX.splashOne,
            font_name="Helvetica",
            font_size=48,
            progress_val=33,
            status_text=AVZTX.splash_title_one
        )
        time.sleep(2)
        AVANTZERO.check_folder_structure()
        AVANTZERO.update_splash(
            text=AVZTX.splashOne,
            font_name="Helvetica",
            font_size=48,
            progress_val=66,
            status_text=AVZTX.splash_title_two
        )
        time.sleep(2)
        AVANTZERO.check_dependencies()
        AVANTZERO.update_splash(
            text=AVZTX.splashOne,
            font_name="Helvetica",
            font_size=48,
            progress_val=100,
            status_text=AVZTX.splash_title_three
        )
        time.sleep(2)
        AVANTZERO.remove_splash()
        while True:
            choice = AVANTZERO.main_menu()
            match(choice):
                case 1:
                    AVANTZERO.boot_project_manager()
                case 2:
                    AVANTZERO.boot_data_generator()
                case 3:
                    AVANTZERO.boot_about()
                case 4:
                    AVANTZERO.boot_credits()
                case 5:
                    AVANTZERO.exit_avantzero()
    except KeyboardInterrupt:
        AVANTZERO.exit_avantzero()

if __name__ == "__main__":
    main()