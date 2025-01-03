import sqlite3
from typing import Optional

DB_NAME = "stocks.db"

class DBConnection:
    """
    Контекстный менеджер для управоения соединением с БД (SQLite)
    """
    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or DB_NAME
        self.conn = None
        
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

def init_db():
    """
    Создаёт таблицу для хранения данных по акциям, если её ещё нет.
    """
    with DBConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS stock_prices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT NOT NULL,
                price REAL NOT NULL,
                timestamp TEXT NOT NULL)
        """)
        conn.commit()
