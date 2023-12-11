"""Day 9: Mirage Maintenance."""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


def main() -> None:
    """Solve day 10 puzzles."""
    with open("data/day_10_input.txt", encoding="ascii") as input_file:
        raw_input = input_file.readlines()

    puzzle_input = pad_input(raw_input)

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle.

    :param puzzle_input: Puzzle input
    """
    step = 1

    starting_position, current_position = get_starting_position(puzzle_input)

    previous_position = starting_position

    while current_position != starting_position:
        previous_position, current_position = execute_step(
            maze=puzzle_input,
            previous=previous_position,
            current=current_position,
        )
        step += 1

    print(f"Star 1: {step//2}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle.

    :param puzzle_input: Puzzle input
    """
    loop = set()

    starting_position, current_position = get_starting_position(puzzle_input)

    previous_position = starting_position

    loop.add(current_position)

    while current_position != starting_position:
        previous_position, current_position = execute_step(
            maze=puzzle_input,
            previous=previous_position,
            current=current_position,
        )
        loop.add(current_position)

    area = 0

    for j, line in enumerate(puzzle_input):
        in_flag = 0
        f_flag = False
        l_flag = False
        for i, character in enumerate(line):
            if (i, j) in loop and character != "-":
                in_flag, f_flag, l_flag = update_flags(
                    maze=puzzle_input,
                    current=(i, j),
                    in_flag=in_flag,
                    f_flag=f_flag,
                    l_flag=l_flag,
                )
            elif in_flag and (i, j) not in loop:
                area += 1

    print(f"Star 2: {area}")


def get_starting_position(
    puzzle_input: list[str],
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Get starting positions.

    :param puzzle_input: Puzzle input
    :return: Tuple of starting and first step coordinates
    """
    for j, line in enumerate(puzzle_input):
        x = line.find("S")
        if x >= 0:
            y = j
            break

    if puzzle_input[y - 1][x] in ["|", "F", "7"]:
        return ((x, y), (x, y - 1))
    if puzzle_input[y][x + 1] in ["-", "7", "J"]:
        return ((x, y), (x + 1, y))
    if puzzle_input[y + 1][x] in ["|", "J", "L"]:
        return ((x, y), (x, y + 1))
    if puzzle_input[y][x + 1] in ["-", "L", "F"]:
        return ((x, y), (x - 1, y))

    raise ValueError("Invalid input!")


def execute_step(
    maze: list[str], previous: tuple[int, int], current: tuple[int, int]
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Execute step.

    :param maze: Maze map
    :param previous: Previous position
    :param current: Current position
    :return: New previous and current positions
    """
    x_p, y_p = previous
    x, y = current

    match maze[y][x]:
        case "|":
            next_ = (x, y + 1) if y_p < y else (x, y - 1)
        case "-":
            next_ = (x + 1, y) if x_p < x else (x - 1, y)
        case "F":
            next_ = (x + 1, y) if y_p > y else (x, y + 1)
        case "7":
            next_ = (x, y + 1) if x_p < x else (x - 1, y)
        case "J":
            next_ = (x - 1, y) if y_p < y else (x, y - 1)
        case "L":
            next_ = (x, y - 1) if x_p > x else (x + 1, y)

    return current, next_


def pad_input(raw_input: list[str]) -> list[str]:
    """Pad input.

    :param raw_input: Puzzle input
    :return: Padded input
    """
    matrix_input = []

    matrix_input.append("." * (len(raw_input[0]) + 1))
    for line in raw_input:
        matrix_input.append("." + line.strip() + ".")
    matrix_input.append("." * (len(raw_input[0]) + 1))

    return matrix_input


def update_flags(
    maze: list[str],
    current: tuple[int, int],
    in_flag: int,
    f_flag: bool,
    l_flag: bool,
) -> tuple[int, bool, bool]:
    """Update flags.

    :param maze: Maze map
    :param current: Current coordinates
    :param in_flag: If inside of loop
    :param f_flag: If in 'F' section
    :param l_flag: If in 'L' section
    :return: Updated in_flag, f_flag, l_flag
    """
    x, y = current
    character = maze[y][x]

    if not (f_flag or l_flag):
        f_flag = character == "F"
        l_flag = character == "L"
        in_flag = (in_flag + 1) % 2

    elif f_flag:
        f_flag = False
        if character == "7" or (
            character == "S" and maze[y + 1][x] in ["|", "L", "J"]
        ):
            in_flag = (in_flag + 1) % 2

    elif l_flag:
        l_flag = False
        if character == "J" or (
            character == "S" and maze[y - 1][x] in ["|", "F", "7"]
        ):
            in_flag = (in_flag + 1) % 2

    return in_flag, f_flag, l_flag


if __name__ == "__main__":
    main()
