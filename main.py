from urllib import request, parse
import urllib
from recognizer import get_contours
 
IMG_PATH = '/Users/wirthjan/maff/formula.jpg'
ENDPOINT = "http://cat.prhlt.upv.es/mer/eq.php"

def recognize(contours):

  print('making request...')
  data = str(contours)
  payload = "strokes=" + parse.quote(data.encode("utf-8"))

  full_url = ENDPOINT
  response = request.urlopen(full_url, parse.unquote_to_bytes(payload))
  return str(response.read()).strip()

print('getting contours...')
contours = get_contours(IMG_PATH)
print(recognize(contours))
