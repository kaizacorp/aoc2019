import sys


def main():
    filename = sys.argv[1]
    wires = open(filename).read().split('\n')
    #del wires[2]
    first_wire = wires[0].split(",")
    second_wire = wires[1].split(",")
    print(first_wire)
    print(second_wire)

    #   track wire positions in list
    #   start from (0,0)
    #   Process each instruction for wire
    #       letter for (+ - x y) and iterate over magnitude
    #       adding coordinate pairs to respective wire list as 'walk' progresses
    #           check if collision? can own wires collide?
    #   when magnitude finished: process next instruction in wire list

    #   repeat for the second wire
    #   if collision with wire 1:
    #       compute Manhattan distance from origin
    #       take min so far
    # return min intersection


if __name__ == "__main__":
    main()
