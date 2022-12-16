import os

path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(path, "input.txt")

with open(input_path) as f:
    data = f.read()

################################### Part 1 ###################################

fully_contained_ranges = 0
partial_overlap = 0
for line in data.splitlines():
    pairs = []
    for pair in line.split(','):
        start, stop = pair.split('-')
        pairs.append((int(start), int(stop)))

    # If one pair is contained in the other, we have a fully contained match
    if ((pairs[0][0] >= pairs[1][0] and pairs[0][1] <= pairs[1][1])
            or (pairs[1][0] >= pairs[0][0] and pairs[1][1] <= pairs[0][1])):
        fully_contained_ranges += 1

    # If there are any overlaps at all (part two)
    range_1 = range(pairs[0][0], pairs[0][1] + 1)
    range_2 = range(pairs[1][0], pairs[1][1] + 1)
    if ((pairs[0][0] in range_2 or pairs[0][1] in range_2)
            or (pairs[1][0] in range_1 or pairs[1][1] in range_1)):
        partial_overlap += 1
print(
    f"Number of ranges that fully contain the other: {fully_contained_ranges}")

print(f"Partially overlapping ranges: {partial_overlap}")

################################### Part 2 ###################################
