from pathlib import Path
from typing import Tuple

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_FILE = BASE_DIR / "data" / "raw_sales.csv"
REPORT_FILE = BASE_DIR / "data" / "report.xlsx"


def load_data() -> pd.DataFrame:
    df = pd.read_csv(RAW_FILE)
    df["date"] = pd.to_datetime(df["date"])
    df["revenue"] = df["quantity"] * df["price"]
    return df


def build_reports(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    by_date = (
        df.groupby("date", as_index=False)["revenue"]
        .sum()
        .sort_values("date")
    )

    by_product = (
        df.groupby("product", as_index=False)
        .agg(
            orders=("order_id", "nunique"),
            quantity=("quantity", "sum"),
            revenue=("revenue", "sum"),
        )
        .sort_values("revenue", ascending=False)
    )

    by_channel = (
        df.groupby("channel", as_index=False)
        .agg(
            orders=("order_id", "nunique"),
            revenue=("revenue", "sum"),
        )
        .sort_values("revenue", ascending=False)
    )

    return by_date, by_product, by_channel


def save_to_excel(
    by_date: pd.DataFrame,
    by_product: pd.DataFrame,
    by_channel: pd.DataFrame,
) -> None:
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(REPORT_FILE, engine="openpyxl") as writer:
        by_date.to_excel(writer, sheet_name="Revenue by date", index=False)
        by_product.to_excel(writer, sheet_name="By product", index=False)
        by_channel.to_excel(writer, sheet_name="By channel", index=False)


def main() -> None:
    df = load_data()
    by_date, by_product, by_channel = build_reports(df)
    save_to_excel(by_date, by_product, by_channel)
    print(f"Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
