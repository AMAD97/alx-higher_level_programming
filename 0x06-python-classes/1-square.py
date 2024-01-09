#!/usr/bin/python3
"""Module for handling squares."""


class Square:
    """Represents a square shape.

    Attributes:
        __size (int): Length of the side of the square.
    """

    def __init__(self, size):
        """Initialize the Square with a specified side length.

        Args:
            size (int): Length of the side of the square.
        """
        self.__size = size
