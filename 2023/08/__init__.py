import math
import re


def complete(positions):
    return all([p[-1] == "Z" for p in positions])


def part_one(directions, movements):
    counter = 0

    position = "AAA"
    while position != "ZZZ":
        for direction in directions:
            position = movements[position][direction]
            counter += 1
            if position == "ZZZ":
                break

    print(f"  Solution: {counter}")


def find_loop_count(directions, movements, starting_position):
    position = starting_position
    count = 0

    moves_to_z = 0
    z_position = ""
    while True:
        for direction in directions:
            position = movements[position][direction]
            count += 1
            if position == z_position:
                return count, moves_to_z
            if position[-1] == "Z":
                moves_to_z = count
                z_position = position


def part_two(directions, movements):
    # Find the list of positions that end with 'A'
    positions = []
    for position in movements.keys():
        if position[-1] == "A":
            positions.append(position)

    # Noticed that all the starting positions goes in a loop,
    # so count it
    loops = []
    for p in positions:
        loops.append(find_loop_count(directions, movements, p))

    # Noticed that the size of the loop is twice the number of steps
    # needed to reach the first 'Z'
    # So we can look for a common multiple between all the loops
    results = [l[1] for l in loops]
    solution = math.lcm(*results)
    print(f"  Solution: {solution}")


def solution(data):
    lines = data.splitlines()

    directions = [d for d in lines[0]]
    movements = {}
    regex = "\w+"
    for line in lines[2:]:
        origin, left, right = re.findall(regex, line)
        movements[origin] = {"L": left, "R": right}

    print("Part 1: ")
    part_one(directions, movements)
    print("Part 2: ")
    part_two(directions, movements)
