from app.models.models import User
from app.repositories import user_repository
from app.utils.helpers import get_next_id
import bcrypt


def authenticate(username: str, password: str):
    user = user_repository.find_by_username(username)
    if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return user
    return None


def register_user(name: str, username: str, password: str) -> tuple[bool, str]:
    user = user_repository.find_by_username(username)
    if user:
       return False, "❌ Ta nazwa użytkownika jest już zajęta"
    if not name or not username or not password:
       return False, "❌ Wszystkie pola są wymagane."

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    # .decode("utf-8") odpowiada za zamianę na <str> a .encode("utf-8") odpowiada za zamianę na bajty (bytes)

    user = User(
        id=get_next_id("U", "users"),
        name=name,
        username=username,
        password=hashed_password,
    )

    user_repository.save(user)
    return True, f"Konto {name} zostało utworzone. Możesz się teraz zalogować"