from operator import mul


def part_one(data):
    data = data.splitlines()
    times = [int(d) for d in data[0][5:].split()]
    distances = [int(d) for d in data[1][10:].split()]

    total = 1
    for i in range(len(times)):
        count = 0
        for j in range(times[i]):
            if j * (times[i] - j) > distances[i]:
                count += 1
        total *= count
    print(total)


def part_two(data):
    data = data.splitlines()
    time = int("".join([d for d in data[0][5:].split()]))
    distance = int("".join([d for d in data[1][10:].split()]))

    count = 0
    for j in range(time):
        if j * (time - j) > distance:
            count += 1
    print(count)


def solution(data):
    part_one(data)
    part_two(data)
