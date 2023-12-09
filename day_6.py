"Day 6: Wait For It"

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


import math


def main() -> None:
    """Solve day 6 puzzles."""
    with open("data/day_6_input.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle.

    :param puzzle_input: Puzzle input
    """
    races = get_races(puzzle_input)

    total = 1

    for race in races:
        x0, x1 = solve_inequality(race)
        if x0 == int(x0):
            x0 += 1
        if x1 == int(x1):
            x1 -= 1
        total *= math.floor(x1) - math.ceil(x0) + 1

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle.

    :param puzzle_input: Puzzle input
    """
    race = get_race(puzzle_input)

    x0, x1 = solve_inequality(race)
    if x0 == int(x0):
        x0 += 1
    if x1 == int(x1):
        x1 -= 1
    ways_to_win = math.floor(x1) - math.ceil(x0) + 1

    print(f"Star 2: {ways_to_win}")


def get_race(puzzle_input: list[str]) -> tuple[int, int]:
    """Get race from puzzle input.

    :param puzzle_input: Puzzle input
    :return: (time, distance) tuple
    """
    time = int(puzzle_input[0].replace("Time:", "").replace(" ", ""))
    distance = int(puzzle_input[1].replace("Distance:", "").replace(" ", ""))

    return time, distance


def get_races(puzzle_input: list[str]) -> list[tuple[int, int]]:
    """Get races from puzzle input.

    :param puzzle_input: Puzzle input
    :return: List of (time, distance) tuples
    """
    times = map(int, puzzle_input[0].replace("Time:", "").split())
    distances = map(int, puzzle_input[1].replace("Distance:", "").split())
    races = list(zip(times, distances))

    return races


def solve_inequality(race: tuple[int, int]) -> tuple[float, float]:
    """Solve a 2nd degree integer inequality.

    :param race: (time, distance) tuple
    :return: (x0, x1) tuple
    """
    time, distance = race
    b = -time
    c = distance

    d = b**2 - 4 * c

    x0 = (-b - math.sqrt(d)) / 2
    x1 = (-b + math.sqrt(d)) / 2

    return x0, x1


if __name__ == "__main__":
    main()
