import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes


BOT_TOKEN = os.environ["BOT_TOKEN"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "📢 KANALA KATIL",
                url="https://t.me/otokodx"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Hoş geldin!\n\n"
        "Güncel kodları görmek için kanalımıza katılabilirsin. 👇",
        reply_markup=reply_markup
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot çalışıyor...")
    app.run_polling()


if __name__ == "__main__":
    main()
