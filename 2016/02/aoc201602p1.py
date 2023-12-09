"""Advent of code Day 2 part 1"""


def main() -> None:
    """Main function"""
    with open("2016/02/input.txt", encoding="utf-8") as file:
        digit_sequences = file.read().split()

    # Position of middle digit
    position = (1, 1)
    previous_position = position
    rows = 3
    cols = 3
    digits = {
        (x, y): str(10 - ((3 - x) + (y * 3))) for y in range(rows) for x in range(cols)
    }

    code = []

    for digit_sequence in digit_sequences:
        for direction in digit_sequence:
            if direction == "U":
                position = (position[0], position[1] + 1)
            elif direction == "R":
                position = (position[0] + 1, position[1])
            elif direction == "D":
                position = (position[0], position[1] - 1)
            elif direction == "L":
                position = (position[0] - 1, position[1])
            else:
                raise ValueError(f"{direction} is not a valid direction")

            # Bring back in bounds
            if position not in digits:
                position = previous_position

            previous_position = position

        code.append(digits[position])

    print("".join(code))


if __name__ == "__main__":
    main()
