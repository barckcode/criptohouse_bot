from telegram import ReplyKeyboardMarkup, keyboardbutton
from telegram.ext import CommandHandler


# Command
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        f"""
        Bienvenido {update.effective_chat.first_name}

        Soy CriptoHouse, sigue estos pasos para conocerte mejor:


        ID: {update.effective_chat.id}
        """
    )

    print(update.effective_chat)


# Action
start_handler = CommandHandler('start', start)
