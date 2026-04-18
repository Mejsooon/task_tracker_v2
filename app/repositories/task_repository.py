from app.models.models import Task
from app.core.database import execute

def save(task: Task):
    execute("INSERT INTO tasks (id, user_id, difficulty, description, additional_notes, status) VALUES (%s, %s, %s, %s, %s, %s)",
            (task.id, task.user_id, task.difficulty, task.description, task.additional_notes, task.status))


def _row_to_task(row: dict):
    return Task(
        id=row["id"],
        user_id=row["user_id"],
        difficulty=row["difficulty"],
        description=row["description"],
        additional_notes=row["additional_notes"],
        status=row["status"],
    )

def find_by_id_and_status(user_id: int, status: str):
    rows = execute("SELECT * FROM tasks WHERE user_id = %s AND status = %s", (user_id, status), fetch="all")
    if rows:
        return [_row_to_task(row) for row in rows]
    return None

def make_task_complete(task: Task):
    execute("UPDATE tasks SET status = 'completed' WHERE id = %s", (task.id,))