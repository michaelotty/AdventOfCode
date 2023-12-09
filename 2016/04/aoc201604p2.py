"""Advent of code Day 4 part 2"""

from collections import Counter
from string import ascii_lowercase as letters


def shift_cipher(encoded_text: str, room_number: int) -> str:
    """Decodes encoded text"""
    room_number %= len(letters)
    cipher = str.maketrans(letters, letters[room_number:] + letters[:room_number])
    decoded_text = encoded_text.translate(cipher)
    return decoded_text


def main() -> None:
    """Main function"""
    with open("2016/04/input.txt", encoding="utf-8") as file:
        lines = file.read().splitlines()

    real_rooms = []
    real_room_ids = []
    not_real_rooms = []

    for line in lines:
        room_name, checksum = line.split("[")
        room_number = int(room_name.split("-")[-1])
        room_name = "".join(room_name.split("-")[:-1])
        checksum = checksum.removesuffix("]")
        rearranged_room_name = "".join(sorted(i for i in room_name if i.isalpha()))
        new_checksum = "".join(
            x[0] for x in Counter(rearranged_room_name).most_common()
        )

        if new_checksum.startswith(checksum):
            real_rooms.append(room_name)
            real_room_ids.append(room_number)
        else:
            not_real_rooms.append(room_name)

    for room_number, room_name in zip(real_room_ids, real_rooms):
        if shift_cipher(room_name, room_number).startswith("north"):
            print(
                f"{room_number} : {room_name} -> {shift_cipher(room_name, room_number)}"
            )


if __name__ == "__main__":
    main()
