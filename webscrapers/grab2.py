# grab2.py
# grab a web page and extract the part the begins
# with the tags BEGIN and END
# Usage: python grab.py foo.txt http://www.bar.com
# BEGIN END
# Try this url:
# python grab2.py http://offcenterapps.com/zimeo/poems/poe-raven.html '<text>' '</text>'
#

import urllib2, sys

def grab_page(url):
  response = urllib2.urlopen(url)
  return response.read()


def grab_element(source, start_index, start_tag,
end_tag):
  i = source.find(start_tag, start_index)
  if i == -1:
    return [-1, ""]
  else:
    i = i + len(start_tag)
    j = source.find(end_tag, i)
    if j == -1:
      return [-1, ""]
    else:
      return [i, source[i:j]]

def run():
  text = grab_page(sys.argv[1])
  element = grab_element(text, 0, sys.argv[2],sys.argv[3])
  if element[0] == -1:
    print "nothing found"
  else:
    print element[1]


run()
