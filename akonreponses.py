def respond(input):
    user_message=str(input).lower() # Make sure the bot won't miss the message due to capitalisation

    if "keyword" in user_message : # Once the keyword is detected in a message 

       return 'Any response you like' # Your bot will reply to the message with this response


    if "Other keyword" in user_message : # Once the keyword is detected in a message 

       return 'Another response you like' # Your bot will reply to the message with this response
