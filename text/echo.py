# File: echo.py

import sys

f = open(sys.argv[1], "r")
data = f.read()
f.close()
print data
