#!/usr/bin/env python

from collections import deque

class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def zigzag(root):
    stack_left = []
    stack_right = [root]
    direction = "right"
    while stack_left or stack_right:
        if stack_left and direction == "left":
            node = stack_left.pop()
            print node.value
            if node.right:
                stack_right.append(node.right)
            if node.left:
                stack_right.append(node.left)
            if not stack_left:
                direction = "right"
        elif stack_right and direction == "right":
            node = stack_right.pop()
            print node.value
            if node.left:
                stack_left.append(node.left)
            if node.right:
                stack_left.append(node.right)
            if not stack_right:
                direction = "left"
