#!/usr/bin/python

def isUniqueChars(s):
  char_set = [False] * 256
  for char in s:
    val = ord(char)
    if (char_set[val]):
      return False
    char_set[val] = True
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
