"""Day 16: The Floor Will Be Lava."""

from __future__ import annotations

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


def main() -> None:
    """Solve day 16 puzzles."""
    with open("data/day_16_input.txt", encoding="ascii") as input_file:
        puzzle_input = [line.strip() for line in input_file.readlines()]

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle."""
    energized = get_energized(puzzle_input, (-1, 0))

    print(f"Star 1: {energized}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle."""
    values = []

    for x, _ in enumerate(puzzle_input[0]):
        values.append(get_energized(puzzle_input, (x, -1)))
        values.append(get_energized(puzzle_input, (x, len(puzzle_input))))

    for y, _ in enumerate(puzzle_input):
        values.append(get_energized(puzzle_input, (-1, y)))
        values.append(get_energized(puzzle_input, (len(puzzle_input[0]), y)))

    print(f"Star 2: {max(values)}")


class Beam:
    """Beam representation."""

    def __init__(self, x: int, y: int, v_x: int, v_y: int) -> None:
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Beam):
            return NotImplemented
        return (
            self.x == other.x
            and self.y == other.y
            and self.v_x == other.v_x
            and self.v_y == other.v_y
        )

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.v_x, self.v_y))

    def advance(self, tile_map: list[str]) -> list[Beam]:
        """Advance by one time step."""
        x, y = self.x + self.v_x, self.y + self.v_y
        v_x, v_y = self.v_x, self.v_y

        beams: list[Beam] = []

        if not 0 <= x < len(tile_map[0]) or not 0 <= y < len(tile_map):
            return beams

        tile = tile_map[y][x]

        match tile:
            case ".":
                beams.append(Beam(x, y, v_x, v_y))
            case "/":
                v_x, v_y = -v_y, -v_x
                beams.append(Beam(x, y, v_x, v_y))
            case "\\":
                v_x, v_y = v_y, v_x
                beams.append(Beam(x, y, v_x, v_y))
            case "|":
                if v_x:
                    beams.append(Beam(x, y, 0, 1))
                    beams.append(Beam(x, y, 0, -1))
                else:
                    beams.append(Beam(x, y, v_x, v_y))
            case "-":
                if v_y:
                    beams.append(Beam(x, y, 1, 0))
                    beams.append(Beam(x, y, -1, 0))
                else:
                    beams.append(Beam(x, y, v_x, v_y))

        return beams


def get_energized(
    puzzle_input: list[str], starting_edge: tuple[int, int]
) -> int:
    """Get the number of energized tiles."""
    x, y = starting_edge
    v_x, v_y = (0, 0)

    if x == -1:
        v_x = 1
    elif y == -1:
        v_y = 1
    elif x > y:
        v_x = -1
    elif x < y:
        v_y = -1

    beams = [Beam(x, y, v_x, v_y)]

    old_states = None
    states: set[Beam] = set()

    while old_states != states:
        old_states = states.copy()
        new_beams = []

        for beam in beams:
            new_beams.extend(beam.advance(puzzle_input))

        beams = [new_beam for new_beam in new_beams if new_beam not in states]
        states.update(beam for beam in beams)

    energized = set((state.x, state.y) for state in states)

    return len(energized)


if __name__ == "__main__":
    main()
