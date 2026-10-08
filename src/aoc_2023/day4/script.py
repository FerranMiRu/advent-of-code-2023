import math
from collections import defaultdict
from pathlib import Path


ROOT_DIR = Path(__file__).parent


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.split(":")[-1].strip() for line in input_lines]
    total = 0

    for line in input_lines:
        winning_numbers_string, actual_numbers_string = line.split(" | ")
        winning_numbers = set([int(num) for num in winning_numbers_string.split(" ") if num])
        actual_numbers = [int(num) for num in actual_numbers_string.split(" ") if num]

        mutual_numbers = winning_numbers.intersection(actual_numbers)

        if len(mutual_numbers) != 0:
            total += math.pow(2, (len(mutual_numbers) - 1))

    print(total)


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.split(":")[-1].strip() for line in input_lines]
    scratch_cards = defaultdict(lambda: 1)

    for i, line in enumerate(input_lines, 1):
        winning_numbers_string, actual_numbers_string = line.split(" | ")
        winning_numbers = set([int(num) for num in winning_numbers_string.split(" ") if num])
        actual_numbers = [int(num) for num in actual_numbers_string.split(" ") if num]

        mutual_numbers = len(winning_numbers.intersection(actual_numbers))
        amount_current_card = scratch_cards[i]

        for card_num in range(i + 1, min(i + 1 + mutual_numbers, len(input_lines) + 1)):
            scratch_cards[card_num] += amount_current_card

    print(sum(scratch_cards.values()))


if __name__ == "__main__":
    part1()
    part2()
