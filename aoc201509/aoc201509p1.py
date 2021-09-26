"""Advent of code Day 9 part 1"""


def main():
    """Main function"""
    with open('test.txt') as f:
        file_lines = f.read().split('\n')

    nodes = {}

    for line in file_lines:
        route, distance = line.split(' = ')
        from_loc, to_loc = route.split(' to ')
        distance = int(distance)

        if from_loc not in nodes:
            nodes[from_loc] = Node()
        if to_loc not in nodes:
            nodes[to_loc] = Node()

        nodes[from_loc].add_neighbor(nodes[to_loc], distance)
        nodes[to_loc].add_neighbor(nodes[from_loc], distance)
    
    print(nodes)


class Node:
    def __init__(self):
        self.neighbors = []

    def add_neighbor(self, node, distance: int):
        self.neighbors.append((node, distance))

    def __repr__(self) -> str:
        return f'Neighbors: {self.neighbors}'


if __name__ == "__main__":
    main()
