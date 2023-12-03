"""Advent of code Day 8 part 1"""


def main():
    """Main function"""
    with open("2015/08/input.txt", encoding="utf-8") as f:
        file_lines = f.read().split("\n")

    code_len = sum(len(i) for i in file_lines)
    memory_len = sum(len(eval(i)) for i in file_lines)

    print(f"Code: {code_len}")
    print(f"Memory: {memory_len}")
    print(f"Answer: {code_len - memory_len}")


if __name__ == "__main__":
    main()
