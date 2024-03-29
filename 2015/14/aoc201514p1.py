"""Advent of code Day 14 part 1."""


def main() -> None:  # pylint: disable=too-many-locals
    """Program starts here."""
    with open("2015/14/input.txt", encoding="utf-8") as file:
        data = file.readlines()

    reindeer = {}
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

        name = name[0:3]
        speed = int(speed_str)
        speed_time = int(speed_time_str)
        rest_time = int(rest_time_str)

        reindeer[name] = speed
        period = speed_time + rest_time
        cycles = time // period
        extra_time = time % period

        cycle_distance = speed_time * speed * cycles
        excess_extra_time = extra_time - speed_time
        if excess_extra_time > 0:
            extra_time -= excess_extra_time

        extra_distance = extra_time * speed
        total_distance = cycle_distance + extra_distance

        print(f"{name}: {total_distance}km")


if __name__ == "__main__":
    main()
