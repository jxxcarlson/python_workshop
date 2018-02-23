def add_word(word, dictionary):
    if word in dictionary:
        dictionary[word] = dictionary[word] + 1
    else:
        dictionary[word] = 1

def frequency_table(words):
    frequencies = dict()
    for word in words:
        add_word(word, frequencies)
    return frequencies
