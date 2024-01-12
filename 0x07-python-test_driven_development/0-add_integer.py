#!/usr/bin/python3
"""module for add_integer module"""



def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
        a (int or float): The first number.
        b (int or float, default: 98): The second number.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__== "__main__":
    import doctest
    doctest.testfile("test/0-add_integer.txt")
