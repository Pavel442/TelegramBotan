import telegram
import Config
import time

def main():
  while True:
    try:
      bot = telegram.Bot(token=Config.TOKEN)
      bot.send_message(chat_id=Config.CHAT_ID,
      text='Бот запущен')
      print(2/0)
    except ConnectionError:
      bot.send_message(chat_id=Config.CHAT_ID,
      text='Ошибка соединения')
    except Exception as e:
      bot.send_message(chat_id=Config.CHAT_ID,
      text='Бот упал с ошибкой')
      bot.send_message(chat_id=Config.CHAT_ID,
      text=str(e))
    time.sleep(90)
main()