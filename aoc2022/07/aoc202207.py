"""Advent of code Day 7."""

import re


def main():
    """Main function."""
    with open("aoc2022/07/test.txt", encoding="utf-8") as file:
        text = file.read().splitlines()
    tree = build_tree(text)
    print("Part 1:", part_1(tree))
    print("Part 2:", part_2(tree))


def build_tree(text):
    """Build the tree."""
    cd = ""
    fs = {}
    for line in text:
        first, second, *third = line.split()
        if first == "$":
            if second == "cd":
                if third[0] == "..":
                    left = re.findall(r"(.*)\/\w+", cd)[0]
                    cd = left
                elif third[0] == "/":
                    cd += ""
                else:
                    cd += "/" + third[0]

            if second == "ls":
                pass

        elif first == "dir":
            pass
        else:
            fs[cd + "/" + second] = int(first)

    return fs


def part_1(tree):
    """Solve part 1."""


def part_2(tree):
    """Solve part 2."""
    return 0


"""
- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
"""

# {"/": {"a": {}, "b.txt": 14848514, "c.dat": 8504156, "d": {}}}


if __name__ == "__main__":
    main()
