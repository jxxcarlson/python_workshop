# news.py: Check New York Times to see if there
# is any news about Slobodia
#
# Example:
# $ python news.py Slobodia

import urllib2, sys

source = "http://nytimes.com"
response = urllib2.urlopen(source)
html = response.read()

if html.find(sys.argv[1]) >=0:
  print "There is news about " + sys.argv[1] + " today"
else:
  print "No news about " + sys.argv[1] + " today"
