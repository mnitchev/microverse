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

    def test_ray_intersect(self):
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


if __name__ == '__main__':
    unittest.main()
