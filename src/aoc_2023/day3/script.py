from collections import defaultdict
from pathlib import Path


ROOT_DIR = Path(__file__).parent


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    current_number = ""
    is_adjacent_to_symbol = False
    total = 0

    for row, line in enumerate(input_lines):
        for column, character in enumerate(line):
            if character.isdigit():
                current_number += character

                if not is_adjacent_to_symbol:
                    for i in range(max(row - 1, 0), min(row + 2, len(input_lines))):
                        for j in range(max(column - 1, 0), min(column + 2, len(line))):
                            if i == row and j == column:
                                continue

                            if not input_lines[i][j].isdigit() and not input_lines[i][j] == ".":
                                is_adjacent_to_symbol = True

            elif not character.isdigit() and current_number:
                if is_adjacent_to_symbol:
                    total += int(current_number)

                current_number = ""
                is_adjacent_to_symbol = False

    print(total)


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    current_number = ""
    adjacent_to_gear = ""
    gears = defaultdict(list)
    total = 0

    for row, line in enumerate(input_lines):
        for column, character in enumerate(line):
            if character.isdigit():
                current_number += character

                if not adjacent_to_gear:
                    for i in range(max(row - 1, 0), min(row + 2, len(input_lines))):
                        for j in range(max(column - 1, 0), min(column + 2, len(line))):
                            if i == row and j == column:
                                continue

                            if input_lines[i][j] == "*":
                                adjacent_to_gear = f"{i}|{j}"

            elif not character.isdigit() and current_number:
                if adjacent_to_gear:
                    gears[adjacent_to_gear].append(int(current_number))

                current_number = ""
                adjacent_to_gear = None

    for _, numbers in gears.items():
        if len(numbers) == 2:
            total += numbers[0] * numbers[1]

    print(total)


if __name__ == "__main__":
    part1()
    part2()
