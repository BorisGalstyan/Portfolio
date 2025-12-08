from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel, EmailStr
from typing import List, Dict

app = FastAPI(title="Мультинейросеть MVP")

# Отдаём фронтенд
app.mount("/static", StaticFiles(directory="static"), name="static")


class UserCreate(BaseModel):
    email: EmailStr
    promokod: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    active_modules: List[str]


class ChatRequest(BaseModel):
    module_id: str
    message: str


# Модули и шаблонные промпты (как в ТЗ, укорочено)
MODULES: Dict[str, Dict] = {
    "jurist": {
        "name": "Юридический навигатор",
        "prompts": [
            "Составь договор аренды квартиры",
            "Проверь договор на риски",
            "Объясни мои права в бытовой ситуации",
            "Помоги написать претензию",
            "Расскажи об изменениях в законе"
        ]
    },
    "auto": {
        "name": "Автопомощник",
        "prompts": [
            "Машина издает странный звук, что это может быть?",
            "Составь график ТО для моего авто",
            "Подбери аналоги запчасти",
            "Рассчитай стоимость владения машиной",
            "Какие документы нужны для продажи авто?"
        ]
    },
    "pc": {
        "name": "ПК‑помощник",
        "prompts": [
            "Компьютер медленно работает, помоги найти причину",
            "Как настроить Wi‑Fi роутер?",
            "Подбери ноутбук для работы и учёбы",
            "Помоги удалить вирус",
            "Настрой автоматическое резервное копирование"
        ]
    },
    "home": {
        "name": "Дом‑мастер",
        "prompts": [
            "Как починить протекающий кран?",
            "Составь график сезонных работ по дому",
            "Как выбрать стиральную машину?",
            "Экстренные меры при засоре",
            "Организуй систему хранения в кладовке"
        ]
    },
    "med": {
        "name": "Медицинский переводчик симптомов",
        "prompts": [
            "Помоги описать симптомы для терапевта",
            "Объясни, что значит диагноз",
            "Составь список вопросов к врачу",
            "Напомни правила приёма лекарства",
            "Расшифруй назначения из карты"
        ]
    }
}


@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("static/index.html")


@app.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    """
    Демо‑регистрация: всегда успешна.
    Промокод ни на что не влияет, просто лог для кейса.
    """
    active = list(MODULES.keys())
    # В реальном проекте тут была бы проверка промокода и БД.
    return UserOut(id=1, email=user.email, active_modules=active)


@app.get("/modules")
async def get_modules():
    """Список модулей с шаблонными промптами."""
    return [
        {"id": mid, "name": data["name"], "prompts": data["prompts"]}
        for mid, data in MODULES.items()
    ]


@app.post("/chat/{module_id}")
async def chat(module_id: str, req: ChatRequest):
    """Простой mock‑ответ нейросети для демо."""
    if module_id not in MODULES:
        raise HTTPException(status_code=404, detail="Модуль не найден")

    base = MODULES[module_id]["name"]
    text = (
        f"Это ответ от ассистента «{base}» на ваш запрос. "
        f"В реальном сервисе здесь будет ответ от YaGPT/GigaChat. "
        f"Ваш вопрос: «{req.message}»."
    )
    return {"response": text}
