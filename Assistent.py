# Импортируем необходимые модули
import openai
import telebot
import config


# Устанавливаем ключ для использования API OpenAI
openai.api_key = config.open_ai_key

# Создаём экземпляр телеграм-бота
bot = telebot.TeleBot(config.tel_bot_api)

# Создаём обработчик для всех получаемых сообщений
@bot.message_handler(func=lambda _: True)
def handle_message(message):
    # Отправляем запрос к модели GPT-3 OpenAI с параметрами
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=message.text,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    # Отвечаем пользователю текстом, полученным от модели
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])

# Запускаем бесконечный цикл опроса новых сообщений с временной задержкой (в секундах)
bot.infinity_polling(timeout=20, long_polling_timeout=10)
