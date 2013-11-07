#!/usr/bin/python

def ReplaceFun(a):
  return a.replace(' ', '%20')

a = "a b c"
print a, "with spaces replaced is", ReplaceFun(a)
