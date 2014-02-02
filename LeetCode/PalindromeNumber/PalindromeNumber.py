#!/usr/bin/python


def isPalindrome(x):
    div = 1
    while (x / div >= 10):
        div *= 10
    while (x >= 10):
        first = x / div
        last = x % 10
        if (first != last):
            return False
        x %= div
        x /= 10
        div /= 100
    return True
