"""Advent of code day 5."""


class Day5Solver:
    """Day 5 solver."""

    def __init__(self, input_text: str) -> None:
        """Create a day 5 solver."""
        seeds_text, *rest_text = input_text.split("\n\n")
        self._seeds = [int(x) for x in seeds_text.split()[1:]]

        self.mapping: dict[tuple[str, str], list[dict[str, int]]] = {}

        for block in rest_text:
            title, *number_lines = block.splitlines()
            from_location, to_location = title.split()[0].split("-to-")

            self.mapping[(from_location, to_location)] = []

            for number_line in number_lines:
                dest_range, source_range, range_len = number_line.split()
                self.mapping[(from_location, to_location)].append(
                    {
                        "dst": int(dest_range),
                        "src": int(source_range),
                        "diff": int(dest_range) - int(source_range),
                        "len": int(range_len),
                    }
                )

    @property
    def seeds(self):
        """Property of seed IDs."""
        return self._seeds.copy()

    def __repr__(self) -> str:
        """Return a string representation."""
        seeds_str = " ".join(map(str, self._seeds))

        mapping_str = ""
        for key, val in self.mapping.items():
            mapping_str += f"\n\n{key[0]}-to-{key[1]} map:\n"
            mapping_str += "\n".join(str(line) for line in val)

        return f"seeds: {seeds_str}{mapping_str}"


def main() -> None:
    """Program starts here."""
    with open("2023/05/input.txt", encoding="utf-8") as file:
        file_text = file.read()

    solver = Day5Solver(file_text)

    print("Part 1:", part_1(solver))
    print("Part 2:", part_2())


def part_1(solver: Day5Solver) -> int:
    """Solve part 1."""
    locations = []
    for seed in solver.seeds:
        for ranges in solver.mapping.values():
            for number_range in ranges:
                if (
                    number_range["src"]
                    <= seed
                    < number_range["src"] + number_range["len"]
                ):
                    seed += number_range["diff"]
                    break
        locations.append(seed)

    return min(locations)


def part_2() -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
