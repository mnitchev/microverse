import unittest
import math
from microverse.simulator import geometry, vec2


class TestUtilityFunctions(unittest.TestCase):
    def test_ray_intersect(self):
        result = geometry.ray_circle_intersect(
            (vec2(0, 0), vec2(0, 2)), (vec2(0, 3), 2))

        valid, actual_distance, actual_point = result

        expected_point = vec2(0, 1)
        expected_distance = 1
        self.assertTrue(valid)
        self.assertTrue(expected_point.almost_equal(actual_point))
        self.assertEqual(actual_distance, expected_distance)

    def test_ray_intersect_not_intersected(self):
        result = geometry.ray_circle_intersect(
            (vec2(0, 0), vec2(2, 2)), (vec2(4, 10), 2))

        valid, actual_distance, actual_point = result

        expected_point = geometry.POINT_AT_INFINITY
        expected_distance = math.inf
        self.assertFalse(valid)
        self.assertEqual(actual_point, expected_point)
        self.assertEqual(actual_distance, expected_distance)

    def test_circles_intersect(self):
        first_circle = vec2(0, 1), 3
        second_circle = vec2(0, 4), 2

        self.assertTrue(geometry.circles_intersect(
            first_circle, second_circle))

    def test_circles_intersect_no_intersection(self):
        first_circle = vec2(5, 5), 3
        second_circle = vec2(-1, 4), 2

        self.assertFalse(geometry.circles_intersect(
            first_circle, second_circle))

    def test_line_line_intersect(self):
        expected_intersection = vec2(0, 0)
        first_line = vec2(-1, 0), vec2(1, 0)
        second_line = vec2(0, -1), vec2(0, 1)

        are_intersected, intersection = geometry.line_line_intersect(
            first_line, second_line)
        self.assertTrue(are_intersected)
        self.assertTrue(expected_intersection.almost_equal(intersection))

    def test_line_line_intersect_no_intersection(self):
        expected_intersection = geometry.POINT_AT_INFINITY
        first_line = vec2(-10, -12), vec2(0, -5)
        second_line = vec2(15, 2), vec2(4, 3)

        are_intersected, intersection = geometry.line_line_intersect(
            first_line, second_line)
        self.assertFalse(are_intersected)
        self.assertEqual(intersection, expected_intersection)


if __name__ == '__main__':
    unittest.main()
