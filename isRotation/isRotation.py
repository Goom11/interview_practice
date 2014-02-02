#!/usr/bin/python


def isRotation(str1, str2):
    length = len(str1)
    if length == len(str2) and length > 0:
        str1str1 = str1 + str1
        found = str1str1.find(str2)
        if found != -1:
            return True
    return False

print isRotation("abc", "bca")
