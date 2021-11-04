"""Advent of code Day 2 part 1"""


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        digit_sequences = file.read().split()

    # Position of middle digit
    position = (1, 1)
    rows = 3
    cols = 3
    digits = {(x, y): 1 + x + y*3 for y in range(rows) for x in range(cols)}

    code = []

    for digit_sequence in digit_sequences:
        for direction in digit_sequence:
            if direction == 'U':
                position = (position[0], position[1] - 1)
            elif direction == 'R':
                position = (position[0] + 1, position[1])
            elif direction == 'D':
                position = (position[0], position[1] + 1)
            elif direction == 'L':
                position = (position[0] - 1, position[1])
            else:
                raise ValueError(f'{direction} is not a valid direction')

            # Bring back in bounds
            if position[0] < 0:
                position = (0, position[1])
            if position[0] >= cols:
                position = (cols - 1, position[1])
            if position[1] < 0:
                position = (position[0], 0)
            if position[1] >= rows:
                position = (position[0], rows - 1)

        code.append(digits[position])

    print(''.join(str(x) for x in code))


if __name__ == "__main__":
    main()
