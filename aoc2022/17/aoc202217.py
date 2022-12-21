"""Advent of code Day 17."""

import itertools


def main():
    """Main function."""
    print("Part 1:", part_1())
    print("Part 2:", part_2())


def part_1():
    """Solve part 1."""
    # gen = shape_generator()
    # for _ in range(10):
    #     print(next(gen))
    #     print()

    columns = [["."] * 4] * 7
    columns[3][1] = "#"
    print_grid(columns)
    return 0


def part_2():
    """Solve part 2."""
    return 0


def direction_generator():
    """Generate the infinite looping directions from the file."""
    with open("aoc2022/17/test1.txt", encoding="utf-8") as file:
        directions = file.read()

    for char in itertools.cycle(directions):
        yield char


def shape_generator():
    """Generate the shape to use infinitely."""
    minus_shape = "....\n....\n....\n####"
    plus_shape = "....\n....\n.#..\n###.\n.#.."
    l_shape = "....\n..#.\n..#.\n###."
    i_shape = "#...\n#...\n#...\n#..."
    box_shape = "....\n....\n##..\n##.."
    shapes = [minus_shape, plus_shape, l_shape, i_shape, box_shape]

    for shape in itertools.cycle(shapes):
        yield shape


def print_grid(grid):
    """Print the grid representation."""
    grid = zip(*grid)
    print("\n".join("".join(line) for line in grid))


if __name__ == "__main__":
    main()
