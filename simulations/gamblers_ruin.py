import random, sys

def generate(initial_value):
    x = initial_value
    n = 0
    output = [x]
    while x > 0 and n < 5000:
        n = n + 1
        x = x + 2*random.randint(0,1) - 1
        output.append(x)
    return output

def writeData(data, fileName):
    file = open(fileName,"w")
    file.write(str(data))
    file.close()


print ;'
    generate(int(sys.argv[1]))
