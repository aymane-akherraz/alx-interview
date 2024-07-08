#!/usr/bin/python3
""" Minimum Operations Interview Challenge """


def is_prime(n):
    """ Returns true if n is prime false otherwise """

    if n < 2:
        return False
    factor = 2
    while factor < n:
        if n % factor == 0:
            return False
        factor += 1
    return True


def get_next_prime(n):
    """
    Returns the next prime number greater to the number
    given as argument.
    """

    if n <= 1:
        return 2
    nb = n + 1
    while not is_prime(nb):
        nb += 1
    return nb


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """

    if n < 2:
        return 0

    factor = 2
    operations = 0
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor = get_next_prime(factor)

    return operations
