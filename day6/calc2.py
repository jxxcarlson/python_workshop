import sys

commandDict = {
  "test": lambda x: test(x),
 }

def test(args):
    print args

def run():
    sys.argv.pop(0)
    cmd = sys.argv.pop(0)
    args = sys.argv
    if cmd in commandDict:
      commandDict[cmd](args)
    else:
      print "Sorry boss, I don't understand that command"

run()
