from app.models.models import User
from app.repositories import user_repository
from app.utils.helpers import get_next_id


def authenticate(username: str, password: str):
    user = user_repository.find_by_username(username)
    if user and user.password == password:
        return user
    return None

def register_user(name: str, username: str, password: str) -> tuple[bool, str]:
    user = user_repository.find_by_username(username)
    if user:
       return False, print("❌ Ta nazwa użytkownika jest już zajęta")
    if not name or not username or not password:
       return False, print("❌ Wszystkie pola są wymagane.")

    user = User(
        id=get_next_id("U", "users"),
        name=name,
        username=username,
        password=password
    )

    user_repository.save(user)
    return True, f"Konto {name} zostało utworzone. Możesz się teraz zalogować"