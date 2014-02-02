#!/usr/bin/python


def maxProfit(prices):
    total = 0
    for i, price in enumerate(prices):
        if prices[i + 1] > price:
            total += prices[i + 1] - price
    return total
