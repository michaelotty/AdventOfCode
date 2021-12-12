"""Advent of code 2020 day 4"""

import re

def part_1(lines):
    """Part 1 of puzzle"""
    valid_records = 0

    for line in lines:
        record = dict(re.findall(r'(\w+):(\w+)', line))

        numeric_keys = ['byr', 'iyr', 'eyr', 'pid', 'cid']
        for numeric_key in numeric_keys:
            if 
            record.get(numeric_key)
        record = dict(i.split(':') for i in line)
        print(record)



        # record = {'ecl': None, 'pid': None, 'eyr': None, 'hcl': None,
        #           'byr': None, 'iyr': None, 'cid': None, 'hgt': None}
        for item in line:
            item = item.split(':')
            key = item[0]
            val = int(item[1].replace('cm', ''))
            record[key] = val
        record.pop('cid')

        if None in record.values():
            pass
        else:
            valid_records += 1

    return valid_records


def part_2(lines):
    """Part 2 of puzzle"""
    return lines


def main():
    """Start of program execution"""
    with open('test.txt', encoding='utf-8') as file:
        lines = file.read().split('\n\n')

    print(f'Part 1: {part_1(lines)}')
    print(f'Part 2: {part_2(lines)}')


if __name__ == "__main__":
    main()
