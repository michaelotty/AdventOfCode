"""Advent of code Day 3 part 1 and 2"""


def find_visited_locations(wire: tuple[str]) -> set[tuple[int, int]]:
    """Create set of visited locations"""
    position = (0, 0)
    visited_locations = set()

    for branch in wire:
        direction, *amount = branch
        amount = int(''.join(amount))
        for _ in range(amount):
            position = move_position(position, direction)
            visited_locations.add(position)

    return visited_locations


def find_intersections(wires: tuple[tuple[str]]) -> set[tuple[int, int]]:
    """Find all coords of all intersections of the wires"""
    wire_visits = [find_visited_locations(wire) for wire in wires]
    return wire_visits[0] & wire_visits[1]


def move_position(position: tuple[int, int], direction: str) -> tuple[int, int]:
    """Return a new position, one step in the direction"""
    if direction == 'U':
        return position[0], position[1] + 1
    if direction == 'R':
        return position[0] + 1, position[1]
    if direction == 'D':
        return position[0], position[1] - 1
    if direction == 'L':
        return position[0] - 1, position[1]

    raise ValueError(f'Unknown direction: {direction}')


def distance_to_closest_intersection(intersections: set[tuple[int, int]]) -> int:
    """Find the closest intersection"""
    intersections = list(intersections)
    intersection_distances = (manhattan_distance(
        intersection) for intersection in intersections)
    distance = min(intersection_distances)
    return distance


def manhattan_distance(coordinate: tuple[int, int]) -> int:
    """Calculates the manhattan distance to a coordinate"""
    return sum(abs(dimension) for dimension in coordinate)


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        wires = tuple(tuple(i.split(',')) for i in file.read().split())

    intersections = find_intersections(wires)
    print(f'Part 1: {distance_to_closest_intersection(intersections)}')


if __name__ == "__main__":
    main()
