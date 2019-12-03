import sys
import math


def main():
    filename = sys.argv[1]
    module_masses = open(filename).read().split('\n')
    del module_masses[-1]

    module_masses = list(map(int, module_masses))
    fuel_list = [calc_fuel(mass) for mass in module_masses]
    print(sum(fuel_list))


def calc_fuel(mass):
    if mass <= 5:
        return 0
    else:
        fuel = math.floor(mass/3) - 2
        return fuel + calc_fuel(fuel)


if __name__ == "__main__":
    main()
