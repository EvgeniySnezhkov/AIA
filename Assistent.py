import openai
import telebot
import config


openai.api_key = config.open_ai_key
bot = telebot.TeleBot(config.tel_bot_api)


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=message.text,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


bot.infinity_polling(timeout=20, long_polling_timeout=10)
