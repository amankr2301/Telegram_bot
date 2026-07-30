from app.logger import write_log
import json                                                        
from app.agent import ask_gemini
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from app.config import BOT_TOKEN




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am your Data Analyst Bot."
    )



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text

    result = ask_gemini(question)

    write_log(question, result)

    await update.message.reply_text(
    	json.dumps(result, ensure_ascii=False)
)

def run_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )

    print("Bot is running...")
    app.run_polling()
