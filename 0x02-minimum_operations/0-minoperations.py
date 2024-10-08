#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n 'H' characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations
    needed to result in exactly n 'H' characters.

    Args:
    n (int): desired number of 'H' characters.

    Returns:
    int: minimum number of operations else 0
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
