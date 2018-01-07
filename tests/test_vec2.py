import unittest
from microverse.simulator import vec2


class TestVec2(unittest.TestCase):
    def test_copy(self):
        vector = vec2(2, 3)
        copy = vector.copy

        self.__assert_vectors_equal(copy, vector)

    def test_reverse(self):
        vector = vec2(5, 4)
        reversed_vector = vector.reverse

        expected_vector = vec2(-vector.x, -vector.y)
        self.__assert_vectors_equal(reversed_vector, expected_vector)

    def test_length(self):
        vector = vec2(3, 4)

        self.assertEqual(vector.length, 5)

    def test_add(self):
        first = vec2(1, 2)
        second = vec2(3, 4)
        actual_result = first.copy.add(second)

        expected_vector = vec2(first.x + second.x,
                               first.y + second.y)
        self.__assert_vectors_equal(actual_result, expected_vector)

    def test_subtract(self):
        first = vec2(5, 3)
        second = vec2(7, 1)
        actual_result = first.copy.subtract(second)

        expected_vector = vec2(first.x - second.x,
                               first.y - second.y)
        self.__assert_vectors_equal(actual_result, expected_vector)

    def test_direction(self):
        first = vec2(5, 3)
        second = vec2(7, 1)
        actual_distance = first.direction(second)
        expected_distance = first.copy.subtract(second).length

        self.assertEqual(actual_distance, expected_distance)

    def test_rotate(self):
        vector = vec2(3, 4)
        actual_vector = vector.copy.rotate(0.785398)

        expected_vector = vec2(-0.7071, 4.9497)
        self.__assert_vectors_equal(actual_vector, expected_vector)

    def __assert_vectors_equal(self, actual, expected):
        self.assertAlmostEqual(actual.x, expected.x, places=4)
        self.assertAlmostEqual(actual.y, expected.y, places=4)


if __name__ == '__main__':
    unittest.main()
