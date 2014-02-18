#!/usr/bin/python

from collections import defaultdict


def anagram(a, b):
    char_set = defaultdict(int)
    if (len(a) != len(b)):
        return False
    for char_a, char_b in zip(a, b):
        char_set[char_b] -= 1
        char_set[char_a] += 1
    for _, amount in char_set.iteritems():
        if amount != 0:
            return False
    return True


def anagramify(words):
    buckets = {}
    for word in words:
        for key in buckets:
            if anagram(word, key):
                buckets[key].append(word)
                break
        else:
            buckets[word] = [word]
    result = [v for v in buckets.values()]
    return result
