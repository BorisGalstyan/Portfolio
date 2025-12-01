# Автоматизация отчёта в Excel (RU)

Учебный проект на Python: скрипт, который берёт сырую выгрузку продаж из CSV, считает базовые метрики и формирует готовый отчёт в Excel с несколькими листами.  
Имитация типового заказа: «автоматизируйте мой еженедельный/ежемесячный отчёт в Excel или Google Sheets».

---

## Что делает скрипт

- Загружает файл `data/raw_sales.csv` с данными по заказам.
- Считает выручку по каждой дате.
- Строит сводку по товарам: количество заказов, штук, выручка.
- Строит сводку по каналам продаж (website, marketplace, offline и т.п.).
- Сохраняет результат в `data/report.xlsx` с тремя листами.

---

## Стек технологий

- Python 3.10+
- pandas — обработка и агрегация данных
- openpyxl — запись отчёта в Excel

---

## Структура проекта

```
excel_report_automation/
├── data/
│   ├── raw_sales.csv      # исходные данные (выгрузка)
│   └── report.xlsx        # готовый отчёт (создаётся скриптом)
├── src/
│   └── main.py            # код автоматизации отчёта
├── requirements.txt
└── README.md
```

---

## Как запустить

1. Перейдите в папку проекта:

```
cd excel_report_automation
```

2. (Опционально) создайте и активируйте виртуальное окружение.
3. Установите зависимости:

```
pip install -r requirements.txt
```

4. Убедитесь, что в `data/raw_sales.csv` лежит ваша выгрузка с колонками:
   `date, order_id, product, category, quantity, price, channel`.
5. Запустите скрипт:

```
python -m src.main
```

В файле `data/report.xlsx` появится готовый отчёт с выручкой по датам, товарам и каналам продаж.

---

# Excel report automation (EN)

Educational Python project: a script that takes a raw sales CSV export, calculates basic metrics and generates a ready-to-use Excel report with several sheets.  
This mimics a common freelance task: “automate my weekly/monthly Excel or Google Sheets report”.

---

## What the script does

- Loads `data/raw_sales.csv` with order-level data.
- Calculates daily revenue.
- Builds a product summary: number of orders, quantity, revenue.
- Builds a channel summary (website, marketplace, offline, etc.).
- Saves the result to `data/report.xlsx` with three sheets.

---

## Tech stack

- Python 3.10+
- pandas — data processing and aggregation
- openpyxl — writing Excel reports

---

## Project structure

```
excel_report_automation/
├── data/
│   ├── raw_sales.csv
│   └── report.xlsx
├── src/
│   └── main.py
├── requirements.txt
└── README.md
```

## Usage

```
cd excel_report_automation
pip install -r requirements.txt
python -m src.main
```

The script will read `data/raw_sales.csv` and create `data/report.xlsx` with aggregated sales metrics.
