# Telegram-Bot

In general, the simple bot is able to reply to messages containing specific keywords you like. What's even more exciting is that it requires little to none coding skills! If you wish to make one using Python, it's super easy and just follow the steps below:

1. To create such Telegram bot, you first need to find Bot Father on Telegram and type /start.

2. Name your bot and an API token, or we say an API key, will be given to you by Bot Father. The Key is simply a string with many letters and numbers. You may want to keep the Key secret as anyone can alter your bot with the token.

3. Open your Python IDE and install the "python-telegram-bot" package. In case you are using PyCharm, you may install it via the Project Interpreter.

4. Copy the code from sample_api.main.py and set the variable API_KEY = "the string given by Bot Father". Quotation marks required. You don't have to make any further changes. We now focus on the making our bot to respond to specific keywords .

5. Now, the only thing you have to do is to edit the if statements and the return strings of the respond function on your own accord, such that your bot will reply to messages containing key words you desired. Run the program and your bot should be functioning! You may want to have it added into your Telegram groups. However, it may not respond to group messages.

6. To solve this, go to Bot Father again. Type /setprivacy then Disable.




And the problem shall be addressed and you are all set. Have fun!

