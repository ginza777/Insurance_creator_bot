from django.core.management.base import BaseCommand
from telegram.utils.request import Request
from django.conf import settings
from  telegram import Bot
from telegram.ext import Updater
from bot_police.settings import TOKEN
from bot_function.bot_function import *



#######

api_id='24990292'
api_hash="5cb886fc0d8c5d2ebe5d40ed6b50ab85"
from bot_police.settings import TOKEN
from telegram.ext import *
########


class Command(BaseCommand):
    help='Bu django telegram bot_function'

    def handle(self,*args,**options):
        request=Request(
        )
        bot=Bot(
            request=request,
            token=settings.TOKEN,


        )

        print(bot.get_me())


def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@geenza_bot' in text:
            new_text = text.replace('@geenza_bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    # Reply normal if the message is in private
    update.message.reply_text(response)


# Log errors
def error(update, context):
    print(f'error caused error {context.error}')
# Run the program
# if __name__ == '__boot__':
###########################################################################################################333

conv_handler = ConversationHandler(
                entry_points=[CommandHandler('start', start_command),
                MessageHandler(Filters.regex('^(New police)$'), New_police),
                  ],
    states={

        '1':  [
                CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text, From_time),
               ],
        '2':  [CommandHandler('cancel', New_police),
               CommandHandler('start', start_command),
               MessageHandler(Filters.text, Company_name),

                ],
        '3':  [ CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text, Name),

                ],
        '4':  [ CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text, Surname),

                ],
        '5':  [ CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text, Father_name),

                ],
        '6':  [ CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text, Phone_number),

                ],
        '7':  [ CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text, Model),

                ],
        '8':  [ CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text, Year),

                ],
        '9':  [ CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text, Davlat_raqami),

                ],
        '10': [ CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text, Motor),

                ],
        '11': [ CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text,Kuzov_raqami ),

                ],
        '12': [ CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text, Guvohnoma_seriya),

                ],
        '13': [ CommandHandler('cancel', New_police),
                CommandHandler('start', start_command),
                MessageHandler(Filters.text, Guvohnoma_raqami),

                ],
        'pdf': [
                CommandHandler('start', start_command),
                MessageHandler(Filters.regex('^(New police)$'), New_police),

                 ],

             },
fallbacks = [
    CommandHandler('start', start_command),
    error

]

)






    # Commands
# dp.add_handler(CommandHandler('start', start_command))
# dp.add_handler(CommandHandler('help', help_command))
# dp.add_handler(CommandHandler('custom', custom_command))
# dp.add_handler(MessageHandler(Filters.regex('^(New police)$'), New_police))

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('cancel', New_police))
updater.dispatcher.add_handler(conv_handler)


updater.start_polling()
updater.idle()


