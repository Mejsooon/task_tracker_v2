from app.cli.auth_cli import login_screen, register_screen
from app.cli.main_cli import user_panel
from app.utils.helpers import clear_screen

def main():
    while True:
        clear_screen()
        print("EXPOSITION TRACKER – ZADANIA EKSPOZYCYJNE")
        print("=" * 70)
        print("MENU GŁÓWNE\n" + "-" * 70)
        print("1. Zaloguj się")
        print("2. Zarejestruj się")
        print("3. Wyjdź")
        print("-" * 70)
        print("\nKonto demo: demo / demo123\n")

        choice = input("Wybierz opcję: ").strip()

        if choice == "1":
            user = login_screen()
            if user:
                user_panel(user)
        elif choice == "2":
            register_screen()
        elif choice == "3":
            clear_screen()
            print("Do zobaczenia!")
            break
        else:
            print("\n❌ Nieprawidłowa opcja.")
            input("\nNaciśnij Enter...")


if __name__ == "__main__":
    main()