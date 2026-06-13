import sqlite3
from pathlib import Path

from models import User


class UserStorage:
    def __init__(self, database_path="users.db"):
        self.database_path = Path(database_path)
        self._create_table()

    def load_users(self):
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT
                    full_name,
                    email,
                    date_of_birth,
                    password_hash,
                    security_question,
                    security_answer_hash
                FROM users
                ORDER BY full_name
                """
            ).fetchall()

        users = {}
        for row in rows:
            user = User(
                full_name=row["full_name"],
                email=row["email"],
                date_of_birth=row["date_of_birth"],
                password_hash=row["password_hash"],
                security_question=row["security_question"],
                security_answer_hash=row["security_answer_hash"],
            )
            users[user.email] = user

        return users

    def save_users(self, users):
        with self._connect() as connection:
            connection.execute("DELETE FROM users")

            for user in users.values():
                connection.execute(
                    """
                    INSERT INTO users (
                        full_name,
                        email,
                        date_of_birth,
                        password_hash,
                        security_question,
                        security_answer_hash
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        user.full_name,
                        user.email,
                        user.date_of_birth,
                        user.password_hash,
                        user.security_question,
                        user.security_answer_hash,
                    ),
                )

    def _connect(self):
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _create_table(self):
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    email TEXT PRIMARY KEY,
                    full_name TEXT NOT NULL,
                    date_of_birth TEXT NOT NULL,
                    password_hash TEXT NOT NULL,
                    security_question TEXT NOT NULL,
                    security_answer_hash TEXT NOT NULL
                )
                """
            )
