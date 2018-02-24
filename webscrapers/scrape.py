import urllib2

part1 = """
<div style='margin: 40px;'>

<form>
  URL:<br>
 <input type="text" name="url" value =
 """


part2 = """
      ><br>
      key:<br>
      <input type="text" name="key">
      <input type="submit" value="Submit">
      <form action="">
    </form>

    </div>
    """


def quote(str):
    return '"' + str + '"'


def form(url):
    return  part1 + quote(url) + part2



def parse(str):
    str2 = str.lstrip("/").lstrip("?")
    parts = str2.split("&")
    return dict(map(lambda x: x.split("="), parts))

def grab_page(url):
  response = urllib2.urlopen(url)
  return response.read()

def filter_with_key(items, key):
    items2 = list(filter(lambda x: x.find(key) >= 0, items))
    return list(filter(lambda x: x.find("meta") == -1, items2))


def replyPage(url, key):
    url2 = "http://" + url
    text = grab_page("http://" + url)
    lines = text.split("\n")
    print "Number of lines (1): " + str(len(lines))
    # lines = list(map((lambda x: x.lower()), text.split("\n")))
    lines2 = filter_with_key(lines, key)
    print "Number of lines (2): " + str(len(lines2))
    print "URLLL: " + url
    output = form(url)
    output = output + "\n\n<div style='margin-top:20px; margin-left:40px;'><p>Hits = " + str(len(lines2)) + "</p>\n"
    for line in lines2:
        output = output +  "<div style='margin-bottom:10px;'>\n" + line.strip() + "\n</div>\n\n"
    output = output  + "\n</div>\n"
    return output


def reply(request):
    arg = parse(request)
    url = arg['url']
    key = arg['key']
    return replyPage(url, key)
