import re
import copy


def parse_data(data):
    regex = r"^Card\s+(\d+): (.*?)\|(.*)$"
    parsed_data = []
    matches = re.finditer(regex, data, re.MULTILINE)
    for m in matches:
        num = int(m.group(1))
        winning = [int(w) for w in m.group(2).split()]
        actual = [int(a) for a in m.group(3).split()]
        parsed_data.append(
            {"id": num, "winning_numbers": winning, "actual_numbers": actual}
        )
    return parsed_data


def part_one(parsed_data):
    point_sum = 0
    for card in parsed_data:
        n_winners = sum(a in card["winning_numbers"] for a in card["actual_numbers"])
        if not n_winners:
            continue
        point_sum += 2 ** (n_winners - 1)

    print(f"  Sum of all card points: {point_sum}")


def part_two(parsed_data):
    tmp = copy.deepcopy(parsed_data)
    nums = [1] * len(tmp)
    total = 0
    while len(tmp) > 0:
        card = tmp.pop(0)
        n_winners = sum(a in card["winning_numbers"] for a in card["actual_numbers"])
        for n in range(n_winners):
            nums[card["id"] + n] += nums[card["id"] - 1]
    print(f"  Total number of cards: {sum(nums)}")


def solution(data):
    cards = parse_data(data)
    print("Part 1:")
    part_one(cards)
    print("Part 2:")
    part_two(cards)
