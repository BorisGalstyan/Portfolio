import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN_FAQ", "PASTE_YOUR_FAQ_BOT_TOKEN_HERE")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


MAIN_MENU = types.InlineKeyboardMarkup(row_width=2)
MAIN_MENU.add(
    types.InlineKeyboardButton(text="О компании", callback_data="about"),
    types.InlineKeyboardButton(text="Услуги и тарифы", callback_data="pricing"),
    types.InlineKeyboardButton(text="FAQ", callback_data="faq"),
    types.InlineKeyboardButton(text="Контакты", callback_data="contacts"),
)

FAQ_MENU = types.InlineKeyboardMarkup(row_width=1)
FAQ_MENU.add(
    types.InlineKeyboardButton(text="Как сделать заказ?", callback_data="faq_how_order"),
    types.InlineKeyboardButton(text="Сроки выполнения", callback_data="faq_timing"),
    types.InlineKeyboardButton(text="Способы оплаты", callback_data="faq_payment"),
    types.InlineKeyboardButton(text="⬅️ Наз
