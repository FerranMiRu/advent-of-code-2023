from pathlib import Path


ROOT_DIR = Path(__file__).parent


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [i.strip() for i in input_lines]
    total = 0

    for line in input_lines:
        game_id, hands = line.split(":")

        game_id = int(game_id.split(" ")[1])
        hands = hands.split(";")

        for hand in hands:
            cubes = hand.split(",")

            for amount_color in cubes:
                amount, color = amount_color.split(" ")[1:]
                amount = int(amount)

                if "red" in color:
                    if amount > 12:
                        game_id = 0

                elif "blue" in color:
                    if amount > 14:
                        game_id = 0

                elif "green" in color:
                    if amount > 13:
                        game_id = 0

        total += game_id

    print(total)


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [i.strip() for i in input_lines]
    total = 0

    for line in input_lines:
        game_id, hands = line.split(":")

        hands = hands.split(";")
        red_amount = 0
        blue_amount = 0
        green_amount = 0

        for hand in hands:
            cubes = hand.split(",")

            for amount_color in cubes:
                amount, color = amount_color.split(" ")[1:]
                amount = int(amount)

                if "red" in color:
                    if amount > red_amount:
                        red_amount = amount

                elif "blue" in color:
                    if amount > blue_amount:
                        blue_amount = amount

                elif "green" in color:
                    if amount > green_amount:
                        green_amount = amount

        total += red_amount * blue_amount * green_amount

    print(total)


if __name__ == "__main__":
    part1()
    part2()
