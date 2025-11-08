import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен бота (замени на свой)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8211063612:AAGwFR5W205fjsIP9D7TSZ-X6EZ8tf3669g")

# URL твоего WebApp — страница /tg
WEBAPP_URL = "https://cupid-comma-08748912.figma.site/tg"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                text="☕ Открыть меню",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Добро пожаловать в кофейню! ☕\n\nНажмите кнопку ниже, чтобы открыть меню:",
        reply_markup=reply_markup
    )

# Основная функция запуска
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
