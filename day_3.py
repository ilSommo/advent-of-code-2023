"""Day 3: Gear Ratios."""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"

from typing import Optional


def main() -> None:
    """Solve day 3 puzzles."""
    with open("data/day_3_input.txt", encoding="ascii") as input_file:
        raw_input = input_file.readlines()

    puzzle_input = pad_input(raw_input)

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle.

    :param puzzle_input: Puzzle input
    """
    total = 0

    for i, line in enumerate(puzzle_input):
        for j, char in enumerate(line):
            if char.isdigit() and not line[j - 1].isdigit():
                number = get_number(line=line, j=j)
                total += get_value(puzzle_input, number, i, j)

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle.

    :param puzzle_input: Puzzle input
    """
    total = 0

    gears: dict[tuple[int, int], list[int]] = {}

    for i, line in enumerate(puzzle_input):
        for j, char in enumerate(line):
            if char.isdigit() and not line[j - 1].isdigit():
                number = get_number(line=line, j=j)
                gear = get_gear(puzzle_input, number, i, j)
                if gear:
                    gears.setdefault(gear, []).append(int(number))

    for gear, numbers in gears.items():
        if len(numbers) == 2:
            total += numbers[0] * numbers[1]

    print(f"Star 2: {total}")


def get_gear(
    puzzle_input: list[str], number: str, i: int, j: int
) -> Optional[tuple[int, int]]:
    """Get coordinate of gear.

    :param puzzle_input: Puzzle input
    :param number: Number
    :param i: Number start line
    :param j: Number start column
    :return: Coordinates if gear, None otherwise
    """
    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + len(number) + 1):
            if puzzle_input[ii][jj] == "*":
                return (ii, jj)

    return None


def get_number(line: str, j: int) -> str:
    """Get complete number.

    :param line: Line
    :param j: Number start index
    :return: Complete number
    """
    number = ""
    k = 0
    while line[j + k].isdigit():
        number += line[j + k]
        k += 1

    return number


def get_value(puzzle_input: list[str], number: str, i: int, j: int) -> int:
    """Get value of number.

    :param puzzle_input: Puzzle input
    :param number: Number
    :param i: Number start line
    :param j: Number start column
    :return: Number if valid, 0 otherwise
    """
    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + len(number) + 1):
            if (
                not puzzle_input[ii][jj].isdigit()
                and puzzle_input[ii][jj] != "."
            ):
                return int(number)

    return 0


def pad_input(raw_input: list[str]) -> list[str]:
    """Pad input.

    :param raw_input: Puzzle input
    :return: Padded input
    """
    matrix_input = []

    matrix_input.append("." * (len(raw_input[0]) + 1))
    for line in raw_input:
        matrix_input.append("." + line.strip() + ".")
    matrix_input.append("." * (len(raw_input[0]) + 1))

    return matrix_input


if __name__ == "__main__":
    main()
