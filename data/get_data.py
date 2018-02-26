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

from compose import compose


def get_data(file_name):

    file = open(file_name)
    data = file.read()
    file.close()

    transform = compose(strip, remove_bad_data, to_twoList, remove_comments, string_to_lines)

    return transform(data)



def remove_comments(data):
    return [x for x in data if x.find("#") != 0]

def string_to_lines(data):
    return data.split("\n")

def to_twoList(data):
    return map(lambda x: x.split(","), data)

def remove_bad_data(data):
    return [x for x in data if len(x) == 2]

def strip(data):
    return map(lambda x: [x[0].strip(), x[1].strip()], data)

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

def smooth(data, window):
  output = []
  n = len(data)
  for k in range(0, n - window + 1):
      segment = data[k:(k + window)]
      value = sum(segment)/window
      output.append(value)
  return output

def drop_window(data, window):
  return data[window-1:]
