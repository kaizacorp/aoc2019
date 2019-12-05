import sys


def main():
    filename = sys.argv[1]
    number_range = open(filename).read().split('\n')
    lower = int(number_range[0].split("-")[0])
    upper = int(number_range[0].split("-")[1])

    print(lower, upper)
    valid = []

    for password in range(lower, upper):
        if has_double_digits(password) and is_increasing_digits(password):
            valid.append(password)

    print(len(valid))


def has_double_digits(integer):
    integer = str(integer)
    if '00' in integer or '11' in integer or '22' in integer or '33' in integer or '44' in integer or '55' in integer or '66' in integer or '77' in integer or '88' in integer or '99' in integer:
        return True
    return False


if __name__ == "__main__":
    main()
