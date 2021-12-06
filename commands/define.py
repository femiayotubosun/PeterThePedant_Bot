import telegram
from telegram import Update
from telegram.ext import CallbackContext
from dictionary_api import define_word
from services import dress_definition

import json


def define(update: Update, context: CallbackContext):
    word = context.args[0]
    if word:
        definition = define_word(word)
        text = dress_definition((definition[0]))

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            parse_mode=telegram.ParseMode.MARKDOWN,
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Please put your command in this format: /define Pedant(replace with word to define)",
        )
