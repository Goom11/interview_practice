#!/usr/bin/python

from collections import defaultdict

def isUniqueChars(s):
  char_set = defaultdict(bool)
  for char in s:
    if (char_set[char]):
      return False
    char_set[char] = True
  return True

str1 = "SO NDUPE"
print str1
if (isUniqueChars(str1)):
  print "doesn't have duplicates"
else:
  print 'has duplicates'
str2 = "SO NDUPES"
print str2
if (isUniqueChars(str2)):
  print "doesn't have duplicates"
else:
  print 'has duplicates'
