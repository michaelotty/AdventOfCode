"""Advent of Code 2020 7 part 1"""

import re


class Bag:
    """Bag"""

    def __init__(self, data) -> None:
        self.data = data
        self.children: list = []

    def add_bags(self, bag, num):
        """Add multiple nodes"""
        for _ in range(num):
            self.children.append(bag)

    def __repr__(self):
        """Printable string"""
        return ", ".join(child.data for child in self.children)


class BagTree(Bag):
    """BagTree"""

    def __init__(self, root) -> None:
        self.root = root
        super().__init__(self.root.data)


def main():
    """Main function"""
    with open("question.txt", encoding="utf-8") as file:
        file_content = file.read()

    first_match = re.search(
        r"shiny gold bags contain ((?:(?:\d+ \w+ \w+ \w+)(?:, )*)+)\.", file_content
    )[1].split(", ")
    pop_list = zip(
        [int(i) for i in re.findall(r"\d+", "".join(first_match))],
        [re.search(r"\d+ (\w+ \w+)", i)[1] for i in first_match],
    )
    root = BagTree(Bag("shiny gold"))

    for amount, value in pop_list:
        root.add_bags(Bag(value), amount)

    print(root)


if __name__ == "__main__":
    main()
