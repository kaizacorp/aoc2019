import sys
from itertools import permutations


def main():
    filename = sys.argv[1]

    phases = list(permutations(range(0, 5)))

    thruster_signal = 0
    for phase in phases:
        output = 0
        for sig in phase:
            amp = Intcode_computer(filename, [sig, output])
            output = amp.output
        thruster_signal = max(thruster_signal, output)

    print(thruster_signal)

    """
    amp_A = Intcode_computer(filename, [3, 0])
    print(amp_A.output)
    amp_B = Intcode_computer(filename, [1, amp_A.output])
    print(amp_B.output)
    amp_C = Intcode_computer(filename, [2, amp_B.output])
    print(amp_C.output)
    amp_D = Intcode_computer(filename, [4, amp_C.output])
    print(amp_D.output)
    amp_E = Intcode_computer(filename, [0, amp_D.output])
    print(amp_E.output)

    thruster_signal = 0
    for a in range(0, 5):
        for b in range(0, 5):
            for c in range(0, 5):
                for d in range(0, 5):
                    for e in range(0, 5):
                        A = Intcode_computer(filename, [a, 0])
                        B = Intcode_computer(filename, [b, A.output])
                        C = Intcode_computer(filename, [c, B.output])
                        D = Intcode_computer(filename, [d, C.output])
                        E = Intcode_computer(filename, [e, D.output])
                        thruster_signal = max(thruster_signal, E.output)
                        print(thruster_signal, a, b, c, d, e)

    print(thruster_signal)
    """


class Intcode_computer:
    def __init__(self, filename, inputs):
        self.output = 0
        self.inputs = inputs
        Intcode = open(filename).read().split(',')
        Intcode.append(Intcode.pop().rstrip())
        Intcode = list(map(int, Intcode))

        index = 0
        instruction = Intcode[index]
        parameter_modes, opcode = self.parse_instruction(instruction)

        while opcode != 99:
            # self.print_as_input(Intcode)
            # print(parameter_modes, opcode)
            if opcode == 1:
                step_size = self.op_add(
                    opcode, parameter_modes, Intcode, index)
            elif opcode == 2:
                step_size = self.op_multiply(
                    opcode, parameter_modes, Intcode, index)
            elif opcode == 3:
                step_size = self.op_input(Intcode, index)
            elif opcode == 4:
                step_size = self.op_output(Intcode, index, parameter_modes)
            elif opcode == 5 or opcode == 6:
                step_size, index = self.op_jump(
                    opcode, parameter_modes, Intcode, index)
            elif opcode == 7 or opcode == 8:
                step_size = self.op_less_than_equals(
                    opcode, parameter_modes, Intcode, index)

            index += step_size
            instruction = Intcode[index]
            parameter_modes, opcode = self.parse_instruction(instruction)

    def parse_instruction(self, instruction):
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

    def op_add(self, opcode, parameter_modes, Intcode, index):
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
        return step_size

    def op_multiply(self, opcode, parameter_modes, Intcode, index):
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
        return step_size

    def op_input(self, Intcode, index):
        # user_value = input("input:  \t ")
        Intcode[Intcode[index+1]] = self.inputs[0]
        self.inputs.remove(self.inputs[0])
        step_size = 2
        return step_size

    def op_output(self, Intcode, index, parameter_modes):
        if parameter_modes[2]:
            stored_value = Intcode[index+1]
        else:
            stored_value = Intcode[Intcode[index+1]]
        # print("output:", "\t", stored_value)
        self.output = int(stored_value)
        step_size = 2
        return step_size

    def op_jump(self, opcode, parameter_modes, Intcode, index):
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
        return step_size, index

    def op_less_than_equals(self, opcode, parameter_modes, Intcode, index):
        if parameter_modes[2]:
            a = Intcode[index+1]
        else:
            a = Intcode[Intcode[index+1]]

        if parameter_modes[1]:
            b = Intcode[index+2]
        else:
            b = Intcode[Intcode[index+2]]
        if (a < b and opcode == 7) or (a == b and opcode == 8):
            stored = 1
        else:
            stored = 0

        if parameter_modes[0]:
            Intcode[index+3] = stored
        else:
            Intcode[Intcode[index+3]] = stored
        # print("a:\t", a)
        # print("b:\t", b)
        # print("result:\t", stored)
        step_size = 4
        return step_size

    def print_as_input(self, Intcode):
        result = ",".join(list(map(str, Intcode)))
        print(result)


if __name__ == "__main__":
    main()
