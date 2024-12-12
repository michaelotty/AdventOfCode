"""Advent of code day 5."""


def main() -> None:
    """Program starts here."""
    with open("2024/05/input.txt", encoding="utf-8") as file:
        top_str, bottom_str = file.read().split("\n\n")
    rules = [tuple(map(int, x.split("|"))) for x in top_str.splitlines()]
    pages = [tuple(map(int, x.split(","))) for x in bottom_str.splitlines()]

    print("Part 1:", part_1(rules, pages))
    print("Part 2:", part_2())


def part_1(rules: list, pages) -> int:
    """Solve part 1."""
    rules.sort()
    count = 0

    for page_listing in pages:
        passed = True
        for i, page in enumerate(page_listing[1:], start=1):
            if not passed:
                break

            for first, second in rules:
                if page != first:
                    break
                if second in page_listing[: i - 1]:
                    passed = False
                    break
        if passed:
            x = page_listing[(len(page_listing) - 1) // 2]
            print(x)
            count += x

    return count  # 10478 too high


def part_2() -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
