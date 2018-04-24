from preprocess import get_contours
from api import recognize
from bot import start_with_method
 
IMG_PATH = '/Users/wirthjan/maff/formula.jpg'

def recognition_method (notify):
  try:
    notify('reading...')
    contours = get_contours(IMG_PATH)
    notify('writing down...')
    return recognize(contours)
  except:
    notify('something went wrong :x')

start_with_method(recognition_method)
