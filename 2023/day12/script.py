from copy import deepcopy
from dataclasses import dataclass
from itertools import permutations
from pathlib import Path


ROOT_DIR = Path(__file__).parents[2]


@dataclass
class SpringRow:
    springs_status: str
    contiguous_damaged_springs: list[int]
    amount_combinations: int = 0


def part1():
    with open(ROOT_DIR / "2023" / "day12" / "input.txt") as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    spring_rows: list[SpringRow] = []
    for line in input_lines:
        spring_status, contiguous_damaged_springs = line.split(" ")
        spring_rows.append(
            SpringRow(
                springs_status=spring_status,
                contiguous_damaged_springs=[int(x) for x in contiguous_damaged_springs.split(",")],
            )
        )

    for i, spring_row in enumerate(spring_rows, 1):
        amount_question_marks = spring_row.springs_status.count("?")
        amount_hashtags = spring_row.springs_status.count("#")

        required_dots_in_question_marks = (
            sum(spring_row.contiguous_damaged_springs) - amount_hashtags
        )
        required_hashtags_in_question_marks = (
            amount_question_marks - required_dots_in_question_marks
        )

        elements_to_combine = ["#"] * required_dots_in_question_marks + [
            "."
        ] * required_hashtags_in_question_marks

        permutations_list = list(permutations(elements_to_combine))
        permutations_set = set(permutations_list)
        print(f"{i} / {len(spring_rows)} ==> {len(permutations_set)}", end="\r")

        for permutation in permutations_set:
            new_status = deepcopy(spring_row.springs_status)

            for character in permutation:
                new_status = new_status.replace("?", character, 1)

            new_contiguous_damaged_springs = [len(i) for i in new_status.split(".")]

            while 0 in new_contiguous_damaged_springs:
                new_contiguous_damaged_springs.remove(0)

            if new_contiguous_damaged_springs == spring_row.contiguous_damaged_springs:
                spring_row.amount_combinations += 1

    total_combinations = 0
    for spring_row in spring_rows:
        total_combinations += spring_row.amount_combinations

    print()
    print(total_combinations)


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
