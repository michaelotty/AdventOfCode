"""Advent of code Day 8 part 2"""


def main():
    """Main function"""
    with open("input.txt", encoding="utf-8") as f:
        file_lines = f.read().split("\n")

    code_len = sum(len(i) for i in file_lines)
    encoded_lines = [i.encode("unicode_escape").decode() for i in file_lines]
    # Encode quotemark characters
    for i, line in enumerate(encoded_lines):
        if '"' in line:
            encoded_lines[i] = '"' + line.replace(r'"', r"\"") + '"'

    encoded_len = sum(len(i) for i in encoded_lines)

    print(f"Encoded: {encoded_len}")
    print(f"Code: {code_len}")
    print(f"Answer: {encoded_len - code_len}")


if __name__ == "__main__":
    main()
