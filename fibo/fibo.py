#!/usr/bin/python

memo = [0, 1]


def fibo(n):
    if n < 0:
        return -1
    size = len(memo)
    if n < size:
        return memo[n]
    for i in xrange(size, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])
    return memo[n]

print fibo(0)
print fibo(1)
print fibo(100000)
print fibo(100000-1)
