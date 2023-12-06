import re
from collections import OrderedDict


def parse_data(data):
    # Get seeds
    regex = r"seeds: (.*)$"
    m = re.search(regex, data, re.MULTILINE)
    seeds = [int(i) for i in m.group(1).split()]

    maps = OrderedDict()
    regex = r"^(\S+) map:\n(.*?)(\n{2}|\Z)"
    for m in re.finditer(regex, data, re.DOTALL | re.MULTILINE):
        maps[m.group(1)] = []
        for line in m.group(2).splitlines():
            maps[m.group(1)].append([int(d) for d in line.split()])

    return {"seeds": seeds, "maps": maps}


def calc_new_val(val, map):
    for destination, source, map_range in map:
        if val >= source and val < source + map_range:
            return val + (destination - source)
    return val


def part_one(parsed_data):
    # What we need to calculate is basically only a sum of offsets
    # So we just need to follow the offsets in the mappings
    locations = []
    num = len(parsed_data["seeds"])
    for i, seed in enumerate(parsed_data["seeds"]):
        location = seed
        for map in parsed_data["maps"].values():
            location = calc_new_val(location, map)
        locations.append(location)
    print(f"  Solution: {min(locations)}")


def calc_result_and_remainder(current, mapping):
    result = None
    remainder = []
    destination, start, rng = mapping
    stop = start + rng

    # We have 5 cases to handle across the boundaries:
    # No overlap
    if current[1] < start or stop <= current[0]:
        pass
    # Fully encapsulated
    elif start <= current[0] and current[1] < stop:
        offset = current[0] - start
        result = (destination + offset, destination + offset + current[1] - current[0])
    # Around start boundary
    elif current[0] < start <= current[1] < stop:
        offset = current[1] - start
        result = (destination, destination + offset)
        remainder.append((current[0], start - 1))
    # Around end boundary
    elif start <= current[0] < stop <= current[1]:
        offset = current[0] - start
        result = (destination + offset, destination + rng - 1)
        remainder.append((stop, current[1]))
    # Around both boundaries
    elif current[0] < start <= stop <= current[1]:
        result = (destination, destination + rng - 1)
        remainder.append((current[0], start - 1))
        remainder.append((stop, current[1]))

    return result, remainder


def part_two(parsed_data):
    seeds = parsed_data["seeds"]
    maps = list(parsed_data["maps"].values())

    locations = []
    seed_pairs = []
    for i in range(0, len(seeds), 2):
        seed_pairs.append((seeds[i], seeds[i] + seeds[i + 1]))

    for pair in seed_pairs:
        remainder = [pair]
        results = []

        for _map in maps:
            while remainder:
                current = remainder.pop()
                for mapping in _map:
                    result, _remainder = calc_result_and_remainder(current, mapping)
                    if result:
                        results.append(result)
                        remainder.extend(_remainder)
                        break
                else:  # In case nothing matched
                    results.append(current)
            remainder = results
            results = []

        locations.extend(remainder)

    print(f"  Solution: {min(i[0] for i in locations)}")


def solution(data):
    parsed = parse_data(data)
    print("Part 1:")
    part_one(parsed)
    print("Part 2:")
    part_two(parsed)
