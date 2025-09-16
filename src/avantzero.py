from utils.SYSTEM import SYSTEM

def main():
    try:
        AVANTZERO = SYSTEM()
        AVANTZERO.show_splash()
        AVANTZERO.init()
        AVANTZERO.check_folder_structure()
        AVANTZERO.update_splash(1)
        AVANTZERO.check_dependencies()
        AVANTZERO.update_splash(2)
        AVANTZERO.check_packages()
        AVANTZERO.update_splash(3)
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