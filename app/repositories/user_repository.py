from app.core.database import execute
from app.models.models import User


def row_to_user(row: dict):
    return User(
        id=row["id"],
        name=row["name"],
        username=row["username"],
        password=row["password"],
    )


def find_by_username(username):
    row = execute("SELECT * FROM users WHERE username = %s", (username,), fetch="one")

    if row:
        return row_to_user(row)
    return None


def save(user: User):
    execute("INSERT INTO users (name, username, password) VALUES (%s, %s, %s)", (user.name, user.username, user.password))