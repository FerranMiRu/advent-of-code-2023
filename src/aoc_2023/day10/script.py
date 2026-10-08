from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from functools import partial
from pathlib import Path


ROOT_DIR = Path(__file__).parent
NODE_TYPES = {
    "|": ["north", "south"],
    "-": ["east", "west"],
    "L": ["north", "east"],
    "J": ["north", "west"],
    "7": ["south", "west"],
    "F": ["south", "east"],
    ".": ["empty"],
    "S": ["start"],
}


@dataclass
class Node:
    x: int
    y: int
    distance: int = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.distance == other.distance

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x and self.y < other.y:
            return True

        return False

    def __hash__(self):
        return hash((self.x, self.y, self.distance))


def _worker(node_to_analyze, loop_nodes, map_matrix):
    amount_of_crosses = 0
    previous_loop_node_character = None
    for node in sorted(loop_nodes):
        current_loop_node_character = map_matrix[node.x][node.y]

        if (
            node.x > node_to_analyze.x
            and node.y == node_to_analyze.y
            and current_loop_node_character in ["S", "F", "L", "7", "J", "-"]
        ):
            if (current_loop_node_character == "L" and previous_loop_node_character == "7") or (
                current_loop_node_character == "J" and previous_loop_node_character == "F"
            ):
                continue

            amount_of_crosses += 1
            previous_loop_node_character = current_loop_node_character

    if amount_of_crosses % 2 != 0:
        return 1

    return 0


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    map_matrix = [[char for char in line] for line in input_lines]
    distance_matrix = [["." for _ in range(len(map_matrix[0]))] for _ in range(len(map_matrix))]

    for i in range(len(map_matrix)):
        for j in range(len(map_matrix[0])):
            if map_matrix[i][j] == "S":
                start_node = Node(i, j, 0)

    next_nodes = [start_node]

    while next_nodes:
        next_node = next_nodes.pop(0)

        if (
            isinstance(distance_matrix[next_node.x][next_node.y], int)
            and next_node.distance >= distance_matrix[next_node.x][next_node.y]
        ):
            continue

        distance_matrix[next_node.x][next_node.y] = next_node.distance
        next_node_type = map_matrix[next_node.x][next_node.y]

        if next_node_type == "S":
            # Look north
            if (
                next_node.x - 1 <= len(map_matrix)
                and "south" in NODE_TYPES[map_matrix[next_node.x - 1][next_node.y]]
            ):
                next_nodes.append(Node(next_node.x - 1, next_node.y, next_node.distance + 1))

            # Look south
            if (
                next_node.x + 1 >= 0
                and "north" in NODE_TYPES[map_matrix[next_node.x + 1][next_node.y]]
            ):
                next_nodes.append(Node(next_node.x + 1, next_node.y, next_node.distance + 1))

            # Look east
            if (
                next_node.y + 1 <= len(map_matrix[0])
                and "west" in NODE_TYPES[map_matrix[next_node.x][next_node.y + 1]]
            ):
                next_nodes.append(Node(next_node.x, next_node.y + 1, next_node.distance + 1))

            # Look west
            if (
                next_node.y - 1 >= 0
                and "east" in NODE_TYPES[map_matrix[next_node.x][next_node.y - 1]]
            ):
                next_nodes.append(Node(next_node.x, next_node.y - 1, next_node.distance + 1))

        else:
            for direction in NODE_TYPES[next_node_type]:
                if direction == "north" and next_node.x - 1 <= len(map_matrix):
                    next_nodes.append(Node(next_node.x - 1, next_node.y, next_node.distance + 1))

                if direction == "south" and next_node.x + 1 >= 0:
                    next_nodes.append(Node(next_node.x + 1, next_node.y, next_node.distance + 1))

                if direction == "east" and next_node.y + 1 <= len(map_matrix[0]):
                    next_nodes.append(Node(next_node.x, next_node.y + 1, next_node.distance + 1))

                if direction == "west" and next_node.y - 1 >= 0:
                    next_nodes.append(Node(next_node.x, next_node.y - 1, next_node.distance + 1))

    farthest_distance = 0
    for line in distance_matrix:
        for char in line:
            if char != "." and char > farthest_distance:
                farthest_distance = char

    print(farthest_distance)


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    map_matrix = [[char for char in line] for line in input_lines]
    distance_matrix = [["." for _ in range(len(map_matrix[0]))] for _ in range(len(map_matrix))]
    loop_nodes = set()

    for i in range(len(map_matrix)):
        for j in range(len(map_matrix[0])):
            if map_matrix[i][j] == "S":
                start_node = Node(i, j, 0)

    next_nodes = [start_node]

    while next_nodes:
        next_node = next_nodes.pop(0)

        if (
            isinstance(distance_matrix[next_node.x][next_node.y], int)
            and next_node.distance >= distance_matrix[next_node.x][next_node.y]
        ):
            continue

        loop_nodes.add(next_node)
        distance_matrix[next_node.x][next_node.y] = next_node.distance
        next_node_type = map_matrix[next_node.x][next_node.y]

        if next_node_type == "S":
            starting_connections = []
            # Look north
            if (
                next_node.x - 1 <= len(map_matrix)
                and "south" in NODE_TYPES[map_matrix[next_node.x - 1][next_node.y]]
            ):
                starting_connections.append("north")
                next_nodes.append(Node(next_node.x - 1, next_node.y))

            # Look south
            if (
                next_node.x + 1 >= 0
                and "north" in NODE_TYPES[map_matrix[next_node.x + 1][next_node.y]]
            ):
                starting_connections.append("south")
                next_nodes.append(Node(next_node.x + 1, next_node.y))

            # Look east
            if (
                next_node.y + 1 <= len(map_matrix[0])
                and "west" in NODE_TYPES[map_matrix[next_node.x][next_node.y + 1]]
            ):
                starting_connections.append("east")
                next_nodes.append(Node(next_node.x, next_node.y + 1))

            # Look west
            if (
                next_node.y - 1 >= 0
                and "east" in NODE_TYPES[map_matrix[next_node.x][next_node.y - 1]]
            ):
                starting_connections.append("west")
                next_nodes.append(Node(next_node.x, next_node.y - 1))

            for node_type, connections in NODE_TYPES.items():
                if set(starting_connections) == set(connections):
                    map_matrix[next_node.x][next_node.y] = node_type

        else:
            for direction in NODE_TYPES[next_node_type]:
                if direction == "north" and next_node.x - 1 <= len(map_matrix):
                    next_nodes.append(Node(next_node.x - 1, next_node.y))

                if direction == "south" and next_node.x + 1 >= 0:
                    next_nodes.append(Node(next_node.x + 1, next_node.y))

                if direction == "east" and next_node.y + 1 <= len(map_matrix[0]):
                    next_nodes.append(Node(next_node.x, next_node.y + 1))

                if direction == "west" and next_node.y - 1 >= 0:
                    next_nodes.append(Node(next_node.x, next_node.y - 1))

    nodes_to_process = []
    for i in range(len(map_matrix)):
        for j in range(len(map_matrix[0])):
            if Node(i, j) not in loop_nodes:
                nodes_to_process.append(Node(i, j))

    partial_worker = partial(_worker, loop_nodes=loop_nodes, map_matrix=map_matrix)
    with ProcessPoolExecutor() as executor:
        enclosed_tiles = sum(
            executor.map(
                partial_worker,
                nodes_to_process,
            )
        )

    print(enclosed_tiles)


if __name__ == "__main__":
    part1()
    part2()
