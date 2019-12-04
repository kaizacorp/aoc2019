import sys
from random import randint


def main():
    filename = sys.argv[1]
    Intcode = open(filename).read().split(',')
    Intcode.append(Intcode.pop().rstrip())
    Intcode = list(map(int, Intcode))
    initial_state = Intcode.copy()
    # print(Intcode)

    used = []
    noun = 0
    verb = 0

    #   fix 'noun' and 'verb' as random integer (1-99) -> one not in tracked list
    is_new_pair = False
    while not is_new_pair:
        noun = randint(1, 99)
        verb = randint(1, 99)
        pair = (noun, verb)
        if pair not in used:
            is_new_pair = True
            #   track tuple in list
            used.append(pair)
    #   reset to initial state
    Intcode = initial_state.copy()
    #   assign new noun/verb values to state
    Intcode[1] = noun
    Intcode[2] = verb

    #   compute through opcodes

    index = 0
    opcode = Intcode[index]
    while opcode != 99:
        if opcode == 1:
            a = Intcode[Intcode[index+1]]
            b = Intcode[Intcode[index+2]]
            dest = Intcode[index+3]
            Intcode[dest] = a + b
        elif opcode == 2:
            a = Intcode[Intcode[index+1]]
            b = Intcode[Intcode[index+2]]
            dest = Intcode[index+3]
            Intcode[dest] = a * b

        index += 4
        opcode = Intcode[index]

    print(Intcode[0])

    #   check if final value at position 0 is 19690720
    if Intcode[0] == 19690720:
        #   if true, print 100 * noun + verb
        print("Found!")
        print("Noun: ", noun, "Verb: ", verb)
        print(100 * noun + verb)
    else:
        #   if not, retry with new tuple
        print("Noun: ", noun, "Verb: ", verb)


def print_as_input(Intcode):
    result = ",".join(list(map(str, Intcode)))
    print(result)


if __name__ == "__main__":
    main()
