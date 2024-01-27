import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = 'YOUR_BOT_TOKEN'
QUESTIONS_FILE = 'questions.json'  # Provide the path to your JSON file

# Load questions from the JSON file
with open(QUESTIONS_FILE, 'r') as file:
    quiz_data = json.load(file)

current_question = 1

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Quiz Bot! Type /quiz to start the quiz.')

def quiz(update: Update, context: CallbackContext) -> None:
    global current_question
    question_data = quiz_data.get(str(current_question))

    if question_data:
        question = question_data['question']
        update.message.reply_text(f'Question {current_question}: {question}')
    else:
        update.message.reply_text('Quiz completed! Type /start to begin again.')

def check_answer(update: Update, context: CallbackContext) -> None:
    global current_question
    user_answer = update.message.text.lower()
    correct_answer = quiz_data[str(current_question)]['answer'].lower()

    if user_answer == correct_answer:
        update.message.reply_text('Correct! Well done.')
    else:
        update.message.reply_text(f'Incorrect. The correct answer is: {correct_answer}')

    current_question += 1
    context.job_queue.run_once(quiz, 5)

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("quiz", quiz))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, check_answer))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
