from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import pprint

WELCOME = """
Hey, I'm Maff.
Send me an image of your formula and I'll type it down for you :)
"""

def start_with_method (formula_recognition_method):

  TOKEN = '551273072:AAGlazl70vLRRyaCPbEiCF_2a0Mf0fzdejM'

  updater = Updater(token=TOKEN)

  logging.basicConfig(format='%(asctime)s - %(name)s', level=logging.INFO)

  def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=WELCOME)
  start_handler = CommandHandler('start', start)

  def process_image(bot, update):
    print("")
    print("Got new request.")
    notify(bot, update, "WIFI is crap over here. Hold on a sec.")
    photo = update.message.photo[3]
    newFile = bot.get_file(photo.file_id, timeout=30)
    newFile.download('formula.jpg', timeout=30)
    parsedFormula = formula_recognition_method(lambda msg: notify(bot, update, msg))
    bot.send_message(chat_id=update.message.chat_id, text=parsedFormula)

  image_handler = MessageHandler(Filters.photo, process_image)

  updater.dispatcher.add_handler(start_handler)
  updater.dispatcher.add_handler(image_handler)
  print('starting bot')
  updater.start_polling(timeout=1)

def notify(bot, update, msg):
  bot.send_message(chat_id=update.message.chat_id, text=msg)
  print(msg)
