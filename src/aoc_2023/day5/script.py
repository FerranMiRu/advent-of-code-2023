from collections import defaultdict
from pathlib import Path


ROOT_DIR = Path(__file__).parent


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]
    seeds = [int(i) for i in input_lines.pop(0).split(":")[1].strip().split(" ")]
    maps = defaultdict(list)
    maps_order = []
    current_map_name = ""

    for line in input_lines:
        if ":" in line:
            current_map_name = line.split(" ")[0]
            maps_order.append(current_map_name)
        elif line:
            current_ranges = [int(i) for i in line.split(" ")]
            maps[current_map_name].append(
                {
                    "source": [
                        current_ranges[1],
                        current_ranges[1] + current_ranges[2] - 1,
                    ],
                    "destination": [
                        current_ranges[0],
                        current_ranges[0] + current_ranges[2] - 1,
                    ],
                }
            )

    closest_location = None

    for seed in seeds:
        next_category = seed

        for current_map_name in maps_order:
            current_category = next_category

            for current_range in maps[current_map_name]:
                if current_range["source"][0] <= current_category <= current_range["source"][1]:
                    next_category = (current_category - current_range["source"][0]) + current_range[
                        "destination"
                    ][0]
                    break

        if closest_location is None or closest_location > next_category:
            closest_location = next_category

    print(closest_location)


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip() for line in input_lines]

    seeds = [int(i) for i in input_lines.pop(0).split(":")[1].strip().split(" ")]
    seeds = [[seeds[i], seeds[i] + seeds[i + 1] - 1] for i in range(0, len(seeds), 2)]

    maps = defaultdict(list)
    maps_order = []
    current_map_name = ""

    for line in input_lines:
        if ":" in line:
            current_map_name = line.split(" ")[0]
            maps_order.append(current_map_name)
        elif line:
            current_ranges = [int(i) for i in line.split(" ")]
            maps[current_map_name].append(
                {
                    "source": [
                        current_ranges[1],
                        current_ranges[1] + current_ranges[2] - 1,
                    ],
                    "destination": [
                        current_ranges[0],
                        current_ranges[0] + current_ranges[2] - 1,
                    ],
                }
            )

    location_ranges = []

    for seed_range in seeds:
        next_ranges = [seed_range]

        for current_map_name in maps_order:
            current_ranges = next_ranges
            next_ranges = []

            while current_ranges:
                current_range = current_ranges.pop(0)

                for category_range in maps[current_map_name]:
                    if (
                        current_range[1] < category_range["source"][0]
                        or current_range[0] > category_range["source"][1]
                    ):
                        continue

                    elif (
                        current_range[0] >= category_range["source"][0]
                        and current_range[1] <= category_range["source"][1]
                    ):
                        next_ranges.append(
                            [
                                (current_range[0] - category_range["source"][0])
                                + category_range["destination"][0],
                                (current_range[1] - category_range["source"][0])
                                + category_range["destination"][0],
                            ]
                        )
                        current_range = []
                        break

                    elif (
                        current_range[0] < category_range["source"][0]
                        and current_range[1] <= category_range["source"][1]
                    ):
                        next_ranges.append(
                            [
                                category_range["destination"][0],
                                (current_range[1] - category_range["source"][0])
                                + category_range["destination"][0],
                            ]
                        )
                        current_range = [
                            current_range[0],
                            category_range["source"][0] - 1,
                        ]

                    elif (
                        current_range[0] >= category_range["source"][0]
                        and current_range[1] > category_range["source"][1]
                    ):
                        next_ranges.append(
                            [
                                (current_range[0] - category_range["source"][0])
                                + category_range["destination"][0],
                                category_range["destination"][1],
                            ]
                        )
                        current_range = [
                            category_range["source"][1] + 1,
                            current_range[1],
                        ]

                    elif (
                        current_range[0] < category_range["source"][0]
                        and current_range[1] > category_range["source"][1]
                    ):
                        next_ranges.append(
                            [
                                category_range["destination"][0],
                                category_range["destination"][1],
                            ]
                        )
                        current_range = [
                            current_range[0],
                            category_range["source"][0] - 1,
                        ]
                        current_ranges.append(
                            [
                                category_range["source"][1] + 1,
                                current_range[1],
                            ]
                        )

                if current_range:
                    next_ranges.append(current_range)

        location_ranges.extend(next_ranges)

    print(min([i[0] for i in location_ranges]))


if __name__ == "__main__":
    part1()
    part2()
