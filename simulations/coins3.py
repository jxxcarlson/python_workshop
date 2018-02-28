
import random as r
import sys
from coin_tools import count_heads

def heads_or_tails():
    if r.random() < 0.5:
        return "H"
    else:
        return "T"

def run (n):
  output = ""
  for k in range(0,n):
    output = output + heads_or_tails()
  return output

n = int(sys.argv[1])
output = run(n)
heads = count_heads(output)
frequency = float(heads)/n

print [frequency, heads, heads - n/2.0]
# print output
