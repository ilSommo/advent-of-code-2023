"""Day 12: Hot Springs."""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


from functools import cache


def main() -> None:
    """Solve day 12 puzzles."""
    with open("data/day_12_input.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle."""
    total = 0
    for line in puzzle_input:
        arrangements = compute_valid_arrangements(line)
        total += arrangements

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle."""
    total = 0
    for line in puzzle_input:
        graph, damaged = line.split()
        line = (
            str(5 * (graph + "?"))[:-1] + " " + str(5 * (damaged + ","))[:-1]
        )
        arrangements = compute_valid_arrangements(line)
        total += arrangements

    print(f"Star 2: {total}")


def compute_valid_arrangements(line: str) -> int:
    """Compute the number of valid arrangements of a given line."""
    graph, damaged_str = line.split()
    springs = graph + "."
    damaged = tuple(map(int, damaged_str.split(",")))

    arrangements = find_arrangemets(springs, damaged)

    return arrangements


@cache
def find_arrangemets(springs: str, damaged: tuple[int]) -> int:
    """Find possible arrangements recursively."""
    total = 0
    size = damaged[0]
    sub_damaged = damaged[1:]

    for i, spring in enumerate(springs[: -size - sum(sub_damaged)]):
        if (
            springs[i - 1] != "#"
            and all(spring in ["?", "#"] for spring in springs[i : i + size])
            and springs[i + size] != "#"
        ):
            if len(damaged) > 1:
                total += find_arrangemets(
                    springs[i + size + 1 :], tuple(sub_damaged)
                )
            elif "#" not in springs[i + size + 1 :]:
                total += 1

        if spring == "#":
            break

    return total


if __name__ == "__main__":
    main()
