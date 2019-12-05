import sys


def main():
    filename = sys.argv[1]
    number_range = open(filename).read().split('\n')
    lower = int(number_range[0].split("-")[0])
    upper = int(number_range[0].split("-")[1])

    print(lower, upper)


if __name__ == "__main__":
    main()
