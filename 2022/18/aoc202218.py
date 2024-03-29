"""Advent of code Day 18."""

import collections
import itertools


def main() -> None:
    """Program starts here."""
    with open("2022/18/input.txt", encoding="utf-8") as file:
        voxels = {tuple(map(int, line.split(","))) for line in file.read().splitlines()}
    print_lava_drop(voxels)
    print("Part 1:", part_1(voxels))
    print("Part 2:", part_2(voxels))


def part_1(voxels: set[tuple[int, ...]]) -> int:
    """Solve part 1."""
    faces = []
    for x, y, z in voxels:
        new_faces = [
            ("x", x, y, z),
            ("x", x + 1, y, z),
            ("y", x, y, z),
            ("y", x, y + 1, z),
            ("z", x, y, z),
            ("z", x, y, z + 1),
        ]
        faces += new_faces
    faces_counted = collections.Counter(faces).most_common()
    uncovered_faces = [face for face, count in faces_counted if count == 1]
    return len(uncovered_faces)


def part_2(lava_drop: set[tuple[int, ...]]) -> int:
    """Solve part 2."""
    mins = {}
    maxs = {}

    mins["x"] = min(x for x, y, z in lava_drop) - 1
    maxs["x"] = max(x for x, y, z in lava_drop) + 1

    mins["y"] = min(y for x, y, z in lava_drop) - 1
    maxs["y"] = max(y for x, y, z in lava_drop) + 1

    mins["z"] = min(z for x, y, z in lava_drop) - 1
    maxs["z"] = max(z for x, y, z in lava_drop) + 1

    locations_to_search: set[tuple[int, ...]] = set(
        itertools.product(
            range(mins["x"], maxs["x"] + 1),
            range(mins["y"], maxs["y"] + 1),
            range(mins["z"], maxs["z"] + 1),
        )
    )

    start = (mins["x"], mins["y"], mins["z"])
    frontier = []
    open_air = set()
    air = locations_to_search - lava_drop

    frontier.append(start)
    open_air.add(start)

    while frontier:
        check_location = frontier.pop(0)

        if check_location in lava_drop:
            continue

        adjacents_air = get_adjacents(check_location) & locations_to_search

        for adjacent in adjacents_air:
            if adjacent not in open_air:
                frontier.append(adjacent)

        open_air.update(adjacents_air)

    trapped_air = air - open_air

    # Treat trapped air air as normal filled in voxel
    lava_drop.update(trapped_air)
    return part_1(lava_drop)


def get_adjacents(voxel: tuple[int, ...]) -> set[tuple[int, int, int]]:
    """Get the adjacent voxels."""
    x, y, z = voxel
    return {
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    }


def print_lava_drop(voxels: set[tuple[int, ...]]) -> None:
    """Print out layer by layer representation of 3D lava drop."""
    min_x, max_x = min(x for x, y, z in voxels), max(x for x, y, z in voxels)
    min_y, max_y = min(y for x, y, z in voxels), max(y for x, y, z in voxels)
    min_z, max_z = min(z for x, y, z in voxels), max(z for x, y, z in voxels)

    print(
        "\n--------------------\n".join(
            "\n".join(
                "".join(
                    "#" if (x, y, z) in voxels else " " for z in range(min_z, max_z + 1)
                )
                for y in range(min_y, max_y + 1)
            )
            for x in range(min_x, max_x + 1)
        )
    )


if __name__ == "__main__":
    main()
