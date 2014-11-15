#!/usr/bin/env python

def first(s, n=1):
    """
    Returns the first n elements of s.
    Default value for n is 1.
    """
    return s[:n]

def rest(s, at=1):
    """
    Returns the rest of the elements of s after at.
    Default value for at is 1.
    """
    return s[at:]

def match(pattern, string, mapping={}):
    """
    Returns a mapping of pattern variables to string expressions.
    Returns None if the pattern cannot be matched.
    """
    if mapping == None:
        return mapping
    if not len(pattern) and not len(string):
        return mapping
    if not len(pattern) or not len(string):
        return None
    var = first(pattern)
    if var in mapping:
        expr = mapping[var]
        if string.startswith(expr):
            return match(rest(pattern), rest(string, len(expr)), mapping)
        return None
    for i in xrange(1, len(string) + 1):
        expr = first(string, i)
        print var, expr
        mapping[var] = expr
        m = match(pattern[1:], string[i:], mapping)
        if m != None:
            return m
        mapping.pop(var)
    return None
