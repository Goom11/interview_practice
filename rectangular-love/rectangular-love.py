#!/usr/bin/env python

def get_endpoints(rect, dimension):
    end = 'width'
    if dimension == 'y':
        end = 'height'
    return (rect[dimension], rect[dimension] + rect[end])

def get_x_endpoints(rect):
    return get_endpoints(rect, 'x')

def get_y_endpoints(rect):
    return get_endpoints(rect, 'y')

def x_overlap(rect1, rect2):
    points = list(get_x_endpoints(rect1) + get_x_endpoints(rect2))
    points = sorted(points)
    return (points[1], points[2])

def y_overlap(rect1, rect2):
    points = list(get_y_endpoints(rect1) + get_y_endpoints(rect2))
    points = sorted(points)
    return (points[1], points[2])

def average(pair):
    return (pair[0] + pair[1])/2.0

def get_middle_point(rect):
    return (average(get_x_endpoints(rect)), average(get_y_endpoints(rect)))

def within_range(point, low, high):
    return point >= low and point <= high

def in_rectangle(point, rect):
    x_endpoints = get_x_endpoints(rect)
    y_endpoints = get_y_endpoints(rect)
    within_x = within_range(point[0], x_endpoints[0], x_endpoints[1])
    within_y = within_range(point[0], y_endpoints[0], y_endpoints[1])
    return within_x and within_y

def rectangular_love(rect1, rect2):
    x1, x2 = x_overlap(rect1, rect2)
    y1, y2 = y_overlap(rect1, rect2)
    result = {}
    result['x'] = x1
    result['y'] = y1
    result['width'] = x2 - x1
    result['height'] = y2 - y1
    result_middle = get_middle_point(result)
    if in_rectangle(result_middle, rect1):
        return result
    return None
