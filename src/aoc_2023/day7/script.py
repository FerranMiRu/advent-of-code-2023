from functools import cmp_to_key, partial
from pathlib import Path


ROOT_DIR = Path(__file__).parent
POKER_HANDS = {
    "FIVE_OF_A_KIND": 7,
    "FOUR_OF_A_KIND": 6,
    "FULL_HOUSE": 5,
    "THREE_OF_A_KIND": 4,
    "TWO_PAIR": 3,
    "ONE_PAIR": 2,
    "HIGH_CARD": 1,
}


def hand_compare(hand1, hand2, card_order):
    if POKER_HANDS[hand1["type"]] > POKER_HANDS[hand2["type"]]:
        return 1
    elif POKER_HANDS[hand1["type"]] < POKER_HANDS[hand2["type"]]:
        return -1
    else:
        for card1, card2 in zip(hand1["hand"], hand2["hand"], strict=True):
            if card_order.index(card1) > card_order.index(card2):
                return -1
            elif card_order.index(card1) < card_order.index(card2):
                return 1

        return 0


def part1():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip().split(" ") for line in input_lines]

    hands = []
    for h, b in input_lines:
        different_cards = list(set(h))

        if len(different_cards) == 1:
            hand_type = "FIVE_OF_A_KIND"

        elif len(different_cards) == 2:
            if h.count(different_cards[0]) == 4 or h.count(different_cards[1]) == 4:
                hand_type = "FOUR_OF_A_KIND"
            else:
                hand_type = "FULL_HOUSE"

        elif len(different_cards) == 3:
            if (
                h.count(different_cards[0]) == 3
                or h.count(different_cards[1]) == 3
                or h.count(different_cards[2]) == 3
            ):
                hand_type = "THREE_OF_A_KIND"
            else:
                hand_type = "TWO_PAIR"

        elif len(different_cards) == 4:
            hand_type = "ONE_PAIR"

        else:
            hand_type = "HIGH_CARD"

        hands.append({"hand": h, "bid": int(b), "type": hand_type})

    part1_hand_compare = partial(
        hand_compare, card_order=["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    )

    hands.sort(key=cmp_to_key(part1_hand_compare))

    print(sum([i * hand["bid"] for i, hand in enumerate(hands, start=1)]))


def part2():
    with (ROOT_DIR / "input.txt").open() as f:
        input_lines = f.readlines()

    input_lines = [line.strip().split(" ") for line in input_lines]

    hands = []
    for h, b in input_lines:
        different_cards = list(set(h))

        if len(different_cards) == 1:
            hand_type = "FIVE_OF_A_KIND"

        elif len(different_cards) == 2:
            if "J" in different_cards:
                hand_type = "FIVE_OF_A_KIND"
            elif h.count(different_cards[0]) == 4 or h.count(different_cards[1]) == 4:
                hand_type = "FOUR_OF_A_KIND"
            else:
                hand_type = "FULL_HOUSE"

        elif len(different_cards) == 3:
            if "J" in different_cards:
                if h.count("J") == 2 or any([h.count(card) == 3 for card in different_cards]):
                    hand_type = "FOUR_OF_A_KIND"
                else:
                    hand_type = "FULL_HOUSE"
            elif (
                h.count(different_cards[0]) == 3
                or h.count(different_cards[1]) == 3
                or h.count(different_cards[2]) == 3
            ):
                hand_type = "THREE_OF_A_KIND"
            else:
                hand_type = "TWO_PAIR"

        elif len(different_cards) == 4:
            if "J" in different_cards:
                hand_type = "THREE_OF_A_KIND"
            else:
                hand_type = "ONE_PAIR"

        else:
            if "J" in different_cards:
                hand_type = "ONE_PAIR"
            else:
                hand_type = "HIGH_CARD"

        hands.append({"hand": h, "bid": int(b), "type": hand_type})

    part1_hand_compare = partial(
        hand_compare, card_order=["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    )

    hands.sort(key=cmp_to_key(part1_hand_compare))

    print(sum([i * hand["bid"] for i, hand in enumerate(hands, start=1)]))


if __name__ == "__main__":
    part1()
    part2()
