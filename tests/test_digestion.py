import math
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from microverse.simulator import Digestion
from microverse.simulator import Food
from microverse.simulator import vec2


class TestDigestion(unittest.TestCase):
    @patch('microverse.simulator.geometry.circles_intersect',
           return_value=MagicMock())
    def test_digestion(self, circle_intersect_mock):
        elements = [Food(vec2(1, 2), 1), ]
        digestion = Digestion(elements)
        circle_intersect_mock().return_value = True
