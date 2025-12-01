from pathlib import Path
import csv
from datetime import datetime

from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

app = FastAPI(title="Site to Sheets API")

BASE_DIR = Path(__file__).resolve().parent.parent
LEADS_FILE = BASE_DIR / "data" / "leads.csv"
LEADS_FILE.parent.mkdir(parents=True, exist_ok=True)


def append_lead(name: str, contact: str, comment: str) -> None:
    is_new = not LEADS_FILE.exists()
    with LEADS_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        if is_new:
            writer.writerow(["datetime", "name", "contact", "comment"])
        writer.writerow([datetime.utcnow().isoformat(), name, contact, comment])


@app.post("/lead")
async def receive_lead(
    name: str = Form(...),
    contact: str = Form(...),
    comment: str = Form(""),
):
    append_lead(name=name.strip(), contact=contact.strip(), comment=comment.strip())
    return JSONResponse({"status": "ok"})
