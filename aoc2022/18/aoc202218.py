"""Advent of code Day 18."""

from collections import Counter


def main():
    """Main function."""
    with open("aoc2022/18/input.txt", encoding="utf-8") as file:
        voxels = {tuple(map(int, line.split(","))) for line in file.read().splitlines()}
    print("Part 1:", part_1(voxels))
    print("Part 2:", part_2(voxels))


def part_1(voxels):
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
    faces = Counter(faces)
    uncovered_faces = [face for face, count in faces.most_common() if count == 1]
    return len(uncovered_faces)


def part_2(voxels):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
