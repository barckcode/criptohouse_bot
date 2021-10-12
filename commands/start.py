from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.update import Update
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext.callbackcontext import CallbackContext


# Currency Buttons
list_of_currencies = {
    "Dolares": "usd",
    "Euros": "eur",
}

currency_list_buttons = [
    []
]

for currency, identifier in list_of_currencies.items():
    currency_list_buttons[0].append(
        InlineKeyboardButton(f"{currency} ({identifier.upper()})", callback_data=f"{identifier}")
    )
    # InlineKeyboardButton("Dólares (USD)", callback_data='usd'),
    # InlineKeyboardButton("Euros (EUR)", callback_data='eur')

currency_markup = InlineKeyboardMarkup(currency_list_buttons)


# Cripto Buttons
list_of_criptos = {
    "Bitcoin": "btc",
    "Ethereum": "eth",
    "Cardano": "ada",
    "Ripple": "xrp",
    "Solana": "sol",
    "Dogecoin": "doge",
    "Terra-luna": "luna",
    "Shiba-inu": "shib",
}

cripto_list_buttons = [
    [
        InlineKeyboardButton(f"Bitcoin (BTC)", callback_data='btc'),
        InlineKeyboardButton(f"Ethereum (ETH)", callback_data='eth'),
        InlineKeyboardButton(f"Cardano (ADA)", callback_data='ada'),
        InlineKeyboardButton(f"Ripple (XRP)", callback_data='xrp'),
    ],
    [
        InlineKeyboardButton(f"Solana (SOL)", callback_data='sol'),
        InlineKeyboardButton(f"Dogecoin (DOGE)", callback_data='doge'),
        InlineKeyboardButton(f"Terra-luna (LUNA)", callback_data='luna'),
        InlineKeyboardButton(f"Shiba-inu (SHIB)", callback_data='shib'),
    ]
]

cripto_markup = InlineKeyboardMarkup(cripto_list_buttons)


# Command
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text=f"🤖 CriptoHouse:\n\n🦾 Bienvenido {update.effective_chat.first_name} (ID: {update.effective_chat.id})\n\n🤖 Soy CriptoHouse, el bot que te ayudará a gestionar y a crear alertas de tus criptomonedas favoritas.\n🧐 Si necesitas saber de qué soy capaz utiliza el comando /help\n\n💰 Empecemos por saber cuál es la moneda en la prefieres ver el precio de tus criptomonedas:",
        reply_markup=currency_markup
    )


# Callback && Buttons Actions
def callback_buttons_handler(update: Update, context: CallbackContext):
    callback = update.callback_query.data
    chat_id = update.effective_chat.id

    print(callback)
    if callback == 'usd':
        context.bot.send_message(
            chat_id=chat_id,
            text='🤖 CriptoHouse:\n\n❗ Ahora el precio de todas tus criptos se mostrará en esta moneda: Dólares (USD)\n\n🪙 Elige ahora tus criptos favoritas (Si anteriormente elegiste ya tus criptos, no es necesario que vuelvas a repetir este proceso):',
            reply_markup=cripto_markup
        )
    elif callback == 'eur':
        context.bot.send_message(
            chat_id=chat_id,
            text='🤖 CriptoHouse:\n\n❗ Ahora el precio de todas tus criptos se mostrará en esta moneda: Euros (EUR)\n\n🪙 Elige ahora tus criptos favoritas (Si anteriormente elegiste ya tus criptos, no es necesario que vuelvas a repetir este proceso):',
            reply_markup=cripto_markup
        )

    for identifier in list_of_criptos.values():
        if callback == identifier:
            context.bot.send_message(
                chat_id=chat_id,
                text=f'🤖 CriptoHouse:\n\n❗ Has seleccionado: {callback.upper()}, puedes seguir eligiendo más criptos si lo deseas.'
            )


# Action
start_command = CommandHandler('start', start)
currency_buttons = CallbackQueryHandler(callback_buttons_handler)
