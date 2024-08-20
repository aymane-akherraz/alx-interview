#!/usr/bin/python3
""" Making Change Problem """


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed
    to meet a given amount total
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    nb_coins = 0
    for c in coins:
        if c <= total:
            while total - c >= 0:
                total -= c
                nb_coins += 1
            if total == 0:
                return nb_coins

    return -1
