import random

def generate(n, initial_value):
    x = initial_value
    output = [x]
    for i in range(1,n):
        x = x + 2*random.randint(0,1) - 1
        output.append(x)
    return output

def writeData(data, fileName):
    file = open(fileName,"w")
    file.write(str(data))
    file.close()
