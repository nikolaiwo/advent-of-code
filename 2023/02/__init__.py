import re


def parse_game(game):
    """Parse game data into a dictionary with number of cubes"""
    result = {"red": 0, "green": 0, "blue": 0}
    for color in result.keys():
        num_regex = re.compile(f"(\d+) {color}")
        try:
            num = int(re.search(num_regex, game).group(1))
        except AttributeError:
            num = 0
        result[color] = num
    return result


def parse_input(data):
    """Turn input into sensible dictionary"""
    parsed_data = {}
    regex = r"^Game (\d+):(.*)$"
    for line in data.splitlines():
        m = re.search(regex, line)
        game_id = int(m.group(1))
        games = m.group(2).split(";")
        parsed_data[game_id] = [parse_game(game) for game in games]
    return parsed_data


def test_colors(game):
    max_numbers = {"red": 12, "green": 13, "blue": 14}
    for color in max_numbers.keys():
        if game[color] > max_numbers[color]:
            return False
    return True


def part_one(parsed_data):
    possible_game_ids = []
    for game_id, games in parsed_data.items():
        if all([test_colors(game) for game in games]):
            possible_game_ids.append(game_id)

    print(f"  The sum of the possible game IDs: {sum(possible_game_ids)}")


def part_two(parsed_data):
    powers = []
    for games in parsed_data.values():
        blues = []
        reds = []
        greens = []

        for game in games:
            blues.append(game["blue"])
            reds.append(game["red"])
            greens.append(game["green"])

        powers.append(max(blues) * max(reds) * max(greens))
    print(f"  The sum of the cube powers: {sum(powers)}")


def solution(data):
    parsed_data = parse_input(data)
    print("Part 1:")
    part_one(parsed_data)
    print("Part 2:")
    part_two(parsed_data)
