# Название проекта
Программа по извлечению цен из СТокМаркета Alpha Vantage

## Установка

1. Клонируйте репозиторий:  
   `git clone https://github.com/Indira2022/my_fastapi_app.git`

2. Установите зависимости:  
   `pip install -r requirements.txt`

## Использование

Запуск приложения:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000

## Использование c Dockerfile 
Создание образа:
docker build -t название_образа .

Запуск контейнера, название контейнера: my_fastapi_app
docker run -d -p 8000:8000 --name my_fastapi_app my_fastapi_app

## После того как контейнер запущен, приложение будет доступно по адресу http://localhost:8000.

