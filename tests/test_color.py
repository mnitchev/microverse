import unittest
from microverse.simulator.color import color


class TestColor(unittest.TestCase):

    def test_to_hex(self):
        expected_hex_color = "#a70a0c"
        color_obj = color(167, 10, 12)
        actual_hex_color = color_obj.to_hex()

        self.assertEqual(actual_hex_color, expected_hex_color)
