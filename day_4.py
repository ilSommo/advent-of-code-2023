"Day 4: Scratchcards"

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


from typing import Optional


def main() -> None:
    """Solve day 4 puzzles."""
    with open("day_4_input.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve first puzzle.

    :param puzzle_input: Puzzle input
    """
    total = 0

    for line in puzzle_input:
        winning_numbers, my_numbers = parse_line(line)
        value = 0
        for number in my_numbers:
            if number in winning_numbers:
                value = max(1, value * 2)
        total += value

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve second puzzle.

    :param puzzle_input: Puzzle input
    """
    scratchcards = dict.fromkeys(list(range(1, len(puzzle_input) + 1)), 1)

    for scratchcard, quantity in scratchcards.items():
        winning_numbers, my_numbers = parse_line(puzzle_input[scratchcard - 1])
        index = 1
        for number in my_numbers:
            if number in winning_numbers:
                scratchcards[scratchcard + index] += quantity
                index += 1

    total = sum(scratchcards.values())

    print(f"Star 2: {total}")


def parse_line(line: str) -> tuple[set[int], set[int]]:
    """Parse a line of numbers.

    :param line: Input line
    :return: Winning numbers and my numbers
    """
    winning_str, my_str = line.strip().split(": ")[1].split(" | ")
    winning_numbers = set(filter(None, winning_str.split(" ")))
    my_numbers = set(filter(None, my_str.split(" ")))
    return winning_numbers, my_numbers


if __name__ == "__main__":
    main()
