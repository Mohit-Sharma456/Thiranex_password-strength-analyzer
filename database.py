import hashlib
import sqlite3
from pathlib import Path


DATABASE_FILE = Path(__file__).parent / "password_history.db"


def get_connection():
    return sqlite3.connect(DATABASE_FILE)


def initialize_database():
    """
    Create password history table if it doesn't exist.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS password_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password_hash TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()


def hash_password(password):
    """
    Convert password into SHA-256 hash.
    """

    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


def is_password_reused(password):
    """
    Check whether password hash already exists.
    """

    password_hash = hash_password(password)

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id
        FROM password_history
        WHERE password_hash = ?
        """,
        (password_hash,)
    )

    result = cursor.fetchone()

    connection.close()

    return result is not None


def save_password(password):
    """
    Store password hash in database.
    """

    password_hash = hash_password(password)

    connection = get_connection()

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO password_history (password_hash)
            VALUES (?)
            """,
            (password_hash,)
        )

        connection.commit()

        success = True

    except sqlite3.IntegrityError:
        success = False

    finally:
        connection.close()

    return success


def get_password_count():
    """
    Return total number of stored password hashes.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM password_history
        """
    )

    count = cursor.fetchone()[0]

    connection.close()

    return count


def clear_password_history():
    """
    Delete all stored password hashes.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM password_history"
    )

    connection.commit()
    connection.close()