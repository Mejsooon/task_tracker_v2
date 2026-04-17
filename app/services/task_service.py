from app.repositories import task_repository
from app.models.models import User, Task, Reflection
from app.utils.helpers import get_next_id
from typing import List


DEFAULT_REFLECTION_QUESTIONS = [
    "Co się wydarzyło podczas wykonywania zadania?",
    "Jakie myśli pojawiły się w trakcie?",
    "Co było inne niż zakładałeś/aś?",
    "Jakie emocje towarzyszyły tej sytuacji?",
]


def get_active_tasks(user: User) -> List[Task]:
    return task_repository.get_by_user_and_status(user.id, "active")


def get_completed_tasks(user: User) -> List[Task]:
    return task_repository.get_by_user_and_status(user.id, "completed")


def create_task(user_id: str, difficulty: str, task_target: str, task_description: str, reflection_questions: list[str]) -> tuple[bool, str]:
    if not (1 <= difficulty <= 10):
        return False, "Poziom trudności musi być od 1 do 10"
    if not task_target or not task_description or not reflection_questions:
        return False, "Wszystkie pola są wymagane"

    task = Task(
        id = get_next_id("T", "tasks"),
        user_id = user_id,
        difficulty_level = difficulty,
        task_target = task_target,
        task_description = task_description,
        reflection_questions = reflection_questions,
    )


    task_repository.save(task)
    return True, f"Zadanie {task.id} zostało utworzone."


def complete_task(task: Task, answers: dict[str, str], notes: str, user_id: str) -> None:
    reflection = Reflection(
        task_id=task.id,
        user_id=user_id,
        answers=answers,
        optional_notes=notes,
    )
