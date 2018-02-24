# news.py: Check New York Times to see if there
# is any news about Slobodia
#
# Example:
# $ python news.py nytimes.com Slobodia

import urllib2, sys

source = "http://" + sys.argv[1]
response = urllib2.urlopen(source)
html = response.read()

print html.count(sys.argv[2])
