from collections import Counter


class Hand:
    strength = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)

    @property
    def type(self):
        counts = Counter(self.hand)
        values = list(counts.values())
        # 5 of a kind
        if 5 in values:
            return 6
        # 4 of a kind
        if 4 in values:
            return 5
        # Full house
        if 3 in values and 2 in values:
            return 4
        if 3 in values:
            return 3
        if values.count(2) == 2:
            return 2
        if 2 in values:
            return 1
        return 0

    def value(self, rank):
        return rank * self.bid

    def __lt__(self, other):
        if self.type == other.type:
            for pair in zip(self.hand, other.hand):
                s0 = self.strength.index(pair[0])
                s1 = self.strength.index(pair[1])
                if s0 != s1:
                    return s0 < s1
        return self.type < other.type


class HandTwo(Hand):
    strength = ["J", "1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

    @property
    def type(self):
        counts = Counter(self.hand)
        try:
            jokers = counts.pop("J")
        except KeyError:
            jokers = 0

        values = list(counts.values())
        if len(values) == 0:
            values = [5]
        else:
            max_value = max(values)
            max_index = values.index(max_value)
            values[max_index] += jokers
        # 5 of a kind
        if 5 in values:
            return 6
        # 4 of a kind
        if 4 in values:
            return 5
        # Full house
        if 3 in values and 2 in values:
            return 4
        if 3 in values:
            return 3
        if values.count(2) == 2:
            return 2
        if 2 in values:
            return 1
        return 0


def part_one(data):
    hands = []
    for d in data.splitlines():
        hand = Hand(*d.split())
        hands.append(hand)

    sum = 0
    for i, h in enumerate(sorted(hands)):
        sum += h.value(i + 1)
    print(f"  Solution: {sum}")


def part_two(data):
    hands = []
    for d in data.splitlines():
        hand = HandTwo(*d.split())
        hands.append(hand)

    sum = 0
    for i, h in enumerate(sorted(hands)):
        sum += h.value(i + 1)
    print(f"  Solution: {sum}")


def solution(data):
    print("Part 1:")
    part_one(data)
    print("Part 2:")
    part_two(data)
