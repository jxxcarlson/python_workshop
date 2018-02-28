# FIle: coin_tools.py

def count_heads(str):
  heads = 0
  for letter in list(str):
      if letter == 'H':
          heads = heads + 1
  return heads
