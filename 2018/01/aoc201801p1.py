"""Advent of code Day 1 part 1"""


def main():
    """Main function"""
    with open("2018/01/input.txt", encoding="utf-8") as file:
        print(sum(int(i) for i in file.readlines()))


if __name__ == "__main__":
    main()
