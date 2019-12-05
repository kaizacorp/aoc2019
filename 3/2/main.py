import sys


def main():
    filename = sys.argv[1]
    wires = open(filename).read().split('\n')
    #del wires[2]
    first_wire = wires[0].split(",")
    second_wire = wires[1].split(",")
    # print(first_wire)
    # print(second_wire)

    collisions = []

    #   track wire positions in list
    wire_coordinates = []
    wire_coordinates.append([])
    #   start from (0,0)
    position = (0, 0)
    wire_coordinates[0].append(position)
    #   Process each instruction for wire
    for instruction in first_wire:
        #   letter for (+ - x y) and iterate over magnitude
        direction = instruction[0]
        magnitude = int(instruction[1:])
        #    adding coordinate pairs to respective wire list as 'walk' progresses
        while magnitude > 0:
            if direction == 'U':
                new_position = (position[0], position[1]+1)
            elif direction == 'D':
                new_position = (position[0], position[1]-1)
            elif direction == 'R':
                new_position = (position[0]+1, position[1])
            elif direction == 'L':
                new_position = (position[0]-1, position[1])
            wire_coordinates[0].append(new_position)
            position = new_position
            magnitude -= 1
            #   when magnitude finished: process next instruction in wire list

    # print(wire_coordinates[0])

    #   repeat for the second wire
    wire_coordinates.append([])
    #   start from (0,0)
    position = (0, 0)
    wire_coordinates[1].append(position)
    #   Process each instruction for wire
    for instruction in second_wire:
        #   letter for (+ - x y) and iterate over magnitude
        direction = instruction[0]
        magnitude = int(instruction[1:])
        #    adding coordinate pairs to respective wire list as 'walk' progresses
        while magnitude > 0:
            if direction == 'U':
                new_position = (position[0], position[1]+1)
            elif direction == 'D':
                new_position = (position[0], position[1]-1)
            elif direction == 'R':
                new_position = (position[0]+1, position[1])
            elif direction == 'L':
                new_position = (position[0]-1, position[1])
            wire_coordinates[1].append(new_position)
            #   if collision with wire 1:
            if new_position in wire_coordinates[0]:
                collisions.append(new_position)
            position = new_position
            magnitude -= 1

    # print(wire_coordinates[1])
    # print(collisions)

    #   calculate steps taken for each wire,
    #   find minimum delay / steps
    minimum_steps = sys.maxsize
    for position in collisions:
        first_steps = wire_coordinates[0].index(position)
        second_steps = wire_coordinates[1].index(position)
        steps = first_steps + second_steps
        if steps < minimum_steps:
            minimum_steps = steps

    print(minimum_steps)


if __name__ == "__main__":
    main()
