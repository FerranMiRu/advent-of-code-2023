import math
from pathlib import Path


ROOT_DIR = Path(__file__).parent


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    instructions = list(input_lines[0])
    nodes = {}

    for line in input_lines[2:]:
        line = line.split("=")
        node = line[0].strip()
        values = [i.strip() for i in line[1].replace("(", "").replace(")", "").split(",")]

        nodes[node] = {"L": values[0], "R": values[1]}

    total_steps = 0

    current_node = "AAA"
    i = 0
    while current_node != "ZZZ":
        current_node = nodes[current_node][instructions[i]]

        i += 1
        if i == len(instructions):
            i = 0

        total_steps += 1

    print(total_steps)


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    instructions = list(input_lines[0])
    nodes = {}

    for line in input_lines[2:]:
        line = line.split("=")
        node = line[0].strip()
        values = [i.strip() for i in line[1].replace("(", "").replace(")", "").split(",")]

        nodes[node] = {"L": values[0], "R": values[1]}

    current_nodes = [node_name for node_name in nodes.keys() if node_name[-1] == "A"]
    steps_per_path = []
    i = 0
    for current_node in current_nodes:
        total_steps = 0

        while current_node[-1] != "Z":
            current_node = nodes[current_node][instructions[i]]

            i += 1
            if i == len(instructions):
                i = 0

            total_steps += 1

        steps_per_path.append(total_steps)

    print(math.lcm(*steps_per_path))


if __name__ == "__main__":
    part1()
    part2()
