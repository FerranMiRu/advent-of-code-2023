from pathlib import Path


ROOT_DIR = Path(__file__).parent


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    race_times = [int(i) for i in input_lines[0].split(":")[1].strip().split(" ") if i]
    race_distances = [int(i) for i in input_lines[1].split(":")[1].strip().split(" ") if i]

    race_possible_ways_to_win = []

    for time, distance in zip(race_times, race_distances, strict=True):
        ways_to_win = 0

        for t in range(time):
            d = (time - t) * t

            if d > distance:
                ways_to_win += 1

        race_possible_ways_to_win.append(ways_to_win)

    total = 1
    for a in race_possible_ways_to_win:
        total *= a

    print(total)


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    time = int("".join(input_lines[0].split(":")[1].strip().split(" ")))
    distance = int("".join(input_lines[1].split(":")[1].strip().split(" ")))

    total = 0

    for t in range(time):
        d = (time - t) * t

        if d > distance:
            total += 1

    print(total)


if __name__ == "__main__":
    part1()
    part2()
