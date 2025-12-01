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
    types.InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_main"),
)


@dp.message_handler(commands=["start", "help"])
async def cmd_start(message: types.Message):
    text = (
        "Привет! Я информационный бот.\n"
        "Выберите интересующий раздел ниже 👇"
    )
    await message.answer(text, reply_markup=MAIN_MENU)


@dp.callback_query_handler(lambda c: c.data in {"about", "pricing", "contacts"})
async def handle_main_sections(callback: types.CallbackQuery):
    if callback.data == "about":
        text = (
            "О компании\n\n"
            "Короткое описание компании/проекта. "
            "Здесь вы можете рассказать, чем занимаетесь и чем полезны клиенту."
        )
    elif callback.data == "pricing":
        text = (
            "Услуги и тарифы\n\n"
            "- Услуга 1 — от 3 000 ₽\n"
            "- Услуга 2 — от 5 000 ₽\n"
            "Точные цены зависят от задач и объёма работы."
        )
    else:  # contacts
        text = (
            "Контакты\n\n"
            "Telegram: @your_contact\n"
            "Email: example@example.com\n"
            "Сайт: https://example.com"
        )

    await callback.message.edit_text(text, reply_markup=MAIN_MENU)
    await callback.answer()


@dp.callback_query_handler(lambda c: c.data in {"faq", "back_main"})
async def handle_faq_entry(callback: types.CallbackQuery):
    if callback.data == "faq":
        text = "Частые вопросы. Выберите вопрос из списка:"
        await callback.message.edit_text(text, reply_markup=FAQ_MENU)
    else:
        text = "Выберите интересующий раздел ниже 👇"
        await callback.message.edit_text(text, reply_markup=MAIN_MENU)
    await callback.answer()


@dp.callback_query_handler(lambda c: c.data.startswith("faq_"))
async def handle_faq_questions(callback: types.CallbackQuery):
    if callback.data == "faq_how_order":
        text = (
            "Как сделать заказ?\n\n"
            "1) Опишите задачу.\n"
            "2) Согласуем детали и стоимость.\n"
            "3) Я выполню работу и отправлю результат с инструкцией."
        )
    elif callback.data == "faq_timing":
        text = (
            "Сроки выполнения\n\n"
            "Обычно от 1 до 3 рабочих дней в зависимости от сложности проекта."
        )
    else:  # faq_payment
        text = (
            "Способы оплаты\n\n"
            "По договорённости: карта, ЮMoney, другие варианты по запросу."
        )

    # показываем ответ и оставляем кнопки FAQ + назад
    await callback.message.edit_text(text, reply_markup=FAQ_MENU)
    await callback.answer()


async def on_startup(_):
    logging.info("FAQ bot started")


if __name__ == "__main__":
    if BOT_TOKEN == "PASTE_YOUR_FAQ_BOT_TOKEN_HERE":
        raise RuntimeError("Укажи токен FAQ-бота в BOT_TOKEN_FAQ или .env")
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
