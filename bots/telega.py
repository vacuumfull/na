import time
import config
import telebot


bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)


def send_link(slug):
    link = '{!s}{!s}'.format(config.base_url, slug)
    bot.send_message(config.channel, link)
    # Спим секунду, чтобы избежать разного рода ошибок и ограничений (на всякий случай!)
    time.sleep(1)

def send_text(text):
    bot.send_message(config.channel, text)
    time.sleep(1)


if __name__ == '__main__':
    bot.polling(none_stop=True)
    send_text('huihui')
