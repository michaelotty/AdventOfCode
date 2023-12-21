"""Advent of code Day 7."""


def main() -> None:
    """Program starts here."""
    with open("2022/07/input.txt", encoding="utf-8") as file:
        text = file.read().splitlines()[1:]
    tree: dict = {}
    text, tree = build_tree(text, tree)
    print("Part 1:", part_1(tree))
    print("Part 2:", part_2(tree))


def build_tree(text: list[str], tree: dict) -> tuple[list[str], dict]:
    """Build the tree."""
    while text:
        line = text.pop(0)
        first, second, *third = line.split()

        if first == "$" and second == "cd":
            if third[0] == "..":
                return text, tree
            text, tree[third[0]] = build_tree(text, tree[third[0]])
        elif first == "$" and second == "ls":
            pass
        elif first == "dir":
            tree[second] = {}
        else:
            tree[second] = int(first)

    return text, tree


def part_1(tree: dict):
    """Solve part 1."""
    size = 0
    for val in tree.values():
        if isinstance(val, dict):
            dir_size = get_directory_size(val)
            if dir_size <= 100000:
                size += dir_size
            size += part_1(val)

    return size


def part_2(tree: dict) -> int:
    """Solve part 2."""
    fs_size = 70000000
    update_size = 30000000
    free_space = fs_size - get_directory_size(tree)
    space_needed = update_size - free_space

    return find_best_directory_to_delete(tree, space_needed, fs_size)


def find_best_directory_to_delete(tree: dict, space_needed: int, size: int) -> int:
    """Find the smallest directory, which is at least space_needed size."""
    for val in tree.values():
        if isinstance(val, dict):
            dir_size = get_directory_size(val)
            if space_needed <= dir_size < size:
                size = dir_size
            size = find_best_directory_to_delete(val, space_needed, size)

    return size


def get_directory_size(tree: dict) -> int:
    """Get the total size for a directory."""
    size = 0
    for val in tree.values():
        if isinstance(val, dict):
            size += get_directory_size(val)
        else:
            size += val
    return size


if __name__ == "__main__":
    main()
