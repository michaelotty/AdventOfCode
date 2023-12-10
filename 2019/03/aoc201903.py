"""Advent of code Day 3 part 1 and 2."""

from typing import Callable


def find_visited_locations(wire: tuple[str, ...]) -> tuple[set[tuple[int, int]], dict]:
    """Create set of visited locations."""
    position = (0, 0)
    visited_locations = set()
    step_record = {}
    step = 1

    for branch in wire:
        direction, *rest = list(branch)
        amount = int("".join(rest))
        for _ in range(amount):
            position = move_position(position, direction)
            visited_locations.add(position)
            step_record[step] = position
            step += 1

    return visited_locations, step_record


def find_intersections(
    wires: tuple[tuple[str, ...], ...],
) -> tuple[set[tuple[int, int]], tuple[dict, dict]]:
    """Find all coords of all intersections of the wires."""
    wire_visits = [find_visited_locations(wire) for wire in wires]
    return (
        wire_visits[0][0] & wire_visits[1][0],
        (wire_visits[0][1], wire_visits[1][1]),
    )


def move_position(position: tuple[int, int], direction: str) -> tuple[int, int]:
    """Return a new position, one step in the direction."""
    if direction == "U":
        return position[0], position[1] + 1
    if direction == "R":
        return position[0] + 1, position[1]
    if direction == "D":
        return position[0], position[1] - 1
    if direction == "L":
        return position[0] - 1, position[1]

    raise ValueError(f"Unknown direction: {direction}")


def distance_to_closest_intersection(
    intersections: set[tuple[int, int]],
    method: str,
    step_records: tuple[dict, dict] | None = None,
) -> int:
    """Find the closest intersection."""
    distance_funcs: dict[str, Callable] = {
        "manhattan": manhattan_distance,
        "path": path_distance,
    }
    try:
        distance_func = distance_funcs[method]
    except KeyError:
        raise ValueError(
            f"Method not defined: '{method}'.\nChoose one of {distance_funcs.keys()}"
        ) from KeyError

    if distance_func is path_distance and step_records is None:
        raise ValueError(f"step_records must be defined if method={method}")

    intersections_list = list(intersections)
    intersection_distances = (
        distance_func(intersection, step_records) for intersection in intersections_list
    )
    return min(intersection_distances)


def manhattan_distance(coordinate: tuple[int, int], *_) -> int:
    """Calculate the manhattan distance to a coordinate."""
    return sum(abs(dimension) for dimension in coordinate)


def path_distance(coordinate: tuple[int, int], step_records: tuple[dict, dict]) -> int:
    """Calculate the path distance to a coordinate."""
    return sum(
        step_count
        for step_record in step_records
        for step_count, coord in step_record.items()
        if coord == coordinate
    )


def main() -> None:
    """Program starts here."""
    with open("2019/03/input.txt", encoding="utf-8") as file:
        wires = tuple(tuple(i.split(",")) for i in file.read().split())

    intersections, step_records = find_intersections(wires)
    part_1 = distance_to_closest_intersection(intersections, "manhattan")
    part_2 = distance_to_closest_intersection(
        intersections, "path", step_records=step_records
    )
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
