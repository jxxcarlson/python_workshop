# File: randomWalk.py
import sys
from generate import generate

n = int(sys.argv[2])
a = int(sys.argv[1])
output = generate(a, n)
print output
