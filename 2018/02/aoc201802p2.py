"""Advent of code Day 2 part 2."""


def calculate_solution(lines: list[str]) -> str:
    """Calculate the solution."""
    for i, _ in enumerate(lines[0]):
        if len(set(line[:i] + line[i + 1 :] for line in lines)) < len(lines):
            checked = set()
            for line in lines:
                new_line = line[:i] + line[i + 1 :]
                if new_line in checked:
                    return new_line
                checked.add(new_line)

    raise ValueError("Answer not found")


def main() -> None:
    """Program starts here."""
    with open("2018/02/input.txt", encoding="utf-8") as file:
        print(calculate_solution(file.read().split()))


if __name__ == "__main__":
    main()
