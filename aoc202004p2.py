"""Advent of code 2020 day 4"""

with open('question.txt', 'rt') as f:
    text = f.read()
    lines = text.split('\n\n')
    VALID_RECORDS = 0

    for line in lines:
        line = line.split()
        record = {'ecl': None, 'pid': None, 'eyr': None, 'hcl': None,
                  'byr': None, 'iyr': None, 'cid': None, 'hgt': None}

        HAS_INVALID_ENTRIES = False
        HAS_VALID_HEIGHT = True
        HAS_VALID_BIRTH = True
        HAS_VALID_ISSUE = True
        HAS_VALID_EXPIRY = True
        HAS_VALID_ID = True
        HAS_VALID_HAIR = True
        HAS_VALID_EYE = True

        for item in line:
            item = item.split(':')
            key = item[0]
            val = item[1]
            if key == 'hgt':
                if val[-2:] == 'cm':
                    val = int(val[:-2])
                    if not 150 <= val <= 193:
                        HAS_INVALID_ENTRIES = True
                elif val[-2:] == 'in':
                    val = int(val[:-2])
                    if not 59 <= val <= 76:
                        HAS_INVALID_ENTRIES = True
                else:
                    HAS_INVALID_ENTRIES = True
            elif key == 'byr':
                val = int(val)
                if not 1920 <= val <= 2002:
                    HAS_INVALID_ENTRIES = True
            elif key == 'iyr':
                val = int(val)
                if not 2010 <= val <= 2020:
                    HAS_INVALID_ENTRIES = True
            elif key == 'eyr':
                val = int(val)
                if not 2020 <= val <= 2030:
                    HAS_INVALID_ENTRIES = True
            elif key == 'pid':
                if len(val) != 9:
                    HAS_INVALID_ENTRIES = True
                else:
                    for char in val:
                        if char not in '0123456789':
                            HAS_INVALID_ENTRIES = True
                            break
            elif key == 'hcl':
                if len(val) != 7 or val[0] != '#':
                    HAS_INVALID_ENTRIES = True
                else:
                    for char in val[1:].lower():
                        if char not in '0123456789abcdef':
                            HAS_INVALID_ENTRIES = True
                            break
            elif key == 'ecl':
                if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl',
                               'oth']:
                    HAS_INVALID_ENTRIES = True
            elif key == 'cid':
                pass
            else:
                raise KeyError('Invalid Key')

            record[key] = val
        record.pop('cid')
        if (None in record.values()) or HAS_INVALID_ENTRIES:
            pass
        else:
            VALID_RECORDS += 1

    print(VALID_RECORDS)
