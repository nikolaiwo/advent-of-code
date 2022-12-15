import os

path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(path, "input.txt")

with open(input_path) as f:
    data = f.read()


def get_priority(item):
    """Get the priority of a character (item in rucksack)

    Use the ASCII table to convert to priority.
    a-z have priorities 1 through 26.
    A-Z have priorities 27 through 52.
    """
    if item.isupper():
        return 27 + (ord(item) - 65)
    else:
        return 1 + (ord(item) - 97)


################################### Part 1 ###################################

total_misplaced_priority = 0
for line, rucksack_items in enumerate(data.splitlines()):
    total_items = len(rucksack_items)
    # Get the items from the two compartments
    compartment_1 = rucksack_items[0:total_items // 2]
    compartment_2 = rucksack_items[total_items // 2:]

    # Convert to a set, to avoid counting twice for duplicate itens
    compartment_1 = set(compartment_1)
    compartment_2 = set(compartment_2)

    for item in compartment_1:
        if item in compartment_2:
            priority = get_priority(item)
            total_misplaced_priority += priority

print(
    f"Total priority of misplaced items in rucksaks: {total_misplaced_priority}"
)

################################### Part 2 ###################################

total_badge_priority = 0
rucksacks = data.splitlines()

for elf_number in range(0, len(rucksacks), 3):
    first_elf = set(rucksacks[elf_number])
    second_elf = set(rucksacks[elf_number + 1])
    third_elf = set(rucksacks[elf_number + 2])
    for item in first_elf:
        if item in second_elf and item in third_elf:
            total_badge_priority += get_priority(item)
print(f"Total priority of all badge items: {total_badge_priority}")
