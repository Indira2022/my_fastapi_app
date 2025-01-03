from fastapi import APIRouter, HTTPException
from typing import List

from services.stock import StockService
from schemas import PriceRecord

# Инициализируем экземпляр класса StockService
stock_service = StockService()

# Создаём роутер. Можно указать prefix, теги и т.д.
router = APIRouter(
    prefix="/stocks",
    tags=["stocks"]
)

@router.get("/fetch/{symbol}")
def fetch_stock_price(symbol: str):
    """
    Эндпоинт, который ходит за ценой акции к апи
    и сохраняет полученные данные в БД.
    """
    stock = stock_service.fetch_and_save_stock_price(symbol)# вызовите функцию для запроса данных из апи и сохранения в базу по названию (symbol) из класса StockService
    return {
        "status": "OK",
        "symbol": stock.symbol,
        "price": stock.price,
        "timestamp": stock.timestamp
    }

@router.get("/{symbol}", response_model=List[PriceRecord])
def get_stock_prices(symbol: str):
    """
    Возвращает все записи по указанному символу из БД.
    """
    stocks = stock_service.get_prices_by_symbol(symbol) # вызовите функцию для запроса данных из базы по названию (symbol) из класса StockService
    return [
        PriceRecord(symbol=s.symbol, price=s.price, timestamp=s.timestamp)
        for s in stocks
    ]

@router.get("/show/all", response_model=List[PriceRecord])
def get_all_prices():
    """
    Возвращает все записи из таблицы stock_prices.
    """
    stocks = stock_service.get_all_prices() # вызовите функцию для запроса всех данных из базы из класса StockService
    return [
        PriceRecord(symbol=s.symbol, price=s.price, timestamp=s.timestamp)
        for s in stocks
    ]
