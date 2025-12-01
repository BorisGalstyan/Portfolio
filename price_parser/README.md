# Парсер цен (RU)

Учебный проект на Python: парсер каталога товаров, который собирает название, цену и ссылку с нескольких страниц сайта и сохраняет всё в CSV-файл.  
Проект имитирует типовой заказ с фриланса: «нужен парсер товаров и цен с интернет-магазина с выгрузкой в таблицу».

---

## Возможности

- Загрузка нескольких страниц каталога по шаблону URL.
- Извлечение названия товара, цены и ссылки на карточку.
- Сохранение данных в `data/products.csv` (разделитель `;`).
- Лёгкая адаптация под другой сайт (достаточно поменять CSS-селекторы и базовый URL).

---

## Стек технологий

- Python 3.10+
- requests — загрузка HTML-страниц
- BeautifulSoup4 + lxml — разбор HTML
- csv, pathlib — работа с файлами и путями

---

## Структура проекта

```
price_parser/
├── data/
│   └── products.csv      # создаётся после первого запуска
├── src/
│   └── main.py           # исходный код парсера
├── requirements.txt
└── README.md
```

Формат файла `products.csv`:

```
title;price;url
The Grand Design;13.95;https://books.toscrape.com/catalogue/the-grand-design_405/index.html
```

---

## Как запустить

1. Перейдите в папку проекта:

```
cd price_parser
```

2. (Опционально) создайте и активируйте виртуальное окружение.
3. Установите зависимости:

```
pip install -r requirements.txt
```

4. Запустите парсер:

```
python -m src.main
```

После выполнения скрипта в `data/products.csv` появится список товаров с названиями, ценами и ссылками.

---

# Price parser (EN)

Educational Python project: a simple catalog scraper that collects product title, price and URL from several pages and saves everything to a CSV file.  
This project mimics a typical freelance task: “parse products and prices from an online shop and export them to a spreadsheet”.

---

## Features

- Fetch multiple catalog pages by URL template.
- Extract product title, price and product URL.
- Save data to `data/products.csv` (semicolon-separated).
- Easy to adapt to another website by changing CSS selectors and base URL.

---

## Tech stack

- Python 3.10+
- requests — HTTP client
- BeautifulSoup4 + lxml — HTML parsing
- csv, pathlib — file and path handling

---

## Project structure

```
price_parser/
├── data/
│   └── products.csv
├── src/
│   └── main.py
├── requirements.txt
└── README.md
```

## Usage

```
cd price_parser
pip install -r requirements.txt
python -m src.main
```

The script will create or update `data/products.csv` with collected products.
