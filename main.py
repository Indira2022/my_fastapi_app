
import uvicorn
from fastapi import FastAPI

from db import init_db
from routes.stock import router as stock_router

# Инициализация БД при старте
init_db()

app = FastAPI(title="Stocks Data Example with Routers")

# Подключаем роутер
app.include_router(stock_router)

@app.get("/")
def root():
    return {"message": "Hello, Hi, Salam"}

def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)