from pathlib import Path


ROOT_DIR = Path(__file__).parents[2]
COUNTER = 0


def count_combinations(springs: str, groups: tuple) -> int:
    global COUNTER
    COUNTER += 1

    combinations = 0

    next_question_mark = springs.find("?")

    if next_question_mark == -1:
        current_groups = [g for g in map(len, springs.split(".")) if g > 0]
        is_valid_combination = current_groups == list(groups)

        return 1 if is_valid_combination else 0
    else:
        combinations += count_combinations(springs.replace("?", ".", 1), groups)
        combinations += count_combinations(springs.replace("?", "#", 1), groups)

    return combinations


def part1():
    with open(ROOT_DIR / "2023" / "day12" / "input.txt") as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]
    total_combinations = 0

    for line in input_lines:
        springs, groups = line.split(" ")
        groups = tuple(map(int, groups.split(",")))

        total_combinations += count_combinations(springs, groups)

    print(total_combinations)
    print(f"{COUNTER = }")


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
