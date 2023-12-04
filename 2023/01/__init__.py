import re


def sum_all_calibration_values(data):
    calibration_values = []
    for line in data.splitlines():
        stripped_line = re.sub(r"[^\d]", "", line)
        calibration_value = int(stripped_line[0] + stripped_line[-1])
        calibration_values.append(calibration_value)

    return sum(calibration_values)


def preprocess_string_digits(data):
    """Pre-process the string before using the solution from part one"""
    valid_string_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    # Make a fancy regex to to find the first and last digit
    string_regex = "|".join(valid_string_digits.keys())
    regex = re.compile(f".*?({string_regex}|\d).*({string_regex}|\d)")

    parsed_data = ""
    for line in data.splitlines():
        match = re.search(regex, line)
        try:
            new = match.group(1) + match.group(2)
            for str_rep, value in valid_string_digits.items():
                new = new.replace(str_rep, value)
        except AttributeError:
            new = line

        parsed_data += new + "\n"
    return parsed_data


def solution(data):
    print("Part 1:")
    sum = sum_all_calibration_values(data)
    print(f"  Sum of all calibration values: {sum}")

    print("Part 2:")
    preprocessed_data = preprocess_string_digits(data)
    sum = sum_all_calibration_values(preprocessed_data)
    print(f"  Sum of all calibration values: {sum}")
