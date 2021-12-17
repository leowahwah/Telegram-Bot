from telegram.ext import*  # You need to install python-telegram-bot in your IDE before you can import from telegram.ext


API_KEY="xxxxxxxxxxxxxxxx" # The API key should be a string given to you by Bot Father


def handle_message(update, context):
    text= str(update.message.text).lower() 
    reponse=respond(text) # The respond function is defined in the responses pyfile
    update.message.reply_text(reponse)
    
    
def respond(input):
    user_message = str(input).lower() # Make sure the bot won't miss the message due to capitalisation

    if "keyword" in user_message : # Once the keyword is detected in a message 

       return 'Any response you like' # Your bot will reply to the message with this response


    if "Other keyword" in user_message : # Once the keyword is detected in a message 

       return 'Another response you like' # Your bot will reply to the message with this response


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
