"""Day 13: Point of Incidence."""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"

from collections import Counter

import numpy as np
from numpy import uint8
from numpy.typing import NDArray


def main() -> None:
    """Solve day 13 puzzles."""
    with open("data/day_13_input.txt", encoding="ascii") as input_file:
        raw_input = input_file.readlines()

    puzzle_input = []
    pattern: list[NDArray[uint8]] = []
    for line in raw_input:
        line = line.replace(".", "0")
        line = line.replace("#", "1")
        if line == "\n":
            puzzle_input.append(np.array(pattern))
            pattern = []
        else:
            pattern.append(np.array(list(map(int, line.strip()))))
    puzzle_input.append(np.array(pattern))

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[NDArray[uint8]]) -> None:
    """Solve the first puzzle."""
    total = 0
    for pattern in puzzle_input:
        total += find_mirror(pattern)

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[NDArray[uint8]]) -> None:
    """Solve the second puzzle."""
    total = 0
    for pattern in puzzle_input:
        total += find_mirror_smudge(pattern)

    print(f"Star 2: {total}")


def find_mirror(pattern: NDArray[uint8]) -> int:
    """Find mirror value."""
    for j, _ in enumerate(pattern[:-1]):
        flag = True
        for jj in range(min(j + 1, len(pattern) - j - 1)):
            if (pattern[j - jj] != pattern[j + jj + 1]).any():
                flag = False
                break
        if flag:
            return 100 * (j + 1)

    for i, _ in enumerate(pattern.T[:-1]):
        flag = True
        for ii in range(min(i + 1, len(pattern.T) - i - 1)):
            if (pattern.T[i - ii] != pattern.T[i + ii + 1]).any():
                flag = False
                break
        if flag:
            return i + 1

    raise ValueError("Mirror not found!")


def find_mirror_smudge(pattern: NDArray[uint8]) -> int:
    """Find mirror value with smudge."""
    for j, _ in enumerate(pattern[:-1]):
        flag = True
        smudge = False
        for jj in range(min(j + 1, len(pattern) - j - 1)):
            counter = Counter(pattern[j - jj] - pattern[j + jj + 1])
            if counter[1] + counter[-1] == 1:
                if smudge:
                    flag = False
                    break
                smudge = True
            elif (pattern[j - jj] != pattern[j + jj + 1]).any():
                flag = False
                break
        if flag and smudge:
            return 100 * (j + 1)

    for i, _ in enumerate(pattern.T[:-1]):
        flag = True
        smudge = False
        for ii in range(min(i + 1, len(pattern.T) - i - 1)):
            counter = Counter(pattern.T[i - ii] - pattern.T[i + ii + 1])
            if counter[1] + counter[-1] == 1:
                if smudge:
                    flag = False
                    break
                smudge = True
            elif (pattern.T[i - ii] != pattern.T[i + ii + 1]).any():
                flag = False
                break
        if flag and smudge:
            return i + 1

    raise ValueError("Mirror not found!")


if __name__ == "__main__":
    main()
