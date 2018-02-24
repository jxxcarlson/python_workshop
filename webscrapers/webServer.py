#!/usr/bin/env python
"""
SOURCE: Source: https://gist.github.com/bradmontgomery/2219997

Very simple HTTP server in python.

To run, use
   python basicServer.py 8000
or
   ./basicServer.py [<port>]

To test:

    curl http://localhost:8000
"""
def form(url):
    return """
    <div style='margin: 40px;'>

    <form>
      URL:<br>
      <input type="text" name="url" value="nytimes.com"><br>
      key:<br>
      <input type="text" name="key">
      <input type="submit" value="Submit">
      <form action="">
    </form>

    </div>
    """


def parse(str):
    str2 = str.lstrip("/").lstrip("?")
    parts = str2.split("&")
    return dict(map(lambda x: x.split("="), parts))

def get_url(str):
    if str.find('url') >= 0:
      dictionary = parse(str)
      return dictionary['url']
    else:
        return ""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from sys import argv
from scrape import reply

class S(BaseHTTPRequestHandler):

    url = "foo"

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print "path:: " + self.path
        url = get_url(self.path)
        print "URL:: " + url
        self._set_headers()
        if self.path == "/":
           self.wfile.write(form(url))
        else:
           self.wfile.write(reply(self.path))

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()



run(port=int(argv[1]))
