"""
Submit to the endpoint of http://cat.prhlt.upv.es/mer/
"""
from urllib import request, parse
import urllib

ENDPOINT = "http://cat.prhlt.upv.es/mer/eq.php"
def recognize(contours):
  # convert our nd list to encoded form data
  payload = "strokes=" + parse.quote(str(contours).encode("utf-8"))

  # convert data to bytes and submit
  response = request.urlopen(ENDPOINT, parse.unquote_to_bytes(payload))

  # clean up result
  return str(response.read().decode('UTF-8')).rstrip('\r\n')
