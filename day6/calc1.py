import sys

def run():
    if len(sys.argv) == 1:
        print "Hey, I need more arguments!"
    elif len(sys.argv) == 2:
        print "Hey, one more argument please!"
    else:
        really_run()

def really_run():
    sys.argv.pop(0)
    cmd = sys.argv.pop(0)
    args = sys.argv
    print "cmd: ", cmd
    print "args: ", args

run()
