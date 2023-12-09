"""Advent of Code 2020 7 part 1"""

import re


def main() -> None:
    """Main function"""
    with open("question.txt", encoding="utf-8") as file:
        file_content = file.read()

    search_string_queue = set()
    search_string_queue.add("shiny gold bag")
    searched_strings = set()

    while True:
        search_string = search_string_queue.pop()
        pattern = r"\w+ \w+ \w+ contain.*" + search_string + ".*"
        matches = re.findall(pattern, file_content)
        for match in matches:
            match_string = re.findall(r"\w* \w* bag", match)[0]
            if match_string not in searched_strings:
                search_string_queue.add(match_string)
                searched_strings.add(match_string)

        if len(search_string_queue) == 0:
            break

    print(len(searched_strings))


if __name__ == "__main__":
    main()
