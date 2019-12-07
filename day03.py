from util import get_lines


def make_lines(path):
    lines = []
    previous_point = (0, 0)
    for segment in path:
        direction = segment[0]
        distance = int(segment[1:])
        if direction == 'U':
            point = (previous_point[0], previous_point[1] + distance)
        elif direction == 'D':
            point = (previous_point[0], previous_point[1] - distance)
        elif direction == 'L':
            point = (previous_point[0] - distance, previous_point[1])
        elif direction == 'R':
            point = (previous_point[0] + distance, previous_point[1])
        else:
            raise ValueError('{} is not a valid direction!'.format(direction))
        lines.append((previous_point, point))
        previous_point = point
    return lines


def intersect(line1, line2):
    # Source: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    try:
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    except ZeroDivisionError:
        return None
    if 0 <= t <= 1 and 0 <= u <= 1:
        # first conditional implies the intersection is on the first line segment
        # second conditional implies the intersection is on the second line segment
        # therefore, the line segments intersect
        return x1 + t * (x2 - x1), y1 + t * (y2 - y1)
    else:
        return None


def make_vec(p1, p2):
    # Make a vector from p1 pointing at p2
    return p2[0] - p1[0], p2[1] - p1[1]


def l1(point, other_point=None):
    # if other_point is None, assume point is a vector
    vec = point if other_point is None else make_vec(point, other_point)
    return sum(map(abs, vec))  # Manhatten distance


def minimum_manhatten_distace(wire1_lines, wire2_lines):
    min_distance = float('inf')

    for line_1 in wire1_lines:
        for line_2 in wire2_lines:
            intersection = intersect(line_1, line_2)
            if intersection is not None and intersection != (0.0, 0.0):
                min_distance = min(min_distance, l1(intersection))

    return min_distance


def minimum_wire_steps(wire1_lines, wire2_lines):
    min_wire_steps = float('inf')

    wire1_steps = 0
    for line1 in wire1_lines:
        wire2_steps = 0
        for line2 in wire2_lines:
            intersection = intersect(line1, line2)
            if intersection is not None and intersection != (0.0, 0.0):
                # the total steps of the wires plus the steps to the intersection
                wires_path_length = (wire1_steps + l1(line1[0], intersection) +
                                     wire2_steps + l1(line2[0], intersection))
                min_wire_steps = min(min_wire_steps, wires_path_length)
            wire2_steps += l1(line2[0], line2[1])  # Add up the steps as we go
        wire1_steps += l1(line1[0], line1[1])  # Add up the steps as we go

    return min_wire_steps


if __name__ == '__main__':
    # Part 1 examples
    assert minimum_manhatten_distace(make_lines('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')),
                                     make_lines('U62,R66,U55,R34,D71,R55,D58,R83'.split(','))) == 159
    assert minimum_manhatten_distace(make_lines('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')),
                                     make_lines('U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','))) == 135
    # Part 2 examples
    assert minimum_wire_steps(make_lines('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')),
                              make_lines('U62,R66,U55,R34,D71,R55,D58,R83'.split(','))) == 610
    assert minimum_wire_steps(make_lines('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')),
                              make_lines('U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','))) == 410
    formatted_input = [make_lines(line.split(',')) for line in get_lines('input/day03.txt')]

    print(minimum_manhatten_distace(*formatted_input))
    print(minimum_wire_steps(*formatted_input))
