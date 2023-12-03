"""Advent of code Day 15."""

import re


def main():
    """Main function."""
    regex = r"Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)"

    with open("2022/15/input.txt", encoding="utf-8") as file:
        coords = [map(int, nums) for nums in re.findall(regex, file.read())]
        coords = {(x1, y1): (x2, y2) for x1, y1, x2, y2 in coords}

    print("Part 1:", part_1(coords, 2_000_000))
    print("Part 2:", part_2(coords))


def part_1(coords: dict[tuple[int, int], tuple[int, int]], y_to_check: int) -> int:
    """Solve part 1."""
    beacon_no_go_zone = set()

    for sensor, beacon in coords.items():
        distance = manhattan_distance(sensor, beacon)
        sensor_x, _ = sensor
        for x in range(-distance + sensor_x, distance + sensor_x + 1):
            pos = (x, y_to_check)
            if manhattan_distance(pos, sensor) <= distance:
                beacon_no_go_zone.add(pos[0])

    return len(beacon_no_go_zone) - 1


def manhattan_distance(start: tuple[int, int], end: tuple[int, int]) -> int:
    """Calculate the manhattan distance between two points."""
    return abs(end[0] - start[0]) + abs(end[1] - start[1])


def part_2(coords: dict[tuple[int, int], tuple[int, int]]) -> int | None:
    """Solve part 2."""
    distances = {
        sensor: manhattan_distance(sensor, beacon) for sensor, beacon in coords.items()
    }
    upper_lim = 4_000_000

    for sensor in coords:
        outside_edges = set()

        sensor_x, sensor_y = sensor
        distance = distances[sensor] + 1
        edge_pos = (sensor_x, sensor_y + distance)
        if all(0 <= axis <= upper_lim for axis in edge_pos):
            outside_edges.add(edge_pos)
        directions = [(+1, -1), (-1, -1), (-1, +1), (+1, +1)]
        corners = {
            (sensor_x, sensor_y + distance),
            (sensor_x, sensor_y - distance),
            (sensor_x + distance, sensor_y),
            (sensor_x - distance, sensor_y),
        }

        for direction in directions:
            while True:
                edge_pos = (edge_pos[0] + direction[0], edge_pos[1] + direction[1])
                if all(0 <= axis <= upper_lim for axis in edge_pos):
                    outside_edges.add(edge_pos)
                if edge_pos in corners:
                    break

        for point_on_edge in outside_edges:
            if all(
                manhattan_distance(sensor, point_on_edge) > distances[sensor]
                for sensor in coords
            ):
                return point_on_edge[0] * upper_lim + point_on_edge[1]

    return None


if __name__ == "__main__":
    main()
