#!/usr/bin/python3
"""0-making_change.py"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0
    remaining = total

    for coin in coins:
        while remaining >= coin:
            remaining -= coin
            count += 1

        if remaining == 0:
            return count

    return -1
