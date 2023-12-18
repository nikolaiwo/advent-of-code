import numpy as np


def parse_data(data):
    values = []
    for line in data.splitlines():
        values.append([int(i) for i in line.split()])
    return values


def extrapolate(inputs):
    outputs = [inputs]
    while any(outputs[-1]):
        output = [
            outputs[-1][j] - outputs[-1][j - 1] for j in range(1, len(outputs[-1]))
        ]
        outputs.append(output)
    return outputs


def part_one(parsed_data):
    extrapolated_values = []
    for line in parsed_data:
        values = extrapolate(line)
        last_values = [v[-1] for v in reversed(values)]
        extrapolated_values.append(np.cumsum(last_values)[-1])

    solution = sum(extrapolated_values)
    print(f"  Solution: {solution}")


def part_two(parsed_data):
    extrapolated_values = []
    for line in parsed_data:
        values = extrapolate(line)
        first_values = [v[0] for v in reversed(values)]

        new_values = [0]
        for i in range(1, len(first_values)):
            new_values.append(first_values[i] - new_values[i - 1])
        extrapolated_values.append(new_values[-1])
    solution = sum(extrapolated_values)
    print(f"  Solution: {solution}")


def solution(data):
    parsed_data = parse_data(data)
    print("Part 1:")
    part_one(parsed_data)
    print("Part 2:")
    part_two(parsed_data)
