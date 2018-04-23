from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import pprint
print('hi')

def start_bot ():

  TOKEN = '551273072:AAGlazl70vLRRyaCPbEiCF_2a0Mf0fzdejM'

  updater = Updater(token=TOKEN)

  logging.basicConfig(format='%(asctime)s - %(name)s', level=logging.INFO)

  def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please be nice")
  start_handler = CommandHandler('start', start)

  def process_image(bot, update):
    photo = update.message.photo[3]
    print(photo)
    newFile = bot.get_file(photo.file_id)
    newFile.download('formula.jpg')
    bot.send_message(chat_id=update.message.chat_id, text='got image')

  image_handler = MessageHandler(Filters.photo, process_image)

  updater.dispatcher.add_handler(start_handler)
  updater.dispatcher.add_handler(image_handler)
  updater.start_polling()
