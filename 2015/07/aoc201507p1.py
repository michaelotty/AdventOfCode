"""Advent of code Day 7 part 1."""


def main() -> None:
    """Program starts here."""
    with open("2015/07/input.txt", encoding="utf-8") as f:
        file_contents = f.read().split("\n")

    parser = Parser(file_contents)
    print(parser.parse_instruction("a"))


class Parser:  # pylint: disable=too-few-public-methods
    """Parses the input of the file."""

    def __init__(self, file_contents) -> None:
        """Create a Parser."""
        self.calc = {}
        self.results: dict[str, int] = {}

        for line in file_contents:
            option, result = line.split("->")
            self.calc[result.strip()] = option.strip().split(" ")

    def parse_instruction(self, var_name: str) -> int:
        """Recursive function."""
        try:
            return int(var_name)
        except ValueError:
            pass

        if var_name not in self.results:
            ops = self.calc[var_name]
            if len(ops) == 1:
                self.results[var_name] = self.parse_instruction(ops[0])
            elif ops[0] == "NOT":
                self.results[var_name] = (~self.parse_instruction(ops[1])) & 0xFFFF
            elif ops[1] == "AND":
                self.results[var_name] = self.parse_instruction(
                    ops[0]
                ) & self.parse_instruction(ops[2])
            elif ops[1] == "OR":
                self.results[var_name] = self.parse_instruction(
                    ops[0]
                ) | self.parse_instruction(ops[2])
            elif ops[1] == "->":
                self.results[var_name] = self.parse_instruction(ops[0])
            elif ops[1] == "LSHIFT":
                self.results[var_name] = self.parse_instruction(
                    ops[0]
                ) << self.parse_instruction(ops[2])
            elif ops[1] == "RSHIFT":
                self.results[var_name] = self.parse_instruction(
                    ops[0]
                ) >> self.parse_instruction(ops[2])
            else:
                raise RuntimeError(f'Invalid line: "{" ".join(var_name)}"')

        return self.results[var_name]


if __name__ == "__main__":
    main()
