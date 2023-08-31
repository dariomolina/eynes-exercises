import unittest
import math
from circle import Circle


class CircleTestCases(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError, msg="Multiplying with zero should raise a ValueError"):
            Circle(0)
        with self.assertRaises(ValueError, msg="Multiplying with a negative number should raise a ValueError"):
            Circle(-1)

    def test_get_radius(self):
        expected = 3
        ouput = Circle(3).get_radius()
        self.assertEqual(
            expected, ouput, f"For a circle of radius 3, expected radius to be {expected} but got {ouput}")

    def test_get_perimeter(self):
        expected = 2 * math.pi * 3
        ouput = Circle(3).get_perimeter()
        self.assertEqual(
            expected, ouput, f"For a circle of radius 3, expected perimeter to be {expected} but got {ouput}")

    def test_get_area(self):
        expected = math.pi * 9
        ouput = Circle(3).get_area()
        self.assertEqual(
            expected, ouput, f"For a circle of radius 3, expected area to be {expected} but got {ouput}")

    def test_set_radius(self):
        c = Circle(2)
        with self.assertRaises(ValueError, msg="Multiplying with zero should raise a ValueError"):
            c.set_radius(0)
        with self.assertRaises(ValueError, msg="Multiplying with a negative number should raise a ValueError"):
            c.set_radius(-1)

    def test_mul(self):
        c = Circle(2)
        try:
            new_circle = c * 3
            assert 6 == new_circle.get_radius(), f"Expected new circle with radius 6 but got {new_circle.get_radius()}"

            with self.assertRaises(ValueError, msg="Multiplying with zero should raise a ValueError"):
                c * 0
            with self.assertRaises(ValueError, msg="Multiplying with a negative number should raise a ValueError"):
                c * -1
        except:
            raise TypeError(
                "It seems there's a missing magic method (dunder method)")
