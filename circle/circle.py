import math


class Circle:
    """
    A class representing a circle.
    Attributes:
        radius (float): The radius of the circle
    Methods:
        get_radius(): Get the radius of the circle
        set_radius(radius): Set the radius of the circle
        get_area(): Calculate the area of the circle.
        get_perimeter(): Calculate the perimeter of the circle
        __mul__(n): Multiply the circle's radius by a number.
        __repr__(): Representation of the circle object.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance with a given radius.
        Args:
            radius (float): The radius of the circle.
        """
        self.__validate_value(value=radius)
        self.radius = radius

    @staticmethod
    def __validate_value(value):
        if value <= 0:
            raise ValueError(f"This value is less than 0: {value}")

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.__validate_value(value=radius)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __mul__(self, n):
        self.__validate_value(value=n)
        return Circle(self.radius * n)

    def __repr__(self):
        return f"{self.radius}"
