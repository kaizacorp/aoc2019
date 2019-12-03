import sys
import math


def main():
    filename = sys.argv[1]
    module_masses = open(filename).read().split('\n')
    del module_masses[-1]

    module_masses = list(map(int, module_masses))
    fuel_list = [(math.floor(mass/3) - 2) for mass in module_masses]
    print(sum(fuel_list))


if __name__ == "__main__":
    main()
