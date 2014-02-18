def increment_counter(counter, lengths):
    counter.reverse()
    lengths.reverse()
    for c, length in zip(counter, lengths):
        c += 1
        if c == length:
            c = 0
        else:
            break
    counter.reverse()     
    return counter


def all_words(words):
    lengths = [len(word) for word in words]
    counter = [0 for _ in words]
    while (True):
        output = ""
        for i, c in enumerate(counter):
            output += words[i][c]
        print output
        if counter == lengths:
            break
        counter = increment_counter(counter, lengths)
