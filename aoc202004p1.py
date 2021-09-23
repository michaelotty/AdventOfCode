"""Advent of code 2020 day 4"""

with open('question.txt', 'rt') as f:
    text = f.read()
    lines = text.split('\n\n')
    valid_records = 0

    for line in lines:
        line = line.split()
        record = {'ecl': None, 'pid': None, 'eyr': None, 'hcl': None,
                  'byr': None, 'iyr': None, 'cid': None, 'hgt': None}
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

    print(valid_records)
