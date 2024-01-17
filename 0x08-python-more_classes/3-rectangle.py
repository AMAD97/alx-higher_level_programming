#!/usr/bin/python3
"""
Module 3-rectangle
Defines a Rectangle class with private attributes width and height.
"""


class Rectangle:
    """
    Rectangle class with private attributes width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance.

        Parameters:
            - width (int): width of the rectangle (default is 0)
            - height (int): height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            - value (int): width to set.
        Raises:
            - TypeError: If width is not an integer.
            - ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            - value (int): height to set.
        Raises:
            - TypeError: If height is not an integer.
            - ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            - If width or height is 0, returns 0.
            - Otherwise, returns the perimeter.
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            - If width or height is 0, returns an empty string.
            - Otherwise, returns a string representation of the rectangle using '#'.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle for reproduction.

        Returns:
            - A string representation of the rectangle instance.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)


if __name__ == "__main__":
    # Example usage as shown in 3-main.py
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))
