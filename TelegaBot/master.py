import telebot
import os
import random

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = 'YOUR_BOT_TOKEN'

# Путь к папке с изображениями
image_folder = '/content/images'
images = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder)]

# Создание объекта бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row("Получить кота")

    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! Я могу прислать тебе котиков.",
        reply_markup=user_markup,
    )

# Обработчик нажатия кнопки "Получить изображение"
@bot.message_handler(func=lambda message: message.text == "Получить кота")
def send_random_image(message):
    chat_id = message.chat.id

    if images:
        random_image = random.choice(images)
        images.remove(random_image)  # Удаление изображения из списка

        with open(random_image, 'rb') as photo:
            bot.send_photo(chat_id, photo)

    else:
        bot.send_message(chat_id, "Коты закончились 😔")

if __name__ == '__main__':
    bot.polling(none_stop=True)