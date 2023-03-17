# Import necessary modules
import openai
import telebot
import config

# Set API key to use OpenAI API
openai.api_key = config.open_ai_key

# Create an instance of the Telegram bot
bot = telebot.TeleBot(config.tel_bot_api)

# Create a handler for all received messages
@bot.message_handler(func=lambda _: True)
def handle_message(message):
    # Send a request to the OpenAI GPT-3 model with parameters
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=message.text,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    # Respond to the user with the text obtained from the model
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])

# Start an infinite loop to poll for new messages with a timeout (in seconds)
bot.infinity_polling(timeout=20, long_polling_timeout=10)
