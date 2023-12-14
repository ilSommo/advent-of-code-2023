"""Day 14: Parabolic Reflector Dish."""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"

import numpy as np
from numpy import uint8
from numpy.typing import NDArray


def main() -> None:
    """Solve day 14 puzzles."""
    with open("data/day_14_input.txt", encoding="ascii") as input_file:
        raw_input = input_file.readlines()

    pattern = []
    for line in raw_input:
        line = line.replace(".", "0")
        line = line.replace("O", "1")
        line = line.replace("#", "2")
        pattern.append(np.array(list(map(int, line.strip()))))
    puzzle_input = np.array(pattern)

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: NDArray[uint8]) -> None:
    """Solve the first puzzle."""
    tilted = tilt_north(puzzle_input)

    weight = get_weight(tilted)

    print(f"Star 1: {weight}")


def star_2(puzzle_input: NDArray[uint8]) -> None:
    """Solve the second puzzle."""
    tilted = spin_cycles(platform=puzzle_input, n_cycles=1000000000)

    weight = get_weight(tilted)

    print(f"Star 2: {weight}")


def get_weight(platform: NDArray[uint8]) -> int:
    """Get weight of configuration."""
    n_lines = len(platform)

    total = 0
    for i, line in enumerate(platform):
        weight = (n_lines - i) * len(np.where(line == 1)[0])
        total += weight

    return total


def spin_cycle(
    platform: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    """Perform a North-West-South-East spin cycle."""
    tilted = np.asarray(platform)

    tilted = tilt_north(tilted)
    tilted = tilt_west(tilted)
    tilted = tilt_south(tilted)
    tilted = tilt_east(tilted)

    return tuple(map(tuple, tilted))


def spin_cycles(platform: NDArray[uint8], n_cycles: int) -> NDArray[uint8]:
    """Perform a number of spin cycles."""
    tilted = tuple(map(tuple, platform))
    known_tilted = [tilted]

    for _ in range(n_cycles):
        tilted = spin_cycle(tilted)

        if tilted in known_tilted:
            base_index = known_tilted.index(tilted)
            cycle_length = len(known_tilted) - base_index
            index = base_index + (n_cycles - base_index) % cycle_length
            return np.asarray(known_tilted[index])

        known_tilted.append(tilted)

    return np.asarray(tilted)


def tilt_east(platform: NDArray[uint8]) -> NDArray[uint8]:
    """Tilt to East."""
    tilted = platform.T
    tilted = tilt_south(tilted)
    tilted = tilted.T

    return tilted


def tilt_north(platform: NDArray[uint8]) -> NDArray[uint8]:
    """Tilt to North."""
    tilted = np.zeros_like(platform)

    for j, column in enumerate(platform.T):
        rounds = np.asarray(np.where(column == 1))
        cubes = [-1] + list(np.where(column == 2)[0]) + [len(column)]
        np.put(tilted.T[j], cubes[1:-1], 2)
        new_rounds = []
        for i, _ in enumerate(cubes[:-1]):
            first_index = cubes[i] + 1
            last_index = first_index + len(
                rounds[(cubes[i] < rounds) & (rounds < cubes[i + 1])]
            )
            new_rounds.extend(list(range(first_index, last_index)))
        np.put(tilted.T[j], new_rounds, 1)

    return tilted


def tilt_south(platform: NDArray[uint8]) -> NDArray[uint8]:
    """Tilt to South."""
    tilted = np.flip(platform)
    tilted = tilt_north(tilted)
    tilted = np.flip(tilted)

    return tilted


def tilt_west(platform: NDArray[uint8]) -> NDArray[uint8]:
    """Tilt to West."""
    tilted = platform.T
    tilted = tilt_north(tilted)
    tilted = tilted.T

    return tilted


if __name__ == "__main__":
    main()
