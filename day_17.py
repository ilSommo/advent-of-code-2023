"""Day 17: Clumsy Crucible."""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"

from heapq import heappop, heappush
from typing import NamedTuple


class State(NamedTuple):
    """Problem state."""

    heat: int
    x: int
    y: int
    p_x: int
    p_y: int


def main() -> None:
    """Solve day 17 puzzles."""
    with open("data/day_17_input.txt", encoding="ascii") as input_file:
        puzzle_input = [line.strip() for line in input_file.readlines()]

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle."""
    min_heat = get_minimum_heat(puzzle_input, 1, 3)

    print(f"Star 1: {min_heat}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle."""
    min_heat = get_minimum_heat(puzzle_input, 4, 10)

    print(f"Star 2: {min_heat}")


def get_minimum_heat(
    puzzle_input: list[str], min_steps: int, max_steps: int
) -> int:
    """Get the minimum possible total heat."""
    int_input = []
    for line in puzzle_input:
        int_input.append(list(map(int, list(line))))

    max_x = len(int_input[0]) - 1
    max_y = len(int_input) - 1

    heap = [State(0, 0, 0, 1, 0), State(0, 0, 0, 0, 1)]
    visited = set()

    while heap:
        current = heappop(heap)
        if current.x == max_x and current.y == max_y:
            return current.heat

        if (current.x, current.y, current.p_x, current.p_y) in visited:
            continue

        visited.add((current.x, current.y, current.p_x, current.p_y))

        if current.p_x == 0:
            for p in range(min_steps, max_steps + 1):
                y = current.y
                if current.x + p <= max_x:
                    x = current.x + p
                    heat = current.heat + sum(
                        int_input[y][i] for i in range(current.x + 1, x + 1)
                    )
                    heappush(heap, State(heat, x, y, p, 0))
                if current.x - p >= 0:
                    x = current.x - p
                    heat = current.heat + sum(
                        int_input[y][i] for i in range(x, current.x)
                    )
                    heappush(heap, State(heat, x, y, -p, 0))

        if current.p_y == 0:
            for p in range(min_steps, max_steps + 1):
                x = current.x
                if current.y + p <= max_y:
                    y = current.y + p
                    heat = current.heat + sum(
                        int_input[j][x] for j in range(current.y + 1, y + 1)
                    )
                    heappush(heap, State(heat, x, y, 0, p))
                if current.y - p >= 0:
                    y = current.y - p
                    heat = current.heat + sum(
                        int_input[j][x] for j in range(y, current.y)
                    )
                    heappush(heap, State(heat, x, y, 0, -p))

    raise ValueError("Invalid input!")


if __name__ == "__main__":
    main()
