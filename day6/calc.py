import sys
print sys.argv

cmd = sys.argv[1]
a = float(sys.argv[2])
b = float(sys.argv[3])

if cmd == "add":
    print a + b
elif cmd == "mul":
    print a*b
else:
    print "Sorry, boss, I can't do that"
