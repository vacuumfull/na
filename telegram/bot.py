import time
import telegram.config
import telebot


bot = telebot.TeleBot(telegram.config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)


def send_link(slug):
    link = '{!s}{!s}'.format(telegram.config.base_url, slug)
    bot.send_message(telegram.config.channel, link)
    time.sleep(1)

def send_text(text):
    bot.send_message(telegram.config.channel, text)
    time.sleep(1)


if __name__ == '__main__':
    bot.polling(none_stop=True)
