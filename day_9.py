"""Day 9: Mirage Maintenance."""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


def main() -> None:
    """Solve day 9 puzzles."""
    with open("data/day_9_input.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle."""
    total = 0
    for line in puzzle_input:
        sequence = list(map(int, line.split()))
        total += estrapolate(sequence)

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle."""
    total = 0
    for line in puzzle_input:
        sequence = list(map(int, line.split()))
        total += backward_estrapolate(sequence)

    print(f"Star 2: {total}")


def estrapolate(sequence: list[int]) -> int:
    """Estrapolate next element from list."""
    differences = []
    for i, _ in enumerate(sequence[:-1]):
        differences.append(sequence[i + 1] - sequence[i])

    if any(differences):
        return sequence[-1] + estrapolate(differences)

    return sequence[-1]


def backward_estrapolate(sequence: list[int]) -> int:
    """Estrapolate previous element from list."""
    differences = []
    for i, _ in enumerate(sequence[:-1]):
        differences.append(sequence[i + 1] - sequence[i])

    if any(differences):
        return sequence[0] - backward_estrapolate(differences)

    return sequence[0]


if __name__ == "__main__":
    main()
