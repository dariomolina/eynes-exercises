import unittest
import math
from circle import Circle


class CircleTestCases(unittest.TestCase):

    msg_multiply_by_zero = "Multiplying with zero should raise a ValueError"
    msg_multiply_by_negative = ("Multiplying with a negative number should "
                                "raise a ValueError")

    def test_init(self):
        with self.assertRaises(ValueError, msg=self.msg_multiply_by_zero):
            Circle(0)

        with self.assertRaises(ValueError, msg=self.msg_multiply_by_negative):
            Circle(-1)

    def test_get_radius(self):
        expected = 3
        output = Circle(3).get_radius()
        self.assertEqual(
            expected,
            output,
            (f"For a circle of radius 3, expected "
             f"radius to be {expected} but got {output}"))

    def test_get_perimeter(self):
        expected = 2 * math.pi * 3
        output = Circle(3).get_perimeter()
        self.assertEqual(
            expected,
            output,
            (f"For a circle of radius 3, expected "
             f"perimeter to be {expected} but got {output}")
        )

    def test_get_area(self):
        expected = math.pi * 9
        output = Circle(3).get_area()
        self.assertEqual(
            expected,
            output,
            (f"For a circle of radius 3, expected area "
             f"to be {expected} but got {output}")
        )

    def test_set_radius(self):
        c = Circle(2)
        with self.assertRaises(ValueError, msg=self.msg_multiply_by_zero):
            c.set_radius(0)
        with self.assertRaises(ValueError, msg=self.msg_multiply_by_negative):
            c.set_radius(-1)

        # test with a valid radius
        radius = 4.2
        c.set_radius(radius=radius)
        self.assertEqual(radius, c.get_radius())

    def test_mul(self):
        c = Circle(2)
        try:
            new_circle = c * 3
            assert 6 == new_circle.get_radius(), (
                f"Expected new circle with radius "
                f"6 but got {new_circle.get_radius()}"
            )

            with self.assertRaises(ValueError, msg=self.msg_multiply_by_zero):
                c * 0
            with self.assertRaises(ValueError,
                                   msg=self.msg_multiply_by_negative):
                c * -1
        except ValueError:
            raise TypeError(
                "It seems there's a missing magic method (dunder method)")

    def test_repr(self):
        radius = 50
        c = Circle(radius=radius)
        self.assertEqual(str(radius), c.__repr__())
