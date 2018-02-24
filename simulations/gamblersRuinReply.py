# File: gambersRuinReply

from gamblersRuin import generate

def parse(str):
    parts = str.lstrip("/").split("&")
    return dict(map(lambda x: x.split("="), parts))

def reply(request):
    arg = parse(request)
    if 'stake' in arg:
      stake = int(arg['stake'])
      data =  generate(stake,5000)
      return str(data)
    else:
      return []
