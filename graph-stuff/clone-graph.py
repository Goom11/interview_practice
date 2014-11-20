#!/usr/bin/env python

class Node(object):
    def __init__(self, children):
        self.children = children

def cloneGraph(startNode):
    return Node([cloneGraph(node) for node in startNode.children])

