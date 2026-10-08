import math
from pathlib import Path


ROOT_DIR = Path(__file__).parent


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    total = 0
    for line in input_lines:
        sequence = [int(i) for i in line.split(" ")]
        binomial_length = len(sequence) - 1
        binomial_coeffs = [
            math.prod([binomial_length - j for j in range(i)]) / math.factorial(i)
            for i in range(binomial_length)
        ]

        prediction = 0
        for i, coeff in enumerate(reversed(binomial_coeffs), 1):
            prediction += math.pow(-1, i + 1) * coeff * sequence[-i]

        total += prediction

    print(total)


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    total = 0
    for line in input_lines:
        sequence = [int(i) for i in line.split(" ")]
        binomial_length = len(sequence) - 1
        binomial_coeffs = [
            math.prod([binomial_length - j for j in range(i)]) / math.factorial(i)
            for i in range(binomial_length)
        ]

        prediction = 0
        for i, coeff in enumerate(reversed(binomial_coeffs)):
            prediction += math.pow(-1, i) * coeff * sequence[i]

        total += prediction

    print(total)


if __name__ == "__main__":
    part1()
    part2()
