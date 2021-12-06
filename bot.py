import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Filters,
)
import commands

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Speak. I have no time to waste."
    )


def help(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""
/start - Start PeterThePedant.
/help - List out commands.
<word> - Type any word to be defined""",
    )


start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
echo_handler = MessageHandler(Filters.text & (~Filters.command), commands.define)

dispatcher.add_handler(start_handler)
# dispatcher.add_handler(define_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(help_handler)


# Start the Bot
# updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=BOT_TOKEN)
# # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
# updater.bot.set_webhook(APP_NAME + BOT_TOKEN)

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.start_polling()
