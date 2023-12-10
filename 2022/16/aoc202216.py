"""Advent of code Day 16."""

# import functools
import itertools
import re
from typing import Any


def main() -> None:
    """Program starts here."""
    with open("2022/16/test1.txt", encoding="utf-8") as file:
        regex = r"Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? (.*)"
        lines = [re.findall(regex, line)[0] for line in file.readlines()]
        valves = {
            key: {"rate": int(rate), "tunnels": tunnels.split(", ")}
            for key, rate, tunnels in lines
        }

    print("Part 1:", part_1(valves))
    print("Part 2:", part_2(valves))


def part_1(valves: dict[str, Any]) -> int:
    """Solve part 1."""
    # Find all the valves with a flow rate and shortest paths
    valves_with_flow_rate = {
        key: val["rate"] for key, val in valves.items() if val["rate"]
    }
    valves_with_flow_rate["AA"] = valves["AA"]["rate"]
    routes = {}
    keys = list(itertools.product(valves_with_flow_rate, repeat=2))
    for key in keys:
        routes[key] = find_route(key[0], key[1], valves)

    # Some dynamic programming algorithm to find solution
    return find_max_pressure(30, "AA", valves_with_flow_rate)


# @functools.cache
def find_max_pressure(time_left, current_position, valves):
    """Find the maximum pressure that can be released."""
    frontier = [current_position]

    while frontier:
        current_position = frontier.pop(0)
        if time_left == 0:
            break

        neighbors = valves - current_position
        for neighbor in neighbors:
            frontier.append(neighbor)


def find_route(start, end, valves):
    """Find the shortest route from start to end."""
    current = start
    frontier = [start]
    came_from = {start: None}

    while frontier:
        current = frontier.pop(0)
        if current == end:
            break

        neighbors = valves[current]["tunnels"]
        for neighbor in neighbors:
            if neighbor not in came_from:
                frontier.append(neighbor)
                came_from[neighbor] = current

    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path


def part_2(valves: dict[str, Any]) -> dict[str, Any]:
    """Solve part 2."""
    return valves


if __name__ == "__main__":
    main()
