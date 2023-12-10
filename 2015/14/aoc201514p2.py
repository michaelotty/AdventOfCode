"""Advent of code Day 14 part 2."""

from __future__ import annotations


def main() -> None:
    """Program starts here."""
    with open("2015/14/input.txt", encoding="utf-8") as file:
        data = file.readlines()

    reindeers = []
    time = 2503

    for line in data:
        (
            name,
            _,
            _,
            speed_str,
            _,
            _,
            speed_time_str,
            *_,
            rest_time_str,
            _,
        ) = line.split()

        speed = int(speed_str)
        speed_time = int(speed_time_str)
        rest_time = int(rest_time_str)

        reindeers.append(Reindeer(name, speed, speed_time, rest_time))

    for _ in range(time):
        reindeer_positions = []
        for reindeer in reindeers:
            next(reindeer)
            reindeer_positions.append(reindeer.position)
        for reindeer in reindeers:
            if reindeer.position == max(reindeer_positions):
                reindeer.add_point()

    print(", ".join(str(reindeer) for reindeer in reindeers))


class Reindeer:  # pylint: disable=too-many-instance-attributes
    """Reindeer class."""

    def __init__(self, name: str, speed: int, speed_time: int, rest_time: int) -> None:
        """Create a Reindeer."""
        self.name = name
        self.speed = speed
        self.speed_time = speed_time
        self.rest_time = rest_time

        self.period = speed_time + rest_time

        self.speed_timer = speed_time
        self.rest_timer = rest_time

        self.is_flying = True
        self.position = 0
        self.points = 0

    def __iter__(self) -> Reindeer:
        """Return the iterator."""
        return self

    def __next__(self) -> None:
        """Increment iterator."""
        if self.is_flying:
            self.position += self.speed
            self.speed_timer -= 1
            if self.speed_timer == 0:
                self.speed_timer = self.speed_time
                self.is_flying = False
        else:
            self.rest_timer -= 1
            if self.rest_timer == 0:
                self.rest_timer = self.rest_time
                self.is_flying = True

    def __str__(self) -> str:
        """Return string representation."""
        return f"{self.name}: {self.points}"

    def add_point(self) -> None:
        """Add 1 point to points tally."""
        self.points += 1


if __name__ == "__main__":
    main()
