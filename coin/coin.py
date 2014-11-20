#!/usr/bin/env python

def coinRec(amount, denominations):
    "Recursive solution, not optimal"
    if amount < 0:
        return None
    if not amount:
        return [[]]
    if not len(denominations):
        return None
    denominations = sorted(denominations, reverse=True)
    withTopCoin = coinRec(amount - denominations[0], denominations)
    if withTopCoin:
        for result in withTopCoin:
            result.append(denominations[0])
    else:
        withTopCoin = []
    withOtherCoins = coinRec(amount, denominations[1:])
    if not withOtherCoins:
        withOtherCoins = []
    return withTopCoin + withOtherCoins

import copy

def coin(amount, denominations):
    "Optimal Dynamic Programming Solution"
    denominations = sorted(denominations)
    acc = [[[] for _ in xrange(len(denominations) + 1)] for _ in xrange(amount + 1)]
    for i in xrange(1, amount + 1):
        acc[0][i] = [[]]
    for a in xrange(1, amount + 1):
        for d in xrange(1, len(denominations) + 1):
            if a - denominations[d - 1] >= 0:
                withTopCoin = copy.deepcopy(acc[a - denominations[d - 1]][d])
                for result in withTopCoin:
                    result.append(denominations[d - 1])
                acc[a][d] = withTopCoin
            acc[a][d] = acc[a][d] + acc[a][d - 1]
    print(acc[amount][len(denominations)])
