from pathlib import Path


ROOT_DIR = Path(__file__).parents[2]
COUNTER = 0


def count_combinations(spring_status, contiguous_damaged_springs) -> int:
    global COUNTER
    COUNTER += 1
    if spring_status == "":
        return 1 if contiguous_damaged_springs == () else 0

    if contiguous_damaged_springs == ():
        return 0 if "#" in spring_status else 1

    combinations = 0

    if spring_status[0] in [".", "?"]:
        combinations += count_combinations(spring_status[1:], contiguous_damaged_springs)

    if spring_status[0] in ["#", "?"]:
        if (
            contiguous_damaged_springs[0] <= len(spring_status)
            and "." not in spring_status[: contiguous_damaged_springs[0]]
            and (
                contiguous_damaged_springs[0] == len(spring_status)
                or spring_status[contiguous_damaged_springs[0]] != "#"
            )
        ):
            combinations += count_combinations(
                spring_status[contiguous_damaged_springs[0] + 1 :], contiguous_damaged_springs[1:]
            )

    return combinations


def part1():
    global COUNTER
    with open(ROOT_DIR / "2023" / "day12" / "input.txt") as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    total_combinations = 0
    for line in input_lines:
        spring_status, contiguous_damaged_springs = line.split(" ")
        contiguous_damaged_springs = tuple(map(int, contiguous_damaged_springs.split(",")))

        total_combinations += count_combinations(spring_status, contiguous_damaged_springs)

    print(total_combinations)
    print(f"{COUNTER = }")


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
