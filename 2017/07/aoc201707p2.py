"""Advent of code Day 7 part 1"""

import re


def get_weight(tree: dict, weights: dict, key: str) -> tuple[int, str]:
    """Returns the corrected value for the unbalanced child"""
    child_weight = 0
    for child in tree[key]:
        weight, _ = get_weight(tree, weights, child)
        child_weight += weight
    return (weights[key] + child_weight, key)


def main():
    """Main function"""
    with open("input.txt", encoding="utf-8") as file:
        lines = file.readlines()

    weights = {}
    tree = {}

    for line in lines:
        label, weight, *extra = re.findall(r"\w+", line)
        weights[label] = int(weight)
        tree[label] = tuple(extra)

    root_key = (
        set(weights) - {child for children in tree.values() for child in children}
    ).pop()

    # Manually go through each layer by inspection
    print(sorted((get_weight(tree, weights, key) for key in tree[root_key])))
    print(sorted((get_weight(tree, weights, key) for key in tree["nhrla"])))
    print(sorted((get_weight(tree, weights, key) for key in tree["idfyy"])))
    print(sorted((get_weight(tree, weights, key) for key in tree["aobgmc"])))

    weight_heavy, _ = get_weight(tree, weights, "aobgmc")
    weight_light, _ = get_weight(tree, weights, "iqwspxd")
    print(weights["aobgmc"] - (weight_heavy - weight_light))


if __name__ == "__main__":
    main()
