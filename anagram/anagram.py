#!/usr/bin/python

from collections import defaultdict


def anagram(a, b):
    if (len(a) != len(b)):
        return False
    char_set = defaultdict(int)
    for char in a:
        char_set[char] += 1
    for char in b:
        char_set[char] -= 1
    for char, amount in char_set.iteritems():
        if amount != 0:
            return False
    return True

a = "Hello"
b = "olelH"
print a, "is",
if not anagram(a, b):
    print "not",
print "an anagram of", b
