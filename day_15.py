"""Day 15: Lens Library."""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


def main() -> None:
    """Solve day 15 puzzles."""
    with open("data/day_15_input.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().strip()

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: str) -> None:
    """Solve the first puzzle."""
    total = 0

    for step in puzzle_input.split(","):
        total += step2hash(step)

    print(f"Star 1: {total}")


def star_2(puzzle_input: str) -> None:
    """Solve the second puzzle."""
    boxes: dict[int, dict[str, int]] = {}
    for i in range(256):
        boxes[i] = {}

    for step in puzzle_input.split(","):
        if "=" in step:
            label, focal = step.split("=")
            box = step2hash(label)
            boxes[box][label] = int(focal)
        else:
            label = step[:-1]
            box = step2hash(label)
            boxes[box].pop(label, None)

    total = 0

    for box, lenses in boxes.items():
        for i, value in enumerate(lenses.values()):
            total += (box + 1) * (i + 1) * value

    print(f"Star 2: {total}")


def char2hash(current_value: int, char: str) -> int:
    """Convert char to hash value."""
    ascii_code = ord(char)

    current_value += ascii_code
    current_value *= 17
    current_value %= 256

    return current_value


def step2hash(step: str) -> int:
    """Convert string to hash value."""
    current_value = 0

    for char in step:
        current_value = char2hash(current_value=current_value, char=char)

    return current_value


if __name__ == "__main__":
    main()
