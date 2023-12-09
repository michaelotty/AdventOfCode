"""Advent of code Day 4 part 1 and 2"""

from __future__ import annotations

import re
from datetime import datetime, time, timedelta
from operator import itemgetter


class Guard:
    """A guard who has a record of shifts"""

    def __init__(self, guard_id: int) -> None:
        """Creates a Guard"""
        self.id: int = guard_id
        self.shift_record: list[Shift] = []

    def __repr__(self) -> str:
        return "Guard(" + str(self.id) + ")"

    def __gt__(self, other):
        return self.calculate_minutes_asleep() > other.calculate_minutes_asleep()

    @property
    def awake_time(self) -> list[int]:
        """A list with count of times awake"""
        awake_time = [0 for _ in range(60)]
        for i in range(60):
            for shift in self.shift_record:
                awake_time[i] += shift.awake_schedule[i]
        return awake_time

    @property
    def asleep_time(self) -> list[int]:
        """A list with count of times asleep"""
        awake_time = self.awake_time
        return [len(self.shift_record) - awake_time[i] for i in range(60)]

    @property
    def most_sleepy_minute(self) -> int:
        """Returns most sleepy time"""
        return min(enumerate(self.awake_time), key=itemgetter(1))[0]

    def add_shift(self, shift: Shift) -> None:
        """Adds a shift to the shift record"""
        self.shift_record.append(shift)

    def calculate_minutes_asleep(self) -> int:
        """Calculate the total minutes asleep"""
        return sum(shift.get_minutes_asleep() for shift in self.shift_record)


class Shift:
    """A work shift"""

    def __init__(self, lines: list[tuple[datetime, str]]) -> None:
        """Creates the Shift object"""
        # If empty list, they were awake the whole time
        if not lines:
            self.time_awake = timedelta(minutes=60)
            self.time_asleep = timedelta(minutes=0)
            self.awake_schedule = [1 for _ in range(60)]
            return

        self.time_awake = timedelta()
        self.time_asleep = timedelta()
        self.awake_schedule = [1 for _ in range(60)]

        last_time = datetime.combine(lines[0][0].date(), time(0))

        is_awake = True

        for line in lines:
            current_time = line[0]

            if is_awake:
                self.time_awake += current_time - last_time
                is_awake = False
            else:
                self.time_asleep += current_time - last_time
                for i in range(last_time.minute, current_time.minute):
                    self.awake_schedule[i] -= 1
                is_awake = True
            last_time = current_time

    def __repr__(self) -> str:
        return "Shift(" + str(self.time_awake) + ")"

    def get_minutes_asleep(self) -> int:
        """Gets the total minutes asleep on the shift"""
        return self.time_asleep.seconds // 60


def main() -> None:
    """Main function"""
    with open("2018/04/input.txt", encoding="utf-8") as file:
        unsorted_lines = [
            (datetime.fromisoformat(date_time), desc)
            for date_time, desc in re.findall(r"\[(.+)\] (.+)", file.read())
        ]

    lines: list[tuple[datetime, str]] = sorted(unsorted_lines, key=itemgetter(0))

    guard_ids = [int(x) for x in re.findall(r"#(\d+)", "".join(str(lines)))]
    guards: dict[int, Guard] = {}

    for guard_id in sorted(set(guard_ids)):
        guards[guard_id] = Guard(guard_id)

    shift_starts = [i for i, line in enumerate(lines) if line[1].startswith("Guard")]

    for i, shift_start in enumerate(shift_starts):
        guard_id = int(lines[shift_start][1].split()[1][1:])

        if shift_start == shift_starts[-1]:
            guards[guard_id].add_shift(Shift(lines[shift_start + 1 :]))
        else:
            guards[guard_id].add_shift(
                Shift(lines[shift_start + 1 : shift_starts[i + 1]])
            )

    most_sleepy_guard = max(guards.values())

    print("Part 1")
    print(most_sleepy_guard.most_sleepy_minute * most_sleepy_guard.id)

    guard_id, time_asleep = max(
        ((key, max(item.asleep_time)) for key, item in guards.items()),
        key=itemgetter(1),
    )

    print("\nPart 2")
    print(guard_id * guards[guard_id].asleep_time.index(time_asleep))


if __name__ == "__main__":
    main()
