"""Advent of code Day 10 part 1 and 2"""


def main() -> None:
    """Main function"""
    with open("2015/10/input.txt", encoding="utf-8") as f:
        file_input = f.read()

    output = file_input
    for _ in range(40):
        output = find_look_and_say_string(output)
    print(f"40 iterations: {len(output)}")

    for _ in range(10):
        output = find_look_and_say_string(output)
    print(f"50 iterations: {len(output)}")


def find_look_and_say_string(in_str: str) -> str:
    """Finds the look-and-say sequence string"""
    output = str()
    count = 0
    last_ch = None

    for ch in in_str:
        if last_ch != ch and last_ch is not None:
            output += f"{count}{last_ch}"
            count = 0
        count += 1
        last_ch = ch

    output += f"{count}{last_ch}"
    return output


if __name__ == "__main__":
    main()
