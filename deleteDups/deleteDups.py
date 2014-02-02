#!/usr/bin/python


def deleteDups(n):
    return list(set(n))

a = [1, 2, 3, 4, 4, 4, 5, 4, 2, 6, 1, 7, 865]
a = deleteDups(a)
for x in a:
    print x,
print
