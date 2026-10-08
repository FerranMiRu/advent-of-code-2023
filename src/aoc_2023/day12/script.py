from functools import cache
from pathlib import Path


ROOT_DIR = Path(__file__).parent


def solve_line(springs, groups):
    @cache
    def dp(s_idx, g_idx):
        if g_idx == len(groups):
            if "#" in springs[s_idx:]:
                return 0
            return 1

        if s_idx >= len(springs):
            return 0

        res = 0
        char = springs[s_idx]
        current_group_size = groups[g_idx]

        if char in ".?":
            res += dp(s_idx + 1, g_idx)

        if char in "#?":
            end_group_idx = s_idx + current_group_size

            if end_group_idx <= len(springs):
                if "." not in springs[s_idx:end_group_idx]:
                    if end_group_idx == len(springs) or springs[end_group_idx] != "#":
                        res += dp(end_group_idx + 1, g_idx + 1)

        return res

    return dp(0, 0)


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        lines = f.read().splitlines()

    total = 0
    for line in lines:
        if not line.strip():
            continue

        parts = line.split()
        springs = parts[0]
        groups = tuple(map(int, parts[1].split(",")))
        total += solve_line(springs, groups)

    print(total)


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        lines = f.read().splitlines()

    total = 0
    for line in lines:
        if not line.strip():
            continue

        parts = line.split()
        springs = parts[0]
        groups = tuple(map(int, parts[1].split(",")))

        springs = "?".join([springs] * 5)
        groups = groups * 5

        total += solve_line(springs, groups)

    print(total)


if __name__ == "__main__":
    part1()
    part2()
