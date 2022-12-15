import os

path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(path, "input.txt")

with open(input_path) as f:
    data = f.read()

# Create a list of the sum of calories carried by each elf
calories = []
for elf_data in data.strip().split('\n\n'):
    elf_calories = sum([int(cal) for cal in elf_data.split('\n')])
    calories.append(elf_calories)

# Part 1
print("Maximum number of calories carried by a single elf: {}".format(
    max(calories)))

# Part 2
top_three_elves = sorted(calories, reverse=True)[0:3]
print("Sum of the top three elves carrying the most calories: {}".format(
    sum(top_three_elves)))
