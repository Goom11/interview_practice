#!/usr/bin/python

class StackWithMin:
  def __init__(self):
    self.actualStack = []
    self.minStack = []

  def push(self, item):
    self.actualStack.append(item)
    if not self.minStack or item <= self.minStack[-1]:
      self.minStack.append(item)

  def pop(self):
    item = self.actualStack.pop()
    if item == self.minStack[-1]:
      self.minStack.pop()
    return item

  def getMin(self):
    return self.minStack[-1]

  def __len__(self):
    return len(self.actualStack)

  def empty(self):
    return not self.actualStack

  def top(self):
    return self.actualStack[-1]

first = StackWithMin()
for i in xrange(5):
  first.push(i)
if not first.empty():
  print "Not empty"
first.pop()
print "Top is", first.top()
print "Stack contains", len(first), "items"
print "The smallest element is", first.getMin()
