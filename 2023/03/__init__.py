import numpy as np


def is_symbol(character):
    if character == ".":
        return False
    if character.isdigit():
        return False
    return True


def extract_digit(line, index):
    # Extract the whole digit from a line (searches left and right)
    start_index = index
    stop_index = index

    while line[start_index].isdigit():
        start_index -= 1
    # Compensate for over stepping
    start_index += 1

    while line[stop_index].isdigit():
        stop_index += 1
    # Compensate for over stepping
    stop_index -= 1

    return int("".join(line[start_index : stop_index + 1])), start_index, stop_index


def part_one(array):
    # Dot-pad
    array = np.pad(array, 1, mode="constant", constant_values=".")
    used_map = np.zeros(array.shape)

    v_is_symbol = np.vectorize(is_symbol)
    part_symbol_sum = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j].isdigit():
                section = array[i - 1 : i + 2, j - 1 : j + 2]
                if v_is_symbol(section.flatten()).any():
                    # We have found a part number, search both ways for more digits
                    digit, start, stop = extract_digit(array[i], j)

                    if used_map[i, start : stop + 1].any():
                        continue
                    else:
                        part_symbol_sum += digit
                        used_map[i, start : stop + 1] = 1
    print(f"  The sum of all part numbers: {part_symbol_sum}")


def part_two(array):
    # Dot-pad
    array = np.pad(array, 1, mode="constant", constant_values=".")
    gear_ratios = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "*":
                section = array[i - 1 : i + 2, j - 1 : j + 2]
                digits = np.char.isdigit(section)
                # Less than two digits around the gear, so there's no ratio to calculate
                if np.sum(digits) < 2:
                    continue

                # Extract all the digits
                extracted_digits = set()
                x, y = np.nonzero(digits)
                for coordinates in zip(x, y):
                    extracted_digits.add(
                        extract_digit(
                            array[i + coordinates[0] - 1], j + coordinates[1] - 1
                        )
                    )

                if len(extracted_digits) != 2:
                    continue
                extracted_digits = list(extracted_digits)
                gear_ratios.append(extracted_digits[0][0] * extracted_digits[1][0])
    print(f"  The sum of all gear ratios: {sum(gear_ratios)}")


def solution(data):
    tmp = []
    for line in data.splitlines():
        tmp.append([*line])
    array = np.array(tmp)

    print("Part 1:")
    part_one(array)

    print("Part 2:")
    part_two(array)
