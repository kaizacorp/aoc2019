import sys
import math


def main():
    mass = int(sys.argv[1])
    fuel = math.floor(mass / 3) - 2
    print(fuel)


if __name__ == "__main__":
    main()
