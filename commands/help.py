from telegram.update import Update
from telegram.ext import CommandHandler
from telegram.ext.callbackcontext import CallbackContext


def help(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text='🤖 CriptoHouse:\n\nHelp text for user ...',
        )


help_command = CommandHandler('help', help)
