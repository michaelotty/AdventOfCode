"""Advent of code day 15."""


def main() -> None:
    """Program starts here."""
    with open("2023/15/input.txt", encoding="utf-8") as file:
        data = file.read().split(",")

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


def part_1(data: list[str]) -> int:
    """Solve part 1."""
    return sum(hash_algorithm(item) for item in data)


def hash_algorithm(string: str) -> int:
    """Return the HASH of a string."""
    output = 0
    for char in string:
        output += ord(char)
        output *= 17
        output %= 256

    return output


def part_2(data: list[str]) -> int:
    """Solve part 2."""
    database: dict[int, dict[str, int]] = {}

    for line in data:
        if "=" in line:
            left, right, *_ = line.split("=")
            box_num = hash_algorithm(left)
            focal_length = int(right)
            database.setdefault(box_num, {})[left] = focal_length
        elif "-" in line:
            label = line.replace("-", "")
            for val in database.values():
                if label in val:
                    del val[label]

            database = {key: val for key, val in database.items() if val}

        else:
            raise RuntimeError("Invalid line")

    return get_focussing_power(database)


def get_focussing_power(database: dict[int, dict[str, int]]) -> int:
    """Get the focussing power."""
    focussing_power = 0
    for box_id, lenses in database.items():
        for slot, lens in enumerate(lenses.values(), start=1):
            lens_power = (box_id + 1) * slot * lens
            focussing_power += lens_power

    return focussing_power


if __name__ == "__main__":
    main()
