from app.models.models import User, Task
from app.utils.helpers import get_next_id
from app.repositories import task_repository


def create_task(user: User, difficulty: int, description: str, notes: str) -> tuple[bool, str]:
    if not (1 <= difficulty <= 10):
        return None, "❌ Poziom trudności musi być między 1 a 10."
    if not description:
        return None, "❌ Wszystkie pola są wymagane"

    new_task = Task(
        id=get_next_id("T", "tasks"),
        user_id=user.id,
        difficulty=difficulty,
        description=description,
        additional_notes=notes
    )

    task_repository.save(new_task)
    return True, f"Zadanie {new_task.id} zostało poprawnie utworzone."


def find_active_tasks(user_id):
    return task_repository.find_by_id_and_status(user_id, "active")


def find_completed_tasks(user_id):
    return task_repository.find_by_id_and_status(user_id, "completed")


def complete_task(task: Task):
    return task_repository.make_task_complete(task)