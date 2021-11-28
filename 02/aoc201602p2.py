"""Advent of code Day 2 part 2"""


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        digit_sequences = file.read().split()

    # Position of middle digit
    position = (0, 2)
    previous_position = position
    digits = {(2, 4): '1',
              (1, 3): '2', (2, 3): '3', (3, 3): '4',
              (0, 2): '5', (1, 2): '6', (2, 2): '7', (3, 2): '8', (4, 2): '9',
              (1, 1): 'A', (2, 1): 'B', (3, 1): 'C',
              (2, 0): 'D'}

    code = []

    for digit_sequence in digit_sequences:
        for direction in digit_sequence:
            if direction == 'U':
                position = (position[0], position[1] + 1)
            elif direction == 'R':
                position = (position[0] + 1, position[1])
            elif direction == 'D':
                position = (position[0], position[1] - 1)
            elif direction == 'L':
                position = (position[0] - 1, position[1])
            else:
                raise ValueError(f'{direction} is not a valid direction')

            if position not in digits:
                position = previous_position

            previous_position = position

        code.append(digits[position])

    print(''.join(code))


if __name__ == "__main__":
    main()
