import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "data" / "products.csv"
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)


@dataclass
class Product:
    title: str
    price: float
    url: str


def fetch_page_html(page_number: int) -> str:
    url = BASE_URL.format(page_number)
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.text


def parse_products_from_html(html: str) -> List[Product]:
    soup = BeautifulSoup(html, "lxml")
    items = []

    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 a")
        price_tag = article.select_one(".price_color")

        if not title_tag or not price_tag:
            continue

        title = title_tag.get("title") or title_tag.text.strip()
        price_text = price_tag.text.strip().lstrip("£").replace(",", ".")
        try:
            price = float(price_text)
        except ValueError:
            continue

        relative_link = title_tag.get("href")
        url = "https://books.toscrape.com/catalogue/" + relative_link.lstrip("./")

        items.append(Product(title=title, price=price, url=url))

    return items


def save_products_to_csv(products: Iterable[Product]) -> None:
    is_new = not OUTPUT_FILE.exists()
    with OUTPUT_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        if is_new:
            writer.writerow(["title", "price", "url"])
        for p in products:
            writer.writerow([p.title, f"{p.price:.2f}", p.url])


def run_scraper(pages: int = 3) -> None:
    all_products: List[Product] = []
    for page in range(1, pages + 1):
        html = fetch_page_html(page)
        products = parse_products_from_html(html)
        all_products.extend(products)

    save_products_to_csv(all_products)
    print(f"Saved {len(all_products)} products to {OUTPUT_FILE}")


if __name__ == "__main__":
    run_scraper(pages=3)
