class Stock:
    """
    Пример простой доменной модели
    """

    def __init__(self, symbol: str, price: float, timestamp:str):
        self.symbol = symbol
        self.price = price
        self.timestamp = timestamp

    def __repr__(self):
        return f"Stock(symbol={self.symbol}, price = {self.price}, timestamp = {self.timestamp})"