"Day 2: Cube Conundrum"

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"

MAX = {"red": 12, "green": 13, "blue": 14}


def main() -> None:
    """Solve day 2 puzzles."""
    with open("day_2_input.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve first puzzle.

    :param puzzle_input: Puzzle input
    """
    total = 0

    for line in puzzle_input:
        game_id, max_colors = process_line(line)
        if is_possible(max_colors):
            total += game_id

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve second puzzle.

    :param puzzle_input: Puzzle input
    """
    total = 0

    for line in puzzle_input:
        _, max_colors = process_line(line)
        total += max_colors["red"] * max_colors["green"] * max_colors["blue"]

    print(f"Star 2: {total}")


def is_possible(max_colors: dict[str, int]) -> bool:
    """Check if the maximum color values are possible.

    :param max_colors: Maximum color values
    :return: If the game is possible
    """
    if (
        max_colors["red"] > MAX["red"]
        or max_colors["green"] > MAX["green"]
        or max_colors["blue"] > MAX["blue"]
    ):
        return False
    return True


def process_line(line: str) -> list[int, dict[str, int]]:
    """Process line.

    :param line: Input line
    :return: Game id and maximum color numbers
    """
    game, subsets = line.strip().split(": ")
    game_id = int(game.split(" ")[1])

    max_colors = {"red": 0, "green": 0, "blue": 0}

    for subset in subsets.split("; "):
        for pick in subset.split(", "):
            number, color = pick.split(" ")
            max_colors[color] = max(max_colors[color], int(number))

    return game_id, max_colors


if __name__ == "__main__":
    main()
