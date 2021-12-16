from telegram.ext import*  # You need to install python-telegram-bot in your IDE before you can import from telegram.ext
import responses as R

API_KEY="xxxxxxxxxxxxxxxx" # The API key should be a string given to you by Bot Father


def handle_message(update, context):
    text= str(update.message.text).lower() 
    reponse=R.respond(text) # The respond function is defined in the responses pyfile
    update.message.reply_text(reponse)

def error(update,context): # Just in case any error occurs
    print(f"Update{update}caused error{context.error}")

def main():
    
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main() # Run the main function
