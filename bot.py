import os
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("8211063612:AAGwFR5W205fjsIP9D7TSZ-X6EZ8tf3669g")
WEBAPP_URL = "https://cupid-comma-08748912.figma.site/tg"
BACKEND_URL = os.getenv("https://cupid-comma-08748912.figma.site/api/telegram-auth")  # это ты добавишь в Render

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # 1. отправляем юзера на твой бэкенд
    if BACKEND_URL:
        try:
            requests.post(BACKEND_URL, json={
                "telegram_id": user.id,
                "username": user.username,
                "first_name": user.first_name,
            }, timeout=3)
        except Exception:
            pass  # чтобы бот не падал

    # 2. шлём кнопку на открытие web app
    keyboard = [[
        InlineKeyboardButton(
            text="☕ Открыть меню",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]
    await update.message.reply_text(
        "Открой меню:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
