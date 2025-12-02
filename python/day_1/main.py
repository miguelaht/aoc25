
instructions = """
R21
L500
"""

def part_1(instructions):
    current_position = 50
    hits = 0
    # print("the dial starts by pointing at {}.".format(current_position))
    for instruction in instructions.split("\n"):
        if instruction == "":
            continue

        direction = instruction[0]
        clicks = int(instruction[1:])
        if direction == "R":
            current_position = (current_position + clicks) % 100
        if direction == "L":
            current_position = (current_position - clicks) % 100

        if current_position == 0:
            hits += 1

        # print("the dial is rotated {} to point at {}" .format(instruction, current_position))

    print("answer {}".format(hits))

def part_2_simulated(instructions):
    current_position = 50
    hits = 0
    print("the dial starts by pointing at {}.".format(current_position))
    for instruction in instructions.split("\n"):
        instruction_hits = 0
        if instruction == "":
            continue

        direction = instruction[0]
        ticks = list(range(0, int(instruction[1:])))
        for _ in ticks:
            if direction == "R":
                current_position = (current_position + 1) % 100
            if direction == "L":
                current_position = (current_position - 1) % 100

            if current_position == 0:
                instruction_hits = instruction_hits + 1

        hits = hits + instruction_hits

    print("answer {}".format(hits))

def part_2(instructions):
    current_position = 50
    hits = 0
    # print("the dial starts by pointing at {}.".format(current_position))
    for instruction in instructions.split("\n"):
        instruction_hits = 0
        if instruction == "":
            continue

        direction = instruction[0]
        clicks = int(instruction[1:])

        if direction == "R":
            instruction_hits += (current_position + clicks) // 100
            current_position = (current_position + clicks) % 100

        if direction == "L":
            # count all hundreds i.e 645 = 6 hundreds
            hundreds = clicks // 100
            if hundreds > 0:
                instruction_hits += hundreds

            # use the remainder of the ticks 645 = 45
            remainder = clicks % 100
            if current_position - remainder < 0 and current_position > 0:
                instruction_hits += 1

            current_position = (current_position - clicks) % 100
            if current_position == 0:
                instruction_hits += 1

        hits += instruction_hits

        # if instruction_hits >= 1 and current_position != 0:
            # print("the dial is rotated {} to point at {}. during this rotation, it points at 0 {} times." .format(instruction, current_position, instruction_hits))
        # else:
            # print("the dial is rotated {} to point at {}" .format(instruction, current_position))

    print("answer {}".format(hits))


part_1(instructions)
part_2(instructions)
