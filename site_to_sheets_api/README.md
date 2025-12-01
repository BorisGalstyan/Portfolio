# Site → Sheets API (RU)

Учебный проект: небольшой HTTP‑сервис на FastAPI, который принимает заявки с формы сайта и записывает их в CSV‑файл (аналог Google Таблицы).  
Имитация типового заказа: «нужно, чтобы заявки с формы на сайте автоматически попадали в таблицу».

---

## Что делает сервис

- Принимает POST‑запрос на `/lead` с полями формы `name`, `contact`, `comment`.
- Добавляет строку в `data/leads.csv` с датой, именем, контактом и комментарием.
- Возвращает JSON‑ответ `{"status": "ok"}` для фронтенда.

---

## Стек технологий

- Python 3.10+
- FastAPI — HTTP‑API
- Uvicorn — ASGI‑сервер
- csv, pathlib, datetime — стандартная библиотека

---

## Структура проекта

site_to_sheets_api/
├── data/
│ └── leads.csv # создаётся автоматически после первого запроса
├── src/
│ └── main.py # код FastAPI-приложения
├── requirements.txt
└── README.md

text

---

## Как запустить локально

1. Перейдите в папку проекта:

cd site_to_sheets_api

text

2. (Опционально) создайте и активируйте виртуальное окружение.  
3. Установите зависимости:

pip install -r requirements.txt

text

4. Запустите сервер:

uvicorn src.main:app --reload

text

По умолчанию приложение будет доступно по адресу `http://127.0.0.1:8000`.

---

## Как отправить тестовую заявку

Через `curl`:

curl -X POST "http://127.0.0.1:8000/lead"
-F "name=Test User"
-F "contact=@testuser"
-F "comment=I need a landing page"

text

После запроса в файле `data/leads.csv` появится новая строка с заявкой.

---

# Site → Sheets API (EN)

Small FastAPI service that accepts lead submissions from a website form and writes them to a CSV file (as a simple Google Sheets analogue).  
This mimics a common freelance task: “send website form submissions to a spreadsheet”.

---

## What the service does

- Accepts a POST request to `/lead` with form fields `name`, `contact`, `comment`.
- Appends a new row to `data/leads.csv` with timestamp, name, contact and comment.
- Returns a JSON response `{"status": "ok"}` for the frontend.

---

## Tech stack

- Python 3.10+
- FastAPI — HTTP API
- Uvicorn — ASGI server
- csv, pathlib, datetime — standard library modules

---

## Project structure

site_to_sheets_api/
├── data/
│ └── leads.csv
├── src/
│ └── main.py
├── requirements.txt
└── README.md

text

---

## Local usage

cd site_to_sheets_api
pip install -r requirements.txt
uvicorn src.main:app --reload

text

Then send a POST request to:

curl -X POST "http://127.0.0.1:8000/lead"
-F "name=Test User"
-F "contact=@testuser"
-F "comment=I need a landing page"

text

The request will be saved into `data/leads.csv` as a new lead.
