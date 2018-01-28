import math


def vec2(x=0, y=0):
    return Vec2(x, y)


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def copy(self):
        return Vec2(self.x, self.y)

    @property
    def reverse(self):
        return Vec2(-self.x, -self.y)

    @property
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

        return self

    def subtract(self, vec):
        return self.add(vec.reverse)

    def distance(self, vec):
        return self.copy.subtract(vec).length

    def rotate(self, angle):
        old_x = self.x

        self.x = self.x * math.cos(angle) - self.y * math.sin(angle)
        self.y = self.y * math.cos(angle) + old_x * math.sin(angle)

        return self

    def scale(self, n):
        self.x *= n
        self.y *= n

        return self

    def scale_to(self, n):
        vac_length = self.length
        if vac_length != 0:
            n /= vac_length

        return self.scale(n)

    def __eq__(self, other):
        return self.x == other.x and \
            self.y == other.y

    def almost_equal(self, other, epsilon=0.0001):
        return math.fabs(self.x - other.x) < epsilon and \
            math.fabs(self.y - other.y) < epsilon


POINT_AT_INFINITY = Vec2(math.inf, math.inf)
