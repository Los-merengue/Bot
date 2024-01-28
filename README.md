Steps to Create a Telegram Bot

1. Open Telegram and Search for BotFather \n
Open the Telegram app on your device.

In the search bar, type "BotFather" and select the official BotFather bot.
2. Start a Chat and Create a New Bot
Start a chat with BotFather by clicking the "Start" button.
Use the /newbot command to create a new bot.
3. Set Bot Name and Username
Follow the instructions provided by BotFather.
Set a name for your bot (e.g., "QuizBot").
Set a username for your bot; it must end in "bot" (e.g., "QuizBotOfficialBot").
4. Save Your Bot Token
Once the bot is created, BotFather will provide you with a unique token.
Save this token; it is required for authenticating your bot.
Using Your Bot Token
Copy the token provided by BotFather and use it in the quiz_bot.py script:

python
Copy code
TOKEN = 'YOUR_BOT_TOKEN'
Replace 'YOUR_BOT_TOKEN' with the actual token obtained from BotFather.

Running Your Bot
Open a terminal and navigate to the directory where quiz_bot.py is located.
Run the following command to start your bot:
bash
Copy code
python quiz_bot.py
Your Telegram Quiz Bot is now created and running! Users can interact with it in the Telegram app.