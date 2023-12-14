"Day 7: Camel Cards"

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"

from collections import Counter

CARDS_1 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

CARDS_2 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def main() -> None:
    """Solve day 7 puzzles."""
    with open("data/day_7_input.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle.

    :param puzzle_input: Puzzle input
    """
    hands = []

    for line in puzzle_input:
        cards, bid = line.split()
        hands.append((cards2value_1(cards), int(bid)))

    hands.sort(key=lambda x: x[0])

    total = 0

    for i, hand in enumerate(hands):
        total += hand[1] * (i + 1)

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle.

    :param puzzle_input: Puzzle input
    """
    hands = []

    for line in puzzle_input:
        cards, bid = line.split()
        hands.append((cards2value_2(cards), int(bid)))

    hands.sort(key=lambda x: x[0])

    total = 0

    for i, hand in enumerate(hands):
        total += hand[1] * (i + 1)

    print(f"Star 2: {total}")


# pylint: disable-next=too-many-return-statements
def cards2type_1(cards: str) -> int:
    """Convert cards to a hand type.

    :param cards: Cards to convert
    :return: Hand type value
    """
    counter = Counter(cards)
    values = sorted(counter.values(), reverse=True)

    if values[0] == 5:
        return 6
    if values[0] == 4:
        return 5
    if values[0] == 3 and values[1] == 2:
        return 4
    if values[0] == 3:
        return 3
    if values[0] == values[1] == 2:
        return 2
    if values[0] == 2:
        return 1
    return 0


# pylint: disable-next=too-many-return-statements
def cards2type_2(cards: str) -> int:
    """Convert cards to a hand type.

    :param cards: Cards to convert
    :return: Hand type value
    """
    counter = Counter(cards)
    jokers = counter["J"]
    counter["J"] = 0
    values = sorted(counter.values(), reverse=True)

    if jokers == 5 or values[0] + jokers == 5:
        return 6
    if values[0] + jokers == 4:
        return 5
    if values[0] + jokers == 3 and values[1] == 2:
        return 4
    if values[0] + jokers == 3:
        return 3
    if values[0] == values[1] == 2:
        return 2
    if values[0] + jokers == 2:
        return 1
    return 0


def cards2value_1(cards: str) -> int:
    """Convert cards to a hand value.

    :param cards: Cards to convert
    :return: Hand value
    """
    hand_type = cards2type_1(cards)
    card0 = CARDS_1[cards[0]]
    card1 = CARDS_1[cards[1]]
    card2 = CARDS_1[cards[2]]
    card3 = CARDS_1[cards[3]]
    card4 = CARDS_1[cards[4]]

    return int(
        hand_type * 1e10
        + card0 * 1e8
        + card1 * 1e6
        + card2 * 1e4
        + card3 * 1e2
        + card4
    )


def cards2value_2(cards: str) -> int:
    """Convert cards to a hand value.

    :param cards: Cards to convert
    :return: Hand value
    """
    hand_type = cards2type_2(cards)
    card0 = CARDS_2[cards[0]]
    card1 = CARDS_2[cards[1]]
    card2 = CARDS_2[cards[2]]
    card3 = CARDS_2[cards[3]]
    card4 = CARDS_2[cards[4]]

    return int(
        hand_type * 1e10
        + card0 * 1e8
        + card1 * 1e6
        + card2 * 1e4
        + card3 * 1e2
        + card4
    )


if __name__ == "__main__":
    main()
