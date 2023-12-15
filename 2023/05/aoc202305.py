"""Advent of code day 5."""


class Part1Solver:
    """Part 1 solver."""

    def __init__(self, input_text: str) -> None:
        """Create a part 1 solver."""
        seeds_text, *rest_text = input_text.split("\n\n")
        self.seeds = [int(x) for x in seeds_text.split()[1:]]

        self.mapping: dict[tuple[str, str], list[dict[str, int]]] = {}

        for block in rest_text:
            title, *number_lines = block.splitlines()
            from_location, to_location = title.split()[0].split("-to-")

            self.mapping[(from_location, to_location)] = []

            for number_line in number_lines:
                dest_range, source_range, range_len = number_line.split()
                self.mapping[(from_location, to_location)].append(
                    {
                        "src": int(source_range),
                        "src_end": int(source_range) + int(range_len),
                        "diff": int(dest_range) - int(source_range),
                    }
                )

    def __repr__(self) -> str:
        """Return a string representation."""
        seeds_str = " ".join(map(str, self.seeds))

        mapping_str = ""
        for key, val in self.mapping.items():
            mapping_str += f"\n\n{key[0]}-to-{key[1]} map:\n"
            mapping_str += "\n".join(str(line) for line in val)

        return f"seeds: {seeds_str}{mapping_str}"

    def solve(self) -> int:
        """Solve part 1."""
        locations = []
        for seed in self.seeds:
            for ranges in self.mapping.values():
                for number_range in ranges:
                    if number_range["src"] <= seed < number_range["src_end"]:
                        seed += number_range["diff"]
                        break
            locations.append(seed)

        return min(locations)


class Part2Solver:
    """Part 2 solver."""

    def __init__(self, input_text: str) -> None:
        """Create a part 2 solver."""
        seeds_text, *rest_text = input_text.split("\n\n")
        seed_nums = [int(x) for x in seeds_text.split()[1:]]
        self.seeds = (
            num
            for left, right in zip(seed_nums[::2], seed_nums[1::2])
            for num in range(left, left + right)
        )

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

    def __repr__(self) -> str:
        """Return a string representation."""
        seeds_str = " ".join(map(str, self.seeds))

        mapping_str = ""
        for key, val in self.mapping.items():
            mapping_str += f"\n\n{key[0]}-to-{key[1]} map:\n"
            mapping_str += "\n".join(str(line) for line in val)

        return f"seeds: {seeds_str}{mapping_str}"

    def solve(self) -> int:
        """Solve part 1."""
        locations = []
        for seed in self.seeds:
            for ranges in self.mapping.values():
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


def main() -> None:
    """Program starts here."""
    with open("2023/05/test.txt", encoding="utf-8") as file:
        file_text = file.read()

    part_1_solver = Part1Solver(file_text)
    part_2_solver = Part2Solver(file_text)

    print("Part 1:", part_1(part_1_solver))
    print("Part 2:", part_2(part_2_solver))


def part_1(solver: Part1Solver) -> int:
    """Solve part 1."""
    return solver.solve()


def part_2(solver: Part2Solver) -> int:
    """Solve part 2."""
    return solver.solve()


if __name__ == "__main__":
    main()
