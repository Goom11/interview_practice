#!/usr/bin/python

from collections import OrderedDict

def removeDuplicates(a):
  return ''.join(OrderedDict.fromkeys(a))
  

s = "Hello"
print s, "with duplicates removed is", removeDuplicates(s)
