from pydantic import BaseModel

class PriceRecord(BaseModel):
    symbol: str
    price: float
    timestamp: str
