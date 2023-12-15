"""Advent of code day 10."""


class PipeMaze:
    """Pipe maze."""

    def __init__(self, input_text: str) -> None:
        """Create a pipe maze."""
        self.text = input_text

    def __repr__(self) -> str:
        """Return a string representation."""
        translation_table = str.maketrans(
            {
                "|": "│",
                "-": "─",
                "L": "╰",
                "J": "╯",
                "7": "╮",
                "F": "╭",
                ".": " ",
                "S": "▒",
            }
        )
        return self.text.translate(translation_table)


def main() -> None:
    """Program starts here."""
    with open("2023/10/input.txt", encoding="utf-8") as file:
        maze = PipeMaze(file.read())

    print(maze)

    print("Part 1:", part_1())
    print("Part 2:", part_2())


def part_1() -> int:
    """Solve part 1."""
    return 0


def part_2() -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
