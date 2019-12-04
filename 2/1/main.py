import sys


def main():
    filename = sys.argv[1]
    Intcode = open(filename).read().split(',')
    Intcode.append(Intcode.pop().rstrip())
    print(Intcode)

    index = 0
    opcode = Intcode[index]
    while opcode != 99:
        if opcode == 1:
            """
            Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.
            """
        elif opcode == 2:
            """
            Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.
            """

        """
        Once you're done processing an opcode, move to the next one by stepping forward 4 positions.
        """
        index += 4
        opcode = Intcode[index]


if __name__ == "__main__":
    main()
