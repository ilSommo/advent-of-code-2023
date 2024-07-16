"""Day 17: Clumsy Crucible."""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"

<<<<<<< HEAD

from dataclasses import dataclass
from itertools import product
import math
from tqdm import tqdm
from heapq import heappop, heappush
=======
from heapq import heappop, heappush
from typing import NamedTuple


class State(NamedTuple):
    """Problem state."""

    heat: int
    x: int
    y: int
    p_x: int
    p_y: int
>>>>>>> 9a95a90b4cc578450a324b9cbdb6efaaca881400


def main() -> None:
    """Solve day 17 puzzles."""
    with open("data/day_17_input.txt", encoding="ascii") as input_file:
        puzzle_input = [line.strip() for line in input_file.readlines()]

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle."""
<<<<<<< HEAD
    max_x = len(puzzle_input[0]) - 1
    max_y = len(puzzle_input) - 1
    min_p = 1
    max_p = 3

    graph = []

    for x, y, p in product(
        range(max_x + 1),
        range(max_y + 1),
        range(min_p, max_p + 1),
    ):
        if 0 <= x - p <= max_x:
            graph.append(Coordinates(x, y, p, 0, max_x, max_y, min_p, max_p))
        if 0 <= x + p <= max_x:
            graph.append(Coordinates(x, y, -p, 0, max_x, max_y, min_p, max_p))
        if 0 <= y - p <= max_y:
            graph.append(Coordinates(x, y, 0, p, max_x, max_y, min_p, max_p))
        if 0 <= y + p <= max_y:
            graph.append(Coordinates(x, y, 0, -p, max_x, max_y, min_p, max_p))

    dist = dijkstra(
        puzzle_input,
        Coordinates(0, 0, 0, 0, max_x, max_y, min_p, max_p),
    )

    print(f"Star 1: {dist}")
=======
    min_heat = get_minimum_heat(puzzle_input, 1, 3)

    print(f"Star 1: {min_heat}")
>>>>>>> 9a95a90b4cc578450a324b9cbdb6efaaca881400


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle."""
<<<<<<< HEAD
    max_x = len(puzzle_input[0]) - 1
    max_y = len(puzzle_input) - 1
    min_p = 4
    max_p = 10

    graph = []

    for x, y, p in product(
        range(max_x + 1),
        range(max_y + 1),
        range(min_p, max_p + 1),
    ):
        if 0 <= x - p <= max_x:
            graph.append(Coordinates(x, y, p, 0, max_x, max_y, min_p, max_p))
        if 0 <= x + p <= max_x:
            graph.append(Coordinates(x, y, -p, 0, max_x, max_y, min_p, max_p))
        if 0 <= y - p <= max_y:
            graph.append(Coordinates(x, y, 0, p, max_x, max_y, min_p, max_p))
        if 0 <= y + p <= max_y:
            graph.append(Coordinates(x, y, 0, -p, max_x, max_y, min_p, max_p))

    dist = dijkstra(
        puzzle_input,
        Coordinates(0, 0, 0, 0, max_x, max_y, min_p, max_p),
    )

    print(f"Star 2: {dist}")


def dijkstra(input_map, source):
    heap = [(0, source)]
    dists = {source: 0}

    while heap:
        dist, current = heappop(heap)

        if (
            current.x == len(input_map[0]) - 1
            and current.y == len(input_map) - 1
        ):
            return dist

        for neighbor in current.neighbors:
            neighbor_dist = dist + int(input_map[neighbor.y][neighbor.x])
            if neighbor not in dists.keys() or (
                neighbor in dists.keys() and neighbor_dist < dists[neighbor]
            ):
                dists[neighbor] = neighbor_dist
                heappush(heap, (neighbor_dist, neighbor))

    return math.inf


@dataclass
class Coordinates:
    x: int
    y: int
    p_x: int
    p_y: int
    max_x: int
    max_y: int
    min_p: int
    max_p: int

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Coordinates):
            return NotImplemented
        if (
            self.x < other.x
            or (self.x == other.x and self.y < other.y)
            or (
                self.x == other.x
                and self.y == other.y
                and self.p_x < other.p_x
            )
            or (
                self.x == other.x
                and self.y == other.y
                and self.p_x == other.p_x
                and self.p_y < other.p_y
            )
        ):
            return True
        return False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinates):
            return NotImplemented
        return (
            self.x == other.x
            and self.y == other.y
            and self.p_x == other.p_x
            and self.p_y == other.p_y
        )

    def __hash__(self):
        return hash((self.x, self.y, self.p_x, self.p_y))

    @property
    def neighbors(self):
        neighbors = []

        if (
            0 <= self.p_x <= self.max_p - self.min_p
            and 0 <= self.x + self.min_p <= self.max_x
        ):
            neighbors.append(
                Coordinates(
                    self.x + self.min_p,
                    self.y,
                    self.p_x + self.min_p,
                    0,
                    self.max_x,
                    self.max_y,
                    self.min_p,
                    self.max_p,
                )
            )
        if (
            -self.max_p + self.min_p <= self.p_x <= 0
            and 0 <= self.x - self.min_p <= self.max_x
        ):
            neighbors.append(
                Coordinates(
                    self.x - self.min_p,
                    self.y,
                    self.p_x - self.min_p,
                    0,
                    self.max_x,
                    self.max_y,
                    self.min_p,
                    self.max_p,
                )
            )
        if (
            0 <= self.p_y <= self.max_p - self.min_p
            and 0 <= self.y + self.min_p <= self.max_y
        ):
            neighbors.append(
                Coordinates(
                    self.x,
                    self.y + self.min_p,
                    0,
                    self.p_y + self.min_p,
                    self.max_x,
                    self.max_y,
                    self.min_p,
                    self.max_p,
                )
            )
        if (
            -self.max_p + self.min_p <= self.p_y <= 0
            and 0 <= self.y - self.min_p <= self.max_y
        ):
            neighbors.append(
                Coordinates(
                    self.x,
                    self.y - self.min_p,
                    0,
                    self.p_y - self.min_p,
                    self.max_x,
                    self.max_y,
                    self.min_p,
                    self.max_p,
                )
            )

        return neighbors
=======
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
>>>>>>> 9a95a90b4cc578450a324b9cbdb6efaaca881400


if __name__ == "__main__":
    main()
