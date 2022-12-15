import os
path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(path, "input.txt")

with open(input_path) as f:
    data = f.read()

################################### Part 1 ###################################
# Opponent:
# A = Rock
# B = Paper
# C = Scissors
# Respoonse:
# X = Rock
# Y = Paper
# Z = Scissors

RESPONSE_MAP = {
    # Index 0 = loose, 1 = tie, 2 = win
    "A": ["Z", "X", "Y"],
    "B": ["X", "Y", "Z"],
    "C": ["Y", "Z", "X"]
}

POINTS_MAP = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

total_points = 0
for line in data.splitlines():
    opponent, response = line.split()

    # Add the points for the shape selection
    points = POINTS_MAP[response]
    # 0 points for loose, 3 for tie, 6 for win
    for i, res in enumerate(RESPONSE_MAP[opponent]):
        if res == response:
            points += i*3

    total_points += points

print(f"Total score following the strategy guide: {total_points}")

################################### Part 2 ###################################
# Response:
# X = Loose the round
# Y = Tie the round
# Z = Win the round

RESPONSE_MAP = {
    # Index 0 = loose, 1 = tie, 2 = win
    "A": ["C", "A", "B"],
    "B": ["A", "B", "C"],
    "C": ["B", "C", "A"]
}

POINTS_MAP = {
    "A": 1,
    "B": 2,
    "C": 3
}

total_points = 0
for line in data.splitlines():
    opponent, outcome = line.split()
    points = 0

    # Loose
    if outcome == "X":
        response = RESPONSE_MAP[opponent][0]
    # Tie
    elif outcome == "Y":
        response = RESPONSE_MAP[opponent][1]
        points += 3
    # Win
    else:
        response = RESPONSE_MAP[opponent][2]
        points += 6

    points += POINTS_MAP[response]
    total_points += points

print(f"Total score following the correct strategy guide: {total_points}")



