from collections import defaultdict
from pathlib import Path


ROOT_DIR = Path(__file__).parent
DIGIT_TO_NAME = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [i.strip() for i in input_lines]
    total = 0

    for line in input_lines:
        line_digits = []

        for character in line:
            if character.isdigit():
                line_digits.append(character)

        total += int(f"{line_digits[0]}{line_digits[-1]}")

    print(total)


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [i.strip() for i in input_lines]
    total = 0

    for line in input_lines:
        line_digits = defaultdict(set)

        for digit in DIGIT_TO_NAME.keys():
            line_digits[digit].add(line.find(str(digit)))
            line_digits[digit].add(line.rfind(str(digit)))
            line_digits[digit].add(line.find(DIGIT_TO_NAME[digit]))
            line_digits[digit].add(line.rfind(DIGIT_TO_NAME[digit]))

        first_digit = 0
        first_position = 10000000000000
        last_digit = 0
        last_position = -1

        for digit, positions in line_digits.items():
            for position in positions:
                if position != -1 and position < first_position:
                    first_digit = digit
                    first_position = position

                if position != -1 and position > last_position:
                    last_digit = digit
                    last_position = position

        total += int(f"{first_digit}{last_digit}")

    print(total)


if __name__ == "__main__":
    part1()
    part2()
