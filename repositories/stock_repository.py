from typing import List
from db import DBConnection
from models.stock import Stock

class StockRepository:
    """
    Репозиторий для CRUD-операций в таблице stock_prices.
    """
    def __init__(self):
        pass

    def save(self, stock: Stock) -> None:
        with DBConnection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO stock_prices (symbol, price, timestamp)
                VALUES (?, ?, ?)
            """, (stock.symbol, stock.price, stock.timestamp))
            conn.commit()
            print(f"Saved stock: {stock}")  # Отладка

    def get_by_symbol(self, symbol: str) -> List[Stock]:
        with DBConnection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT symbol, price, timestamp
                FROM stock_prices
                WHERE symbol = ?
                ORDER BY id DESC     
            """, (symbol,)) # в строку напишите sql запрос, который вытащит из базы записи по заданному symbol. Чтобы передать в запрос ваш symbol, после = напишите ?
            rows = cursor.fetchall()
        return [Stock(symbol=row[0], price=row[1], timestamp=row[2]) for row in rows]

    def get_all(self) -> List[Stock]:
        with DBConnection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                    SELECT symbol, price, timestamp
                    FROM stock_prices
                    ORDER by id DESC
            """) # напишите запрос, который вытащит все записи из таблицы stock_prices с сортировкой по id по убыванию
            rows = cursor.fetchall()
        return [Stock(symbol=row[0], price=row[1], timestamp=row[2]) for row in rows]
