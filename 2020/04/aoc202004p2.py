"""Advent of code 2020 day 4"""

with open("question.txt", encoding="utf-8") as f:
    text = f.read()
    lines = text.split("\n\n")
    VALID_RECORDS = 0

    for line in lines:
        split_line = line.split()
        record: dict[str, int | None] = {
            "ecl": None,
            "pid": None,
            "eyr": None,
            "hcl": None,
            "byr": None,
            "iyr": None,
            "cid": None,
            "hgt": None,
        }

        HAS_INVALID_ENTRIES = False
        HAS_VALID_HEIGHT = True
        HAS_VALID_BIRTH = True
        HAS_VALID_ISSUE = True
        HAS_VALID_EXPIRY = True
        HAS_VALID_ID = True
        HAS_VALID_HAIR = True
        HAS_VALID_EYE = True

        for item in split_line:
            split_item = item.split(":")
            key = split_item[0]
            val_str = split_item[1]
            if key == "hgt":
                if val_str[-2:] == "cm":
                    val = int(val_str[:-2])
                    if not 150 <= val <= 193:
                        HAS_INVALID_ENTRIES = True
                elif val_str[-2:] == "in":
                    val = int(val_str[:-2])
                    if not 59 <= val <= 76:
                        HAS_INVALID_ENTRIES = True
                else:
                    HAS_INVALID_ENTRIES = True
            elif key == "byr":
                val = int(val_str)
                if not 1920 <= val <= 2002:
                    HAS_INVALID_ENTRIES = True
            elif key == "iyr":
                val = int(val_str)
                if not 2010 <= val <= 2020:
                    HAS_INVALID_ENTRIES = True
            elif key == "eyr":
                val = int(val_str)
                if not 2020 <= val <= 2030:
                    HAS_INVALID_ENTRIES = True
            elif key == "pid":
                if len(val_str) != 9:
                    HAS_INVALID_ENTRIES = True
                else:
                    for char in val_str:
                        if char not in "0123456789":
                            HAS_INVALID_ENTRIES = True
                            break
            elif key == "hcl":
                if len(val_str) != 7 or val_str[0] != "#":
                    HAS_INVALID_ENTRIES = True
                else:
                    for char in val_str[1:].lower():
                        if char not in "0123456789abcdef":
                            HAS_INVALID_ENTRIES = True
                            break
            elif key == "ecl":
                if val_str not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    HAS_INVALID_ENTRIES = True
            elif key == "cid":
                pass
            else:
                raise KeyError("Invalid Key")

            record[key] = val
        record.pop("cid")
        if (None in record.values()) or HAS_INVALID_ENTRIES:
            pass
        else:
            VALID_RECORDS += 1

    print(VALID_RECORDS)
