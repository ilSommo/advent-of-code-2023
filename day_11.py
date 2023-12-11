"""Day 11: Cosmic Expansion."""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


def main() -> None:
    """Solve day 11 puzzles."""
    with open("data/day_11_input.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle.

    :param puzzle_input: Puzzle input
    """
    galaxies = input_2_list(puzzle_input)
    galaxies = expand(galaxies=galaxies, factor=2)

    total = 0

    for j, g_2 in enumerate(galaxies):
        for g_1 in galaxies[:j]:
            distance = abs(g_2[0] - g_1[0]) + abs(g_2[1] - g_1[1])
            total += distance

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle.

    :param puzzle_input: Puzzle input
    """
    galaxies = input_2_list(puzzle_input)
    galaxies = expand(galaxies=galaxies, factor=1000000)

    total = 0

    for j, g_2 in enumerate(galaxies):
        for g_1 in galaxies[:j]:
            distance = abs(g_2[0] - g_1[0]) + abs(g_2[1] - g_1[1])
            total += distance

    print(f"Star 2: {total}")


def expand(
    galaxies: list[tuple[int, int]], factor: int
) -> list[tuple[int, int]]:
    """Expand space.

    :param galaxies: Input galaxies
    :param factor: Expansion factor
    :return: Expanded galaxies
    """
    expansion = factor - 1

    galaxies.sort(key=lambda g: g[0])
    cols = [g[0] for g in galaxies]
    offset = 0
    for col in range(galaxies[-1][0] + 1):
        if col not in cols:
            for i, galaxy in enumerate(galaxies):
                x, y = galaxy
                galaxies[i] = (x if x < col + offset else x + expansion, y)
            offset += expansion

    galaxies.sort(key=lambda g: g[1])
    rows = [g[1] for g in galaxies]
    offset = 0
    for row in range(galaxies[-1][1] + 1):
        if row not in rows:
            for i, galaxy in enumerate(galaxies):
                x, y = galaxy
                galaxies[i] = (x, y if y < row + offset else y + expansion)
            offset += expansion

    return galaxies


def input_2_list(puzze_input: list[str]) -> list[tuple[int, int]]:
    """Convert input to list of galaxies.

    :param puzzle_input: Puzzle input
    :return: List of positions of galaxies
    """
    galaxies = []
    for j, line in enumerate(puzze_input):
        for i, character in enumerate(line):
            if character == "#":
                galaxies.append((i, j))

    return galaxies


if __name__ == "__main__":
    main()
