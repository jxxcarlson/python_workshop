    # File: get_data.py
    # Assumpions.  The file consists
    # of comment lines and data lines.
    # A comment line begins with '#' and
    # is ignored.  A data line has the form
    # a,b where a and b are data values,
    # e.g., '1880,-0.12'.  The function
    # getData(foo.txt) returns a list of
    # data values [[a1,b1], [a2,b2], ...]

# https://mathieularose.com/function-composition-in-python/
# https://docs.python.org/3/howto/functional.html


def get_data(file_name):

    file = open(file_name)
    data = file.read()
    file.close()

    lines = data.split("\n")
    data_lines = [x for x in lines if x.find("#") != 0]
    pairs1 = map(lambda x: x.split(","), data_lines)
    pairs2 = [x for x in pairs1 if len(x) == 2]
    pairs3 = map(lambda x: [x[0].strip(), x[1].strip()], pairs2)
    return pairs3

def first(data):
    return [ x[0] for x in data]

def second(data):
    return [ x[1] for x in data]

def to_int(data):
    return [int(x) for x in data]

def to_float(data):
    return [float(x) for x in data]

def mean(data):
    return sum(data)/len(data)
