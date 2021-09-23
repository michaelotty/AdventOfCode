"""Advent of code Day 2 part 1"""

def area_of_cuboid(length: float, width: float, height: float) -> float:
    """Finds the surface area of a cuboid"""
    return 2.0*length*width + 2.0*length*height + 2.0*height*width


def main():
    """Main function"""
    with open('input.txt') as f:
        print(f.read())


if __name__ == "__main__":
    main()
