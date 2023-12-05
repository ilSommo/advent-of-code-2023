"Day 1: Trebuchet?!"

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


SPELLED_DIGITS = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}


def main() -> None:
    """Solve day 1 problems."""
    with open("day_1_input.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve first problem.

    :param puzzle_input: Puzzle input
    """
    total = 0

    for line in puzzle_input:
        total += get_star_calibration_value(line)

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve second problem.

    :param puzzle_input: Puzzle input
    """
    total = 0

    for line in puzzle_input:
        line = replace_spelled_digits(line)
        total += get_star_calibration_value(line)

    print(f"Star 2: {total}")


def get_star_calibration_value(line: str) -> int:
    """Get calibration value from line.

    :param line: Line to process
    :return: Calibration value
    """
    all_digits = "".join(filter(lambda x: x.isdigit(), line))
    first_digit = all_digits[0]
    last_digit = all_digits[-1]
    two_digit_number = int(first_digit + last_digit)
    return two_digit_number


def replace_spelled_digits(line: str) -> str:
    """Replace spelled out digits with numbers.

    :param line: Line to process
    :return: Processed line
    """
    for spelled, digit in SPELLED_DIGITS.items():
        line = line.replace(spelled, digit)

    return line


if __name__ == "__main__":
    main()
