#!/usr/bin/python

for i in xrange(1,101):
  s = ""
  if i % 3 == 0:
    s += "Fizz"
  if i % 5 == 0:
    s += "Buzz"
  print i if len(s) == 0 else s
