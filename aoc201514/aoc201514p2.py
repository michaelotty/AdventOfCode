"""Advent of code Day 14 part 2"""


def main():
    """Main function"""
    with open('input.txt') as file:
        data = file.readlines()

    reindeer = []
    time = 2503

    for line in data:
        name, _, _, speed, _, _, speed_time, _, _, _, _, _, _, rest_time, _ = line.split()

        name = name[0:3]
        speed = int(speed)
        speed_time = int(speed_time)
        rest_time = int(rest_time)

        reindeer.append(Reindeer(name, speed, speed_time, rest_time))

        reindeer[name] = dict()
        reindeer[name]['speed'] = speed
        reindeer[name]['speed_time'] = speed_time
        reindeer[name]['rest_time'] = rest_time


class Reindeer:
    def __init__(self, name: str, speed: int, speed_time: int, rest_time: int) -> None:
        """Create a Reindeer"""
        self.name = name
        self.speed = speed
        self.speed_time = speed_time
        self.rest_time = rest_time

        self.period = speed_time + rest_time

        self.speed_timer = speed_time
        self.rest_timer = rest_time

        self.is_flying = True
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
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
        """Returns string representation"""
        return f'{self.name}: {self.position}'


if __name__ == "__main__":
    main()
