import sys

commandDict = {
  "test": lambda x: test(x),
  "add": lambda x: add(x),
  "analyze": lambda x: analyze(x)
 }

def test(args):
    print args

def add(args):
    print float(args[0]) + float(args[1])

def analyze(args):
    file_name = args[0]
    f = open(file_name,"r")
    data = f.read()
    f.close()
    print data
    print "Characters:", len(data)


def run():
     sys.argv.pop(0)
     cmd = sys.argv.pop(0)
     args = sys.argv
     if cmd in commandDict:
         commandDict[cmd](args)
     else:
         print "Sorry boss, I don't understand that command"


run()
