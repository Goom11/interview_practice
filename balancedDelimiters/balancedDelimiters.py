#!/usr/bin/env python

def isBalanced(string):
    "Returns True if the string contains only balanced delimiters"
    braces = {'{':'}', '(':')', '[':']'}
    return isBalancedAcc(string, braces)

def is_stack_empty(stack):
    "Returns True if the stack is empty"
    return not stack

def peek_stack(stack):
    "Returns the top element of the stack"
    return stack[-1]

def is_open_delimiter(ch, braces):
    return ch in braces

def get_matching_close_delimiter(ch, braces):
    return braces[ch]

def isBalancedAcc(string, braces, stack=[]):
    """
    Return True if the string contains only balanced delimiters.
    Given a set of delimiters, braces, and optionally, a starting stack.
    """
    for ch in string:
        if is_open_delimiter(ch, braces):
            stack.append(ch)
        elif is_stack_empty(stack):
            return False
        elif ch != get_matching_close_delimiter(peek_stack(stack), braces):
            return False
        else:
            stack.pop()
    if is_stack_empty(stack):
        return True
    return False
