# grab.py
# grab a web page
#
# Usage: python grab.py http://www.bar.com/blah-blah.txt
#
# Try this:
#
# python grab.py http://offcenterapps.com/zimeo/poems/poe-raven.html
#

import urllib2, sys

def grab_page(url):
  response = urllib2.urlopen(url)
  return response.read()

def run():
  text = grab_page(sys.argv[1])
  print text

run()
