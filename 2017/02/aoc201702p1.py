"""Advent of code Day 2 part 1."""


def main() -> None:
    """Program starts here."""
    with open("2017/02/input.txt", encoding="utf-8") as file:
        rows = tuple(
            tuple(int(element) for element in row.split()) for row in file.readlines()
        )
    print(sum(max(row) - min(row) for row in rows))


if __name__ == "__main__":
    main()
