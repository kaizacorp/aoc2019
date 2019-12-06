import sys


def main():
    filename = sys.argv[1]
    Intcode = open(filename).read().split(',')
    Intcode.append(Intcode.pop().rstrip())
    Intcode = list(map(int, Intcode))
    # print(Intcode)

    # parse opcode
    index = 0
    instruction = Intcode[index]

    parameter_modes, opcode = parse_instruction(instruction)

    step_size = 4
    while opcode != 99:
        print_as_input(Intcode)
        if opcode == 1:
            print(parameter_modes, opcode)
            if parameter_modes[2]:
                a = Intcode[index+1]
            else:
                a = Intcode[Intcode[index+1]]

            if parameter_modes[1]:
                b = Intcode[index+2]
            else:
                b = Intcode[Intcode[index+2]]

            dest = Intcode[index+3]
            Intcode[dest] = a + b
            step_size = 4
        elif opcode == 2:
            print(parameter_modes, opcode)
            if parameter_modes[2]:
                a = Intcode[index+1]
            else:
                a = Intcode[Intcode[index+1]]

            if parameter_modes[1]:
                b = Intcode[index+2]
            else:
                b = Intcode[Intcode[index+2]]
            dest = Intcode[index+3]
            Intcode[dest] = a * b
            step_size = 4
        elif opcode == 3:
            print(parameter_modes, opcode)
            user_value = input("input:  \t ")
            Intcode[Intcode[index+1]] = int(user_value)
            step_size = 1
        elif opcode == 4:
            print(parameter_modes, opcode)
            if parameter_modes[2]:
                stored_value = Intcode[index+1]
            else:
                stored_value = Intcode[Intcode[index+1]]
            print("output:", "\t", stored_value)
            step_size = 1
        elif opcode == 5 or opcode == 6:
            print(parameter_modes, opcode)
            if parameter_modes[2]:
                a = Intcode[index+1]
            else:
                a = Intcode[Intcode[index+1]]

            if parameter_modes[1]:
                b = Intcode[index+2]
            else:
                b = Intcode[Intcode[index+2]]

            if (a and opcode == 5) or (not a and opcode == 6):
                index = b
                step_size = 0
            else:
                step_size = 3

        index += step_size
        instruction = Intcode[index]
        parameter_modes, opcode = parse_instruction(instruction)

    # print_as_input(Intcode)


def print_as_input(Intcode):
    result = ",".join(list(map(str, Intcode)))
    print(result)


def parse_instruction(instruction):
    instruction = str(instruction)
    A = 0
    B = 0
    C = 0

    if len(instruction) >= 2:
        D = instruction[-2]
    else:
        D = '0'
    E = instruction[-1]

    if len(instruction) >= 3:
        C = int(instruction[-3])
    if len(instruction) >= 4:
        B = int(instruction[-4])

    parameter_modes = (A, B, C)
    opcode = D + E
    return parameter_modes, int(opcode)


if __name__ == "__main__":
    main()
