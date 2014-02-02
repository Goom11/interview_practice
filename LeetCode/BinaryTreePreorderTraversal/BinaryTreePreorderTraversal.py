#!/usr/bin/python


def preorderTraversal(root):
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node:
            print node.val
            stack.append(node.right)
            stack.append(node.left)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node('F')
root.left = Node('B')
root.left.left = Node('A')
root.left.right = Node('D')
root.left.right.left = Node('C')
root.left.right.right = Node('E')
root.right = Node('G')
root.right.right = Node('I')
root.right.right.left = Node('H')

preorderTraversal(root)
