"""Advent of code Day 3 part 2"""

from itertools import combinations, permutations


def main():
    """Main function"""
    with open("2016/03/input.txt", encoding="utf-8") as file:
        file_content = [
            tuple(int(x) for x in line.split()) for line in file.read().split("\n")
        ]

    triangles = []
    for i in range(0, len(file_content), 3):
        for j in range(3):
            triangle = (
                file_content[i][j],
                file_content[i + 1][j],
                file_content[i + 2][j],
            )
            triangles.append(triangle)

    valid_triangles = []
    invalid_triangles = []

    for triangle in triangles:
        checks = []
        combos = (
            x
            for x in permutations(triangle, 3)
            if (x[0], x[1]) in combinations(triangle, 2)
        )

        for combo in combos:
            checks.append(sum(combo[0:2]) > combo[-1])

        if all(checks):
            valid_triangles.append(triangle)
        else:
            invalid_triangles.append(triangle)

    print(len(valid_triangles))


if __name__ == "__main__":
    main()
