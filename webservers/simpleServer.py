# File: simpleServer.py

import SimpleHTTPServer
import SocketServer
import sys

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "running on port", PORT
httpd.serve_forever()
