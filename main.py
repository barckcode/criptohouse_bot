import os
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

# Internal Modules
from commands.start import start_command, currency_buttons
from commands.help import help_command


updater = Updater(
    token=os.environ['TOKEN_BOT'],
    use_context=True
)

dispatcher = updater.dispatcher


# Commands List
dispatcher.add_handler(start_command)
dispatcher.add_handler(currency_buttons)
dispatcher.add_handler(help_command)


# def echo(update, context):
#     context.bot.send_message(
#         chat_id=update.effective_chat.id, text=update.message.text
#     )


# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)


# def caps(update, context):
#     text_caps = ' '.join(context.args).upper()
#     context.bot.send_message(
#         chat_id=update.effective_chat.id, text=text_caps
#     )


# caps_handler = CommandHandler('caps', caps)
# dispatcher.add_handler(caps_handler)


# def inline_caps(update, context):
#     query = update.inline_query.query
#     if not query:
#         return
#     results = list()
#     results.append(
#         InlineQueryResultArticle(
#             id=query.upper(),
#             title='Caps',
#             input_message_content=InputTextMessageContent(query.upper())
#         )
#     )
#     context.bot.answer_inline_query(update.inline_query.id, results)


# inline_caps_handler = InlineQueryHandler(inline_caps)
# dispatcher.add_handler(inline_caps_handler)


# def unknown(update, context):
#     context.bot.send_message(
#         chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command."
#     )


# unknown_handler = MessageHandler(Filters.command, unknown)
# dispatcher.add_handler(unknown_handler)


if __name__ == '__main__':
    updater.start_polling()
