import sys


def main():
    filename = sys.argv[1]
    number_range = open(filename).read().split('\n')
    lower = int(number_range[0].split("-")[0])
    upper = int(number_range[0].split("-")[1])

    print(lower, upper)

    valid = []

    for password in range(lower, upper):
        doubles = has_double_digits(password)
        increasing = is_increasing_digits(password)
        if doubles and increasing:
            valid.append(password)

    print(len(valid))


def has_double_digits(integer):
    integer = str(integer)
    if '00' in integer or '11' in integer or '22' in integer or '33' in integer or '44' in integer or '55' in integer or '66' in integer or '77' in integer or '88' in integer or '99' in integer:
        return True
    return False


def is_increasing_digits(integer):
    integer = str(integer)
    increasing = True

    for first, second in zip(integer[:-1], integer[1:]):
        if int(first) > int(second):
            increasing = False

    return increasing


if __name__ == "__main__":
    main()
