import asyncio
import csv
import logging
import os
from datetime import datetime
from pathlib import Path

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

# Загружаем переменные окружения из .env (по желанию)
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "PASTE_YOUR_TOKEN_HERE")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))  # можно подставить свой ID руками

LEADS_FILE = Path(__file__).resolve().parent.parent / "data" / "leads.csv"
LEADS_FILE.parent.mkdir(parents=True, exist_ok=True)

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class LeadForm(StatesGroup):
    waiting_for_name = State()
    waiting_for_contact = State()
    waiting_for_comment = State()


def append_lead_to_csv(user_id: int, name: str, contact: str, comment: str) -> None:
    is_new_file = not LEADS_FILE.exists()
    with LEADS_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        if is_new_file:
            writer.writerow(["datetime", "user_id", "name", "contact", "comment"])
        writer.writerow([
            datetime.utcnow().isoformat(),
            user_id,
            name.strip(),
            contact.strip(),
            comment.strip()
        ])


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(text="Оставить заявку"))

    text = (
        "Привет! Я бот для приёма заявок.\n"
        "Нажми кнопку ниже, чтобы оставить свои контакты."
    )
    await message.answer(text, reply_markup=kb)


@dp.message_handler(lambda m: m.text == "Оставить заявку")
async def start_lead_form(message: types.Message, state: FSMContext):
    await message.answer("Как вас зовут?")
    await LeadForm.waiting_for_name.set()


@dp.message_handler(state=LeadForm.waiting_for_name, content_types=types.ContentTypes.TEXT)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Оставьте, пожалуйста, контакт (телефон, @username или email).")
    await LeadForm.waiting_for_contact.set()


@dp.message_handler(state=LeadForm.waiting_for_contact, content_types=types.ContentTypes.TEXT)
async def process_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await message.answer("Кратко опишите, что вам нужно.")
    await LeadForm.waiting_for_comment.set()


@dp.message_handler(state=LeadForm.waiting_for_comment, content_types=types.ContentTypes.TEXT)
async def process_comment(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    contact = data.get("contact")
    comment = message.text

    try:
        append_lead_to_csv(
            user_id=message.from_user.id,
            name=name,
            contact=contact,
            comment=comment,
        )
    except Exception as e:
        logging.exception("Ошибка при сохранении заявки: %s", e)
        await message.answer("Что-то пошло не так при сохранении заявки. Попробуйте ещё раз позже.")
        await state.finish()
        return

    await message.answer("Спасибо! Ваша заявка сохранена. Я свяжусь с вами как можно скорее. ✅")
    await state.finish()

    # Уведомляем админа, если указан
    if ADMIN_ID:
        lead_text = (
            f"Новая заявка:\n"
            f"Имя: {name}\n"
            f"Контакт: {contact}\n"
            f"Комментарий: {comment}\n"
            f"User ID: {message.from_user.id}"
        )
        try:
            await bot.send_message(chat_id=ADMIN_ID, text=lead_text)
        except Exception as e:
            logging.warning("Не удалось отправить уведомление админу: %s", e)


async def on_startup(_):
    logging.info("Bot started")


if __name__ == "__main__":
    if BOT_TOKEN == "PASTE_YOUR_TOKEN_HERE":
        raise RuntimeError("Укажи токен бота в переменной BOT_TOKEN или файле .env")
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
