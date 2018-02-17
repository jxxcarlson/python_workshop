
import urllib2, sys

def grab_page(url):
  response = urllib2.urlopen(url)
  return response.read()

def filter_with_key(items, key):
    items2 = list(filter(lambda x: x.find(key) >= 0, items))
    return list(filter(lambda x: x.find("meta") == -1, items2))

def run():

  text = grab_page(sys.argv[2])
  lines = text.split("\n")
  # lines = list(map((lambda x: x.lower()), text.split("\n")))
  lines2 = filter_with_key(lines, sys.argv[1])
  for line in lines2:
      print line
      print ""
  print ""
  print [len(lines), len(lines2)]

run()
