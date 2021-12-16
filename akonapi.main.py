from telegram.ext import* # You need to install python-telegram-bot in your IDE
import reponses as R


def handle_message(update, context):
    text= str(update.message.text).lower()
    reponse=R.respond(text) 
    update.message.reply_text(reponse)

def error(update,context):
    print(f"Update{update}caused error{context.error}")

def main():
    updater = Updater(mykey.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()
