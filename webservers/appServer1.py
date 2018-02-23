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

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from sys import argv

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile  .write("Hello!")

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()


if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
