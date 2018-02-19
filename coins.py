
import random as r

def heads_or_tails():
    if r.random() < 0.5:
        return "H"
    else:
        return "T"

def run(n):
  output = ""
  for k in range(0,n):
    output = output + heads_or_tails()
  return output
