#!/usr/bin/env python
"""
https://gist.github.com/bradmontgomery/2219997

Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import os

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def get_data(self, fname):
        if os.path.exists(fname):
           with open(fname, 'rb') as f:
               try:
                  file = open("data.txt", "r")
                  return file.read()
               except : # whatever reader errors you care about
                  return "error: file not found"

    def do_GET(self):
        if self.path == "/data":
            message = self.get_data("data.txt")
        else:
            message = "I don't understand"
        self._set_headers()
        self.wfile.write(message)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
