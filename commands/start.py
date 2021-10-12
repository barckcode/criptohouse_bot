from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.update import Update
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext.callbackcontext import CallbackContext


# Buttons
keyboard = [
    [
        InlineKeyboardButton("Dólares (USD)", callback_data='usd'),
        InlineKeyboardButton("Euros (EUR)", callback_data='eur')
    ],
    # [
    #     InlineKeyboardButton("Codechef", callback_data='CClist8'),
    #     InlineKeyboardButton("Spoj", callback_data='SPlist8')
    # ],
    # [
    #     InlineKeyboardButton("Codeforces", callback_data='CFlist8'),
    #     InlineKeyboardButton("ALL", callback_data='ALLlist8')
    # ]
]

reply_markup = InlineKeyboardMarkup(keyboard)


# Command
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text=f"🦾 Bienvenido {update.effective_chat.first_name} (ID: {update.effective_chat.id})\n\n🤖 Soy CriptoHouse, el bot que te ayudará a gestionar y a crear alertas de tus criptomonedas favoritas.\n🧐 Si necesitas saber de qué soy capaz utiliza el comando /help\n\n💰 Empecemos por saber cuál es la moneda en la prefieres ver el precio de tus criptomonedas:",
        reply_markup=reply_markup
    )


# Callback && Buttons Actions
def callback_buttons_handler(update: Update, context: CallbackContext):
    callback = update.callback_query.data
    chat_id = update.effective_chat.id

    print(callback)
    if callback == 'usd':
        context.bot.send_message(
            chat_id=chat_id,
            text='Ahora el precio de todas tus criptos se mostrará en esta moneda: Dólares (USD)',
        )
    elif callback == 'eur':
        context.bot.send_message(
            chat_id=chat_id,
            text='Ahora el precio de todas tus criptos se mostrará en esta moneda: Euros (EUR)',
        )


# Action
start_command = CommandHandler('start', start)
currency_buttons = CallbackQueryHandler(callback_buttons_handler)
