import requests
from fastapi import HTTPException
from typing import List, Optional

from repositories.stock_repository import StockRepository
from models.stock import Stock


ALPHAVANTAGE_API_KEY='KNXI6PPPULD9A84S'
ALPHAVANTAGE_URL='https://www.alphavantage.co/query'

class StockService:
    """
    Сервисный класс, где теперь используем Alpha Vantage
    для получения котировок 
    """
    def __init__(self):
        self.repo = StockRepository()

    def fetch_and_save_stock_price(self, symbol: str) -> Stock:
        """
        Получить цену из Alpha Vantage (GLOBAL QUOTE и БД)
        """
        params = {
            'function':'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': ALPHAVANTAGE_API_KEY
        }  

        try: 
            response = requests.get(ALPHAVANTAGE_URL, params = params, timeout = 10)
            if response.status_code != 200:
                raise HTTPException(status_code=400, detail=f"Can't fetch data for {symbol}")
            data = response.json()
            global_quote = data.get('Global Quote', {})

            if not global_quote or not global_quote.get("05. price"):
            #Не нашли цену в ответе
                raise HTTPException(status_code=404, detail=f"No data found for {symbol}")

            price_str = global_quote["05. price"] #строка типа 137.0000
            timestamp_str = global_quote.get("07. latest trading day","") #'YYYY-MM-DD' или ''

            #Конвертируем цену из строки в float
            try:
                price_float = float(price_str)
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid price format from Alpha Vantage")
        
            #Создаем модель Stock
            stock = Stock(
                symbol = symbol,
                price=price_float,
                timestamp = timestamp_str
            )

            #Сохраняем в БД
            self.repo.save(stock)
            return stock

        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Request error: {str(e)}")

    def get_prices_by_symbol(self, symbol: str) -> List[Stock]:
        """
        Вернуть записи из БД по символу.
        """
        return self.repo.get_by_symbol(symbol)

    def get_all_prices(self) -> List[Stock]:
        """
        Вернуть все записи из БД.
        """
        return self.repo.get_all()



    







