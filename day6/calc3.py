import sys



def test(args):
    print args

def add(args):
    print float(args[0]) + float(args[1])

def mul(args):
    print float(args[0]) * float(args[1])

commandDict = {
  "test": lambda x: test(x),
  "add": lambda x: add(x),
  "mul": lambda x: mul(x)
 }

def run():
     sys.argv.pop(0)
     cmd = sys.argv.pop(0)
     args = sys.argv
     if cmd in commandDict:
         commandDict[cmd](args)
     else:
         print "Sorry boss, I don't understand that command"


run()
