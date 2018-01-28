import math
from .vec2 import vec2, POINT_AT_INFINITY


def circles_intersect(first, second):
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
        denominator = line_length * line_length

        if denominator != 0:
            x1 = (det * dy + dy_sign * dx * disc_root) / denominator
            x2 = (det * dy - dy_sign * dx * disc_root) / denominator

            y1 = (-det * dx + math.fabs(dy) * disc_root) / denominator
            y2 = (-det * dx - math.fabs(dy) * disc_root) / denominator

            first = vec2(x1, y1)
            second = vec2(x2, y2)

            first.add(center)
            second.add(center)

            intersections = first, second

            return True, intersections

    return False, POINT_AT_INFINITY


def line_line_intersect(first, second):
    point1, point2 = first
    point3, point4 = second

    denominator = ((point1.x - point2.x) * (point3.y - point4.y) -
                   (point1.y - point2.y) * (point3.x - point4.x))

    if denominator == 0:
        return False, POINT_AT_INFINITY

    x_numerator = (((point1.x * point2.y) - (point1.y * point2.x)) *
                   (point3.x - point4.x) - (point1.x - point2.x) *
                   (point3.x * point4.y - point3.y * point4.x))

    y_numerator = (((point1.x * point2.y) - (point1.y * point2.x)) *
                   (point3.y - point4.y) - (point1.y - point2.y) *
                   (point3.x * point4.y - point3.y * point4.x))

    intersect_x = x_numerator / denominator
    intersect_y = y_numerator / denominator
    intersection = vec2(intersect_x, intersect_y)

    first_min_x, first_max_x = __get_min_and_max(point1.x, point2.x)
    first_min_y, first_max_y = __get_min_and_max(point1.y, point2.y)

    second_min_x, second_max_x = __get_min_and_max(point3.x, point4.x)
    second_min_y, second_max_y = __get_min_and_max(point3.y, point4.y)
    
    if first_min_x <= intersection.x <= first_max_x and \
        second_min_x <= intersection.x <= second_max_x and \
        first_min_y <= intersection.y <= first_max_y and \
         second_min_y <= intersection.y <= second_max_y:
        return True, intersection

    return False, POINT_AT_INFINITY


def __get_min_and_max(first, second):
    return min(first, second), max(first, second)
