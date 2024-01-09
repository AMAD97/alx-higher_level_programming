#!/usr/bin/python3
"""Module defining a Square class."""


class Square:
    """Represent a square shape.

    This class represents a square and allows operations related to squares.

    Attributes:
        __size (int): Length of the side of the square.
    """

    def __init__(self, size=0):
        """Initialize a Square with a specified side length.

        Args:
            size (int): The length of the side of the square.
                It defaults to 0 if not provided.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
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
        return self.__size ** 2

    def perimeter(self):
        """Calculate the perimeter of the square.

        Returns:
            int: The perimeter of the square (4 times the side length).
        """
        return 4 * self.__size
