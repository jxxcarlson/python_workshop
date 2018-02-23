from generate import generate

def parse(str):
    parts = str.lstrip("/").split("&")
    return dict(map(lambda x: x.split("="), parts))

def reply(request):
    arg = parse(request)
    if 'n' in arg:
      n = int(arg['n'])
      data =  generate(0,n)
      return str(data)
    else:
      return []
