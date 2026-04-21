import mysql.connector
from mysql.connector import MySQLConnection, errorcode
from config import DB_CONFIG
import logging


logger = logging.getLogger(__name__)


def get_connection() -> MySQLConnection:
    return mysql.connector.connect(**DB_CONFIG)


def execute(query: str, params: tuple = (), fetch: str = None) -> dict | list | int | None:
    conn = None
    cursor = None

    try:
        conn = get_connection()
        if conn or not conn.is_connected():
            raise mysql.connector.InterfaceError("Nie udało się uzyskać połączenia z bazą danych")

        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params)

        if fetch == "one":
            return cursor.fetchone()
        elif fetch == "all":
            return cursor.fetchall()

        conn.commit()
        return cursor.lastrowid

    except mysql.connector.IntegrityError as e:
        if conn:
            conn.rollback()
        if e.errno == errorcode.ER_DUP_ENTRY:
            logger.warning(f"Duplikat rekordu: {e}")
            raise  # przekaż wyżej — caller niech zdecyduje co zrobić
        logger.error(f"Naruszenie więzów bazy danych: {e}")
        raise

    except mysql.connector.ProgrammingError as e:
        if conn:
            conn.rollback()
        logger.error(f"Błąd SQL (sprawdź zapytanie): {e}")
        raise  # to zawsze powinno "eksplodować" — nie chcemy tego ukrywać

    except mysql.connector.OperationalError as e:
        # Serwer niedostępny, timeout, zbyt wiele połączeń
        if conn:
            conn.rollback()
        logger.error(f"Błąd operacyjny (serwer/sieć): {e}")
        raise

    except mysql.connector.InterfaceError as e:
        # Brak połączenia, None connection
        logger.error(f"Błąd interfejsu połączenia: {e}")
        raise

    except mysql.connector.Error as e:
        # Catch-all dla pozostałych błędów MySQL
        if conn:
            conn.rollback()
        logger.error(f"Nieoczekiwany błąd MySQL [{e.errno}]: {e}")
        raise

    finally:
        # Zawsze zamknij kursor i połączenie — nawet jeśli był wyjątek
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()