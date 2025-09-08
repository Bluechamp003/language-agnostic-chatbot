from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TELEGRAM_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Received /start command!")
    await update.message.reply_text("Hello! This is a test bot.")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started, waiting for messages...")
    app.run_polling()

if __name__ == "__main__":
    main()
