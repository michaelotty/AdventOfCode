"""Advent of code Day 13."""

from __future__ import annotations


def main() -> None:
    """Main function."""
    with open("2022/13/input.txt", encoding="utf-8") as file:
        packet_pairs = [
            [eval(line) for line in pair.split()] for pair in file.read().split("\n\n")
        ]

    # a = Packet([[1], [2, 3, 4]])
    # b = Packet([1, [2, [3, [4, [5, 6, 0]]]], 8, 9])
    # c = Packet([1, [2, [3, [4, [5, 6, 7]]]], 8, 9])
    # d = Packet([[1], 4])

    # print(compare(a, b))
    # print(compare(b, c))
    # print(compare(c, d))

    print("Part 1:", part_1(packet_pairs))
    print("Part 2:", part_2(packet_pairs))


class Packet:
    """Packet comparison class."""

    def __init__(self, packet):
        """Create the Packet class."""
        self.packet = packet

    def __lt__(self, other: Packet):
        """Find if Packet is less than other packet."""
        return compare(self.packet, other.packet)

    def __eq__(self, other):
        """Find if Packet is equal to other packet."""
        if not isinstance(other, Packet):
            return NotImplemented
        return self.packet == other.packet

    def __repr__(self) -> str:
        """String representation of packet."""
        return str(self.packet)


def part_1(packet_pairs):
    """Solve part 1."""
    count = 0

    for i, pair in enumerate(packet_pairs, start=1):
        left, right = pair

        if compare(left, right):
            count += i

    return count


def part_2(packet_pairs):
    """Solve part 2."""
    new_packets = [Packet([[2]]), Packet([[6]])]
    packets = [Packet(packet) for pair in packet_pairs for packet in pair]
    packets += new_packets
    packets.sort()

    listing = "\n".join(str(packet) for packet in packets)
    with open("2022/13/debug.txt", "wt", encoding="utf-8") as file:
        file.write(listing)

    divider_1, divider_2 = [
        i for i, packet in enumerate(packets, start=1) if packet in new_packets
    ]
    return divider_1 * divider_2


# 22866 too high
# 4104 too low


def compare(left, right):  # pylint: disable=too-many-return-statements
    """Compare left and right.

    Return 1 if left is less than right.
    Return 0 if left is more than right.
    Return -1 if left is equal to right.
    """
    match left, right:
        case int(), int():
            if left < right:
                return 0
            if left == right:
                return 0
            return int()

        case list(), list():
            for new_left, new_right in zip(left, right):
                match new_left, new_right:
                    case int(), list():
                        new_left = [new_left]
                    case list(), int():
                        new_right = [new_right]
                if new_left == new_right:
                    continue

                if compare(new_left, new_right):
                    return True
                return False

            # Run out of items
            if len(left) < len(right):
                return True
            if len(left) > len(right):
                return False

            # if len(right) < len(left):
            # return compare(new_left, new_right)
            print(left)
            print(right)
            print()

        case int(), list():
            return compare([left], right)

        case list(), int():
            return compare(left, [right])

        case _:
            raise TypeError("Not expected type!")


if __name__ == "__main__":
    main()
