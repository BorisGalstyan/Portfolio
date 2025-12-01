# Python-портфолио: боты, парсеры, автоматизация (RU)

Это портфолио-проект Python‑разработчика, который специализируется на прикладных задачах для малого и среднего бизнеса: Telegram‑боты, парсинг данных, автоматизация отчётов и интеграции через API.  
Все решения спроектированы как реалистичные кейсы под фриланс‑задачи (формат Kwork / биржи), часть из них уже обкатана на учебных и тестовых запросах.

Основной фокус — быстро превращать размытые запросы («нужен бот/отчёт/парсер») в понятные технические решения: с нормальной структурой кода, описанием, инструкциями и возможностью дальнейшего расширения.

---

## Стек и навыки

- Python 3.x: написание скриптов, модулей, работа с файлами и окружением.
- Telegram‑боты: aiogram 2.x, команды, меню, формы заявок, интеграции с базами и таблицами.
- Парсинг сайтов: requests, BeautifulSoup, lxml, экспорт данных в CSV/Excel.
- Таблицы и отчёты: pandas, openpyxl, автоматизация рутинных отчётов в Excel/Google Sheets.
- Веб‑API: FastAPI, приём форм с сайта, простые интеграции «сайт → таблица/бот».
- Организация проектов: структура репозиториев, README на русском и английском, пример конфигов (.env).

---

## Проекты

### 1. Telegram Lead Bot

Бот для приёма заявок через Telegram: собирает имя, контакт и комментарий, записывает их в таблицу (CSV) и, при необходимости, отправляет уведомление администратору.  
Это типовой кейс «бот для сбора лидов с лендинга или рекламной кампании».

**Стек:** Python, aiogram 2.x, csv, pathlib, dotenv.  
**Папка:** `telegram_lead_bot/`

---

### 2. Telegram FAQ Bot

Информационный бот‑визитка с меню и разделом FAQ: «О компании», «Услуги и тарифы», «FAQ», «Контакты».  
Подходит как быстрый пример того, как оформить FAQ‑бота для бизнеса без сложной логики.

**Стек:** Python, aiogram 2.x, Inline‑клавиатуры.  
**Папка:** `telegram_faq_bot/`

---

### 3. Price Parser (парсер цен)

Скрипт, который обходит несколько страниц каталога, собирает товары, цены и ссылки и сохраняет всё в CSV‑файл.  
Имитация заказа «нужен парсер товаров и цен с сайта конкурента / маркетплейса с выгрузкой в таблицу».

**Стек:** Python, requests, BeautifulSoup4, lxml, csv.  
**Папка:** `price_parser/`

---

### 4. Excel Report Automation

Автоматизация отчёта по продажам: из сырой выгрузки `raw_sales.csv` скрипт считает выручку по датам, товарам и каналам продаж и формирует отчёт `report.xlsx` с несколькими листами.  
Это типичный сценарий «убрать ручной Excel, оставить одну кнопку/скрипт».

**Стек:** Python, pandas, openpyxl.  
**Папка:** `excel_report_automation/`

---

### 5. Site → Sheets API

Небольшое FastAPI‑приложение, которое принимает заявки с формы сайта (POST `/lead`) и записывает их в CSV‑файл, играющий роль простой «таблицы заявок».  
Показывает умение делать минимальный backend для интеграций «сайт → таблица / CRM / бот».

**Стек:** Python, FastAPI, Uvicorn, csv, pathlib, datetime.  
**Папка:** `site_to_sheets_api/`

---

## Как использовать это портфолио

- Каждая папка — отдельный мини‑проект с собственным README и инструкциями по запуску.
- Проекты можно адаптировать под реальные задачи: сменить тексты, подключить настоящие Google Sheets, базы данных или внешние API.
- Репозиторий можно показать заказчику как набор готовых шаблонов для быстрых решений под его задачу.

---

# Python Portfolio: bots, scraping, automation (EN)

This repository is a Python developer portfolio focused on practical business tasks: Telegram bots, web scraping, report automation, and simple API integrations.  
All projects are designed as realistic freelance‑style cases (Kwork / freelance marketplaces), some of them already used as templates for test and educational tasks.

The main goal is to turn vague requests like “I need a bot/report/parser” into clear technical solutions: with clean structure, documentation and straightforward deployment.

---

## Tech stack & skills

- Python 3.x: scripting, modules, file handling, virtual environments.
- Telegram bots: aiogram 2.x, commands, menus, lead forms, integrations with files and simple databases.
- Web scraping: requests, BeautifulSoup, lxml, export to CSV/Excel.
- Spreadsheets & reports: pandas, openpyxl, automation of routine Excel/Google Sheets reports.
- Web APIs: FastAPI, handling HTML form submissions, simple “website → sheet/bot” integrations.
- Project organization: per‑project folders, bilingual READMEs (RU/EN), example `.env`‑based configuration.

---

## Projects

### 1. Telegram Lead Bot

Telegram bot that collects leads: name, contact and comment, stores them in a CSV table and optionally notifies an admin.  
Typical use case: collecting leads from a landing page or ad campaign directly in Telegram.

**Stack:** Python, aiogram 2.x, csv, pathlib, dotenv.  
**Folder:** `telegram_lead_bot/`

---

### 2. Telegram FAQ Bot

Simple informational “business card” bot with an inline menu and FAQ section: About, Services & pricing, FAQ, Contacts.  
Shows how to build a lightweight FAQ bot for a small business without complex logic.

**Stack:** Python, aiogram 2.x, inline keyboards.  
**Folder:** `telegram_faq_bot/`

---

### 3. Price Parser

Script that iterates over several catalog pages, extracts product titles, prices and URLs, and saves everything to a CSV file.  
This mimics a common freelance task: “parse products and prices from an online shop/marketplace into a spreadsheet”.

**Stack:** Python, requests, BeautifulSoup4, lxml, csv.  
**Folder:** `price_parser/`

---

### 4. Excel Report Automation

Report automation script: takes a raw `raw_sales.csv` export, calculates revenue by date, product and channel, and writes a ready‑to‑use `report.xlsx` with multiple sheets.  
A typical scenario where a manual Excel report is replaced by a single script.

**Stack:** Python, pandas, openpyxl.  
**Folder:** `excel_report_automation/`

---

### 5. Site → Sheets API

Small FastAPI service exposing a `/lead` endpoint which accepts website form submissions and appends them to `data/leads.csv`.  
Demonstrates a minimal backend for “website → sheet / CRM / bot” integrations.

**Stack:** Python, FastAPI, Uvicorn, csv, pathlib, datetime.  
**Folder:** `site_to_sheets_api/`

---

## How to work with this portfolio

- Each folder is a standalone mini‑project with its own README and usage instructions.
- You can adapt these projects to real‑world tasks: change copy, plug in real Google Sheets or databases, or extend them with extra logic.
- This repository can be shared with clients as a set of ready‑made templates to quickly implement their ideas with Python.
