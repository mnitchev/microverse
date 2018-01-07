import math
from .vec2 import vec2


# Here we assume the ray is bounded by its end.
def ray_circle_intersect(ray, circle):
    position, direction = ray
    start, end = position, position.copy.add(direction)

    valid, intersections = line_circle_intersect((start, end), circle)
    p1, p2 = intersections

    p1_distance = position.distance(p1)
    p2_distance = position.distance(p2)

    if p1_distance < p2_distance:
        return valid, p1_distance, p1

    return valid, p2_distance, p2


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

    dr = direction.length
    det = center.x * end.y - end.x * center.y
    disc = radius * radius * dr * dr - det * det

    if disc >= 0:
        disc_root = math.sqrt(disc)

        dy_sign = math.copysign(1, dy)

        x1 = (det * dy + dy_sign * dx * disc_root) / (dr * dr)
        x2 = (det * dy - dy_sign * dx * disc_root) / (dr * dr)

        y1 = (-det * dx + math.fabs(dy) * disc_root) / (dr * dr)
        y2 = (-det * dx - math.fabs(dy) * disc_root) / (dr * dr)

        p1 = vec2(x1, y1)
        p2 = vec2(x2, y2)

        intersections = p1, p2

        return True, intersections
    return False, (vec2(), vec2())
