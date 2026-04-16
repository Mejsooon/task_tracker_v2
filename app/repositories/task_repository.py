from app.models.models import User, Task
from typing import List, Optional
from app.core.database import execute


def _row_to_task(row: dict) -> Optional[Task]:
    # Z tabeli (reflection_question) zwraca wszystkie pytania przypisane do tego zadania.
    # Pytania są w formie słownika -> (key: value) ("question": "Jak się masz?")
    questions = execute("SELECT question from reflecion_questions WHERE task_id = %s ORDER BY position",
                        (row["task_id"],), fetch="all")

    return Task(
        id=row["id"],
        user_id=row["user_id"],
        difficulty_level=row["difficulty_level"],
        task_target=row["task_target"],
        task_description=row["task_description"],
        reflection_questions=[q["question"] for q in questions], # Z pobranego słownika bierzemy tylko wartość (value)
        status=row["status"],
    )


def get_by_user_and_status(user: User, status: str) -> List[Task]:
    execute(f"SELECT * FROM tasks WHERE user_id= %s AND status= %s", (user.id, status), fetch="all")


def save(task: Task) -> Task:
    execute("INSERT INTO tasks VALUES (%s, %s, %s, %s, %s, %s)",
    (task.id, task.user_id, task.difficulty_level, task.task_target, task.task_description,))

    for pos, question in enumerate(task.reflection_questions, 1):
        execute("INSERT INTO reflection_questions (task_id, position, question) VALUES (%s, %s, %s)",
        (task.id, pos, question))
