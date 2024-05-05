import arrr
from pyscript import document
import telebot


TOKEN = 7000647312:AAEZ0t5ZX8GT3ZdhCtCYXZ_iii0Yns52TTY
GROUP_CHAT_ID = -1002106472139
name = 'main'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    # Проверяем, содержит ли сообщение ключевое слово для пересылки
    if 'объявление' in message.text.lower():
        bot.forward_message(GROUP_CHAT_ID, message.chat.id, message.message_id)

@bot.message_handler(content_types=['photo', 'document', 'audio', 'video'])
def handle_media_messages(message):
    # Проверяем, содержит ли подпись к медиафайлу ключевое слово
    if message.caption and 'объявление' in message.caption.lower():
        bot.forward_message(GROUP_CHAT_ID, message.chat.id, message.message_id)


if name == 'main':
    bot.polling(none_stop=True)



def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)
