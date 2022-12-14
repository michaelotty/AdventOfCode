"""Advent of code Day 13."""

from __future__ import annotations


def main():
    """Main function."""
    with open("aoc2022/13/input.txt", encoding="utf-8") as file:
        packet_pairs = [
            [eval(line) for line in pair.split()] for pair in file.read().split("\n\n")
        ]

    print("Part 1:", part_1(packet_pairs))
    print("Part 2:", part_2(packet_pairs))


def part_1(packet_pairs):
    """Solve part 1."""
    count = 0

    for i, pair in enumerate(packet_pairs, start=1):
        left, right = pair

        if left_is_less(left, right):
            count += i

    return count


def left_is_less(left, right):
    """Compare left and right, return True if left is less than right."""
    try:
        return left < right
    except TypeError:
        pass

    match left, right:
        case list(), list():
            for new_left, new_right in zip(left, right):
                if new_left == new_right:
                    continue
                elif left_is_less(new_left, new_right):
                    return True
                return False

        case int(), list():
            return left_is_less([left], right)

        case list(), int():
            return left_is_less(left, [right])

        case _:
            raise TypeError("Not expected type!")


def part_2(packet_pairs):
    """Solve part 2."""
    new_packets = [Packet([[2]]), Packet([[6]])]
    packets = [Packet(packet) for pair in packet_pairs for packet in pair]
    packets += new_packets
    packets.sort()

    nums = []
    for i, packet in enumerate(packets, start=1):
        if packet in new_packets:
            nums.append(i)
    if len(nums) == 2:
        return nums[0] * nums[1]
    return 0


# 22866 too high


class Packet:
    """Packet comparison class."""

    def __init__(self, packet):
        """Create the Packet class."""
        self.packet = packet

    def __lt__(self, other: Packet):
        """Find if Packet is less than other packet."""
        return left_is_less(self.packet, other.packet)

    def __eq__(self, other: Packet):
        """Find if Packet is equal to other packet."""
        return str(self.packet) == str(other.packet)

    def __repr__(self) -> str:
        """String representation of packet."""
        return str(self.packet)


if __name__ == "__main__":
    main()
