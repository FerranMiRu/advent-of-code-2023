from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path


ROOT_DIR = Path(__file__).parent


@dataclass
class Galaxy:
    id: int
    x: int
    y: int

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def expanded_distance(self, other, empty_rows, empty_columns, expansion_rate):
        x_expansion = 0
        for column in empty_columns:
            if self.x < column < other.x or other.x < column < self.x:
                x_expansion += 1

        y_expansion = 0
        for row in empty_rows:
            if self.y < row < other.y or other.y < row < self.y:
                y_expansion += 1

        return (
            abs(self.x - other.x)
            + (x_expansion * (expansion_rate - 1))
            + abs(self.y - other.y)
            + (y_expansion * (expansion_rate - 1))
        )


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]
    galaxies_map = [list(line) for line in input_lines]

    expanded_galaxies_map = []
    for row in galaxies_map:
        expanded_galaxies_map.append(deepcopy(row))

        if set(row) == {"."}:
            expanded_galaxies_map.append(deepcopy(row))

    expanded_columns = 0
    for j in range(len(galaxies_map[0])):
        empty_column = True

        for row in galaxies_map:
            if row[j] != ".":
                empty_column = False
                break

        if empty_column:
            expanded_columns += 1
            for row in expanded_galaxies_map:
                row.insert(j + expanded_columns, ".")

    galaxies = []
    for i, row in enumerate(expanded_galaxies_map):
        for j, column in enumerate(row):
            if column == "#":
                galaxies.append(Galaxy(len(galaxies) + 1, j, i))

    total_distance = 0
    for i, galaxy in enumerate(galaxies):
        for other_galaxy in galaxies[i + 1 :]:
            total_distance += galaxy.distance(other_galaxy)

    print(total_distance)


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    expansion_rate = 1000000
    input_lines = [line.strip() for line in input_lines]
    galaxies_map = [list(line) for line in input_lines]

    empty_rows = []
    for i in range(len(galaxies_map)):
        if set(galaxies_map[i]) == {"."}:
            empty_rows.append(i)

    empty_columns = []
    for j in range(len(galaxies_map[0])):
        is_empty_column = True

        for row in galaxies_map:
            if row[j] != ".":
                is_empty_column = False
                break

        if is_empty_column:
            empty_columns.append(j)

    galaxies = []
    for i, row in enumerate(galaxies_map):
        for j, column in enumerate(row):
            if column == "#":
                galaxies.append(Galaxy(len(galaxies) + 1, j, i))

    total_distance = 0
    for i, galaxy in enumerate(galaxies):
        for other_galaxy in galaxies[i + 1 :]:
            total_distance += galaxy.expanded_distance(
                other_galaxy, empty_rows, empty_columns, expansion_rate
            )

    print(total_distance)


if __name__ == "__main__":
    part1()
    part2()
