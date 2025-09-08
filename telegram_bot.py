import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import rag_chat  # this imports your chatbot code

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Replace with your real BotFather token
TELEGRAM_TOKEN = "8430754600:AAF5fdiIKnxXAjOITRbT6Yl6m4elGqCMFrc"

# Function for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I’m your campus chatbot. Ask me anything.")

# Function for handling user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    # Pass user input to your chatbot
    response = rag_chat.ask_bot(user_input)  # <-- you'll need a function like this in rag_chat.py

    await update.message.reply_text(response)

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()


def ask_bot(user_input: str) -> str:
    # TODO: replace this with your actual chatbot logic
    response = f"You said: {user_input}"
    return response

