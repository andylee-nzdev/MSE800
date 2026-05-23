from pathlib import Path
import sqlite3


class DatabaseManager:
    """Manages SQLite storage for aquarium inventory records."""

    def __init__(self):
        self.database_path = Path(__file__).with_name("aquarium_inventory.db")
        self.create_inventory_table()

    def connect(self):
        return sqlite3.connect(self.database_path)

    def create_inventory_table(self):
        with self.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS fish_inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    category TEXT NOT NULL,
                    quantity INTEGER NOT NULL CHECK (quantity >= 0)
                )
                """
            )

    def add_or_update_fish(self, name, category, quantity):
        with self.connect() as connection:
            connection.execute(
                """
                INSERT INTO fish_inventory (name, category, quantity)
                VALUES (?, ?, ?)
                ON CONFLICT(name) DO UPDATE SET
                    category = excluded.category,
                    quantity = fish_inventory.quantity + excluded.quantity
                """,
                (name, category, quantity),
            )

    def get_all_fish(self):
        with self.connect() as connection:
            return connection.execute(
                """
                SELECT name, category, quantity
                FROM fish_inventory
                ORDER BY name
                """
            ).fetchall()

    def has_fish(self):
        with self.connect() as connection:
            fish_count = connection.execute(
                "SELECT COUNT(*) FROM fish_inventory"
            ).fetchone()[0]

        return fish_count > 0
