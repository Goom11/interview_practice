#!/usr/bin/python

def singleNumber(nums):
    counts =  {}
    for num in nums:
        counts[num] = counts.setdefault(num, 0) + 1
    for num, count in counts.iteritems():
        if count == 1:
            return num
