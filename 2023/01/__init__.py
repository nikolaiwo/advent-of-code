import re


def solution(data):
    calibration_values = []
    for line in data.splitlines():
        stripped_line = re.sub("[^0-9]", "", line)
        calibration_value = int(stripped_line[0] + stripped_line[-1])
        calibration_values.append(calibration_value)

    result = sum(calibration_values)
    print(f"The sum of all calibration values is: {result}")
