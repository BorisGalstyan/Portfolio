# Telegram Lead Bot (RU)

Простой Telegram‑бот для приёма заявок: собирает имя, контакт и короткий комментарий пользователя и сохраняет всё в CSV‑файл.  
Учебный проект для портфолио под типовые задачи с фриланса: сбор заявок через Telegram.

---

## Возможности

- Команда `/start` с приветствием и кнопкой «Оставить заявку».
- Трёхшаговая форма заявки: **имя → контакт → комментарий**.
- Сохранение каждой заявки в файл `data/leads.csv` (разделитель — `;`).
- Опциональное уведомление администратора с деталями заявки в личные сообщения.
- Минимум зависимостей, можно запускать локально или на любом VPS.

---

## Стек технологий

- Python 3.10+
- aiogram 2.x — фреймворк для Telegram‑ботов
- Стандартная библиотека: `csv`, `datetime`, `logging`, `os`, `pathlib`
- `python-dotenv` для загрузки переменных окружения из `.env`

---

## Структура проекта

```
telegram_lead_bot/
├── data/
│   └── leads.csv          # создаётся автоматически после первой успешной заявки
├── src/
│   └── main.py            # исходный код бота
├── .env.example           # пример файла окружения (опционально)
├── requirements.txt
└── README.md
```

Формат файла `leads.csv`:

```
datetime;user_id;name;contact;comment
2025-01-01T12:34:56.789012;123456789;John Doe;@johndoe;Need a Telegram bot for my shop
```

---

## Как запустить

1. Клонируйте репозиторий и перейдите в папку проекта.
2. (По желанию) создайте виртуальное окружение и активируйте его.
3. Установите зависимости командой `pip install -r requirements.txt`.
4. Укажите токен бота и `ADMIN_ID` через файл `.env` или прямо в `src/main.py`.
5. Запустите бота:

```
python -m src.main
```

После запуска откройте бота в Telegram, отправьте `/start`, нажмите «Оставить заявку» и ответьте на вопросы.  
Заявка будет записана в `data/leads.csv`, а администратор (если задан `ADMIN_ID`) получит уведомление.

---

## Как это работает

1. Пользователь отправляет `/start` и видит клавиатуру с кнопкой **«Оставить заявку»**.
2. Бот запускает конечный автомат (FSM) с тремя состояниями:
   - `waiting_for_name`
   - `waiting_for_contact`
   - `waiting_for_comment`
3. После ввода всех полей бот:
   - добавляет строку в `data/leads.csv`;
   - благодарит пользователя и завершает диалог;
   - опционально отправляет администратору текст заявки.

---

## Как адаптировать под реальные задачи

- Измените поля формы (например, добавьте выбор услуги или бюджета).
- Замените CSV‑хранение на SQLite или Google Sheets.
- Подключите отправку заявок в CRM или на e‑mail.

---

# Telegram Lead Bot (EN)

Simple Telegram bot for collecting leads (name, contact, short comment) and saving them to a CSV file.  
Made as a portfolio project for typical freelance tasks: collecting requests from users via Telegram.

---

## Features

- `/start` command with a short intro and a button to leave a request.
- Three–step lead form: **name → contact → comment**.
- Saving each lead to `data/leads.csv` (semicolon-separated).
- Optional notification with lead details to the admin in a private chat.
- Minimal dependencies, easy to deploy on any VPS or local machine.

---

## Tech stack

- Python 3.10+
- aiogram 2.x as Telegram Bot framework
- `csv`, `datetime`, `logging`, `os`, `pathlib` from the standard library
- `python-dotenv` for loading environment variables from `.env`

---

## Project structure

```
telegram_lead_bot/
├── data/
│   └── leads.csv          # created automatically after the first successful lead
├── src/
│   └── main.py            # bot source code
├── .env.example           # example env file (optional)
├── requirements.txt
└── README.md
```

**Leads file format (`leads.csv`):**

```
datetime;user_id;name;contact;comment
2025-01-01T12:34:56.789012;123456789;John Doe;@johndoe;Need a Telegram bot for my shop
```

---

## Getting started

### 1. Clone the repo and go to the project folder

```
git clone https://github.com/<your-username>/python-kwork-portfolio.git
cd python-kwork-portfolio/telegram_lead_bot
```

### 2. Create and activate virtual environment (optional but recommended)

```
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
# .venv\Scripts\activate.bat   # Windows (cmd)
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure bot token and admin ID

You can set configuration via environment variables (recommended) or by editing constants in `src/main.py`.

**Option A — `.env` file**

Create `.env` in the project root:

```
BOT_TOKEN=your_telegram_bot_token_here
ADMIN_ID=123456789
```

**Option B — constants in code (for quick local testing)**

In `src/main.py` replace the default values with your actual token and admin id.  
Do not commit real secrets to public repositories.

---

### 5. Run the bot

```
python -m src.main
```

If everything is configured correctly, you will see a log line like:

```
INFO:root:Bot started
```

Open your bot in Telegram, send `/start`, press **«Оставить заявку»** and follow the prompts.  
After the final message, a new row will appear in `data/leads.csv`, and the admin (if configured) will receive a notification.

---

## How it works

1. User sends `/start` and gets a welcome message with a keyboard button **«Оставить заявку»**.
2. Bot starts a finite state machine (FSM) with three states:
   - `waiting_for_name`
   - `waiting_for_contact`
   - `waiting_for_comment`
3. After collecting all three fields, bot:
   - appends a new row to `data/leads.csv`;
   - thanks the user and finishes the conversation;
   - optionally sends a formatted lead summary to the admin.

---

## Notes

- This is an educational project for a portfolio. You can easily adapt the form fields, storage (e.g. SQLite or Google Sheets) and notification logic to match a real client task.
- Do **not** commit real bot tokens or personal admin IDs to public repositories. Use `.env` and `.gitignore` for secrets.
