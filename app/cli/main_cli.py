from app.models.models import User
from app.utils.helpers import clear_screen
from app.services import task_service
from app.utils.helpers import multiline_read

def user_panel(user: User):
    while True:
        clear_screen()
        active = len(task_service.get_active_tasks(user.id))
        done = len(task_service.get_completed_tasks(user.id))
        print(f"EXPOSITION TRACKER – {user.name}")
        print(f"Aktywne zadania: {active}  |  Ukończone: {done}")
        print("-" * 70)
        print("1. Utwórz nowe zadanie")
        print("2. Aktywne zadania")
        print("3. Historia zadań")
        print("4. Wyloguj się")
        print("-" * 70)

        choice = input("\nWybierz opcję: ").strip()
        if choice == "1":
            _create_task(user)
        elif choice == "2":
            _view_active(user)
        elif choice == "3":
            _view_history(user)
        elif choice == "4":
            break
        else:
            print("\n❌ Nieprawidłowa opcja.")
            input("\nNaciśnij Enter...")

def _create_task(user: User):
    clear_screen()
    print("NOWE ZADANIE EKSPOZYCYJNE\n" + "-" * 70)

    try:
        difficulity = int(input("Poziom Trudności (1-10): ").strip())
    except ValueError:
        difficulity = 0

    target = multiline_read("\nCel zadania (pusta linia kończy):")
    description = multiline_read("\n Opi zadania (pusta linia kończy):")

    print("Czy użyć domyślnych pytań refleksyjnych? (t/n): ", end="")
    if input().strip().lower() == "t":
        questions = task_service.DEFAULT_REFLECTION_QUESTIONS
    else:
        print("\nWpisz pytania refleksyjne (pusta linia kończy):")
        questions = []
        while True:
            q = input().strip()
            if not q:
                break
            questions.append(q)

    ok, msg = task_service.create_task(user.id, difficulity, target, description, questions)
    print(f"\n{'✅' if ok else '❌'} {msg}")
    input("\nNaciśnij Enter...")

def _view_active(user: User):
    clear_screen()
    print("AKTYWNE ZADANIA\n" + "-" * 70)

    tasks = task_service.get_active_tasks(user.id)

    if not tasks:
        print("Brak aktywnych zadań")
        input("\nNaciśnij Enter...")
        return

    for idx, t in enumerate(tasks, 1):
        preview = t.task_description[:60] + ("..." if len(t.task_description) > 60 else "")
        print(f"{idx}. [{t.id}] Trudność: {t.difficulty_level}/10")
        print(f"   {preview}")

    try:
        choice = int(input("Wybierz zadanie (0 - powrót): ")).strip()
        if choice == 0:
            return
        if not (1 <= choice <= len(tasks)):
            raise ValueError
    except ValueError:
        print("\n❌ Nieprawidłowy wybór.")
        input("\nNaciśnij Enter...")
        return

    user_choice = tasks[choice - 1] # Pierwsze zadanie ma indeks 0!




