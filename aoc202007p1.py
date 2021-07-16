"""Advent of Code 2020 7 part 1"""

import re
from queue import Queue

with open('question.txt') as f:
    file_content = f.read()

search_string_queue = Queue()
search_string_queue.put('shiny gold bag')
searched_strings = []

while True:
    search_string = search_string_queue.get()
    pattern = r'\w+ \w+ \w+ contain.*' + search_string + '.*'
    matches = re.findall(pattern, file_content)
    for match in matches:
        match_string = re.findall(r'\w* \w* bag', match)[0]
        if match_string not in searched_strings:
            search_string_queue.put(match_string)
            searched_strings.append(match_string)

    if search_string_queue.empty():
        break

print(searched_strings)
print(len(searched_strings))
