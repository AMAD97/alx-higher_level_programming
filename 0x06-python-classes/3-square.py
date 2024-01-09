#!/usr/bin/python3
"""A simple square class."""


class Square:
    """Represents a square shape.

    Attributes:
        __size (int): Length of the side of the square.
    """

    def __init__(self, size=0):
        """Initialize a square with a specified side length.

        Args:
            size (int): The length of the side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square (side length squared).
        """
        return self.__size * self.__size
