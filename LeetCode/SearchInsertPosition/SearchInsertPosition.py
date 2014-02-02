#!/usr/bin/python

def searchInsert(nums, target):
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)
