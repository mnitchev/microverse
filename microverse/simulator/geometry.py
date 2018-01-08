import math
from .vec2 import vec2, POINT_AT_INFINITY


def if_circle_circle_intersect(first, second):
    first_center, first_radius = first
    second_center, second_radius = second
    centers_distance = first_center.distance(second_center)

    return centers_distance < first_radius + second_radius


# Here we assume the ray is bounded by its end.
def ray_circle_intersect(ray, circle):
    position, direction = ray
    start, end = position.copy, position.copy.add(direction)

    valid, intersections = line_circle_intersect((start, end), circle)
    if not valid:
        return valid, math.inf, POINT_AT_INFINITY

    first, second = intersections

    first_distance = position.distance(first)
    second_distance = position.distance(second)

    if first_distance < second_distance:
        return valid, first_distance, first

    return valid, second_distance, second


def line_circle_intersect(line, circle):
    """Resource used for the implementation:
    http://mathworld.wolfram.com/Circle-LineIntersection.html
    """
    center, radius = circle
    start, end = line

    start.subtract(center)
    end.subtract(center)

    direction = end.subtract(start)
    dx = direction.x
    dy = direction.y

    line_length = direction.length
    det = start.x * end.y - end.x * start.y
    disc = radius * radius * line_length * line_length - det * det

    if disc >= 0:
        disc_root = math.sqrt(disc)

        dy_sign = math.copysign(1, dy)

        x1 = (det * dy + dy_sign * dx * disc_root) / \
            (line_length * line_length)
        x2 = (det * dy - dy_sign * dx * disc_root) / \
            (line_length * line_length)

        y1 = (-det * dx + math.fabs(dy) * disc_root) / \
            (line_length * line_length)
        y2 = (-det * dx - math.fabs(dy) * disc_root) / \
            (line_length * line_length)

        first = vec2(x1, y1)
        second = vec2(x2, y2)

        first.add(center)
        second.add(center)

        intersections = first, second

        return True, intersections
    return False, (vec2(), vec2())
