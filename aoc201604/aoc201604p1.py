"""Advent of code Day 4 part 1"""

from collections import Counter


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        lines = file.read().splitlines()

    real_rooms = []
    not_real_rooms = []

    for line in lines:
        room_name, checksum = line.split('[')
        checksum = checksum.removesuffix(']')
        rearranged_room_name = ''.join(sorted(
            i for i in room_name if i.isalpha()))
        new_checksum = ''.join(x[0] for x in Counter(
            rearranged_room_name).most_common())

        if new_checksum.startswith(checksum):
            real_rooms.append(room_name)
        else:
            not_real_rooms.append(room_name)

    print(sum(int(x.split('-')[-1]) for x in real_rooms))


if __name__ == "__main__":
    main()
