"""Day 18: Lavaduct Lagoon."""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


def main() -> None:
    """Solve day 18 puzzles."""
    with open("data/day_18_input.txt", encoding="ascii") as input_file:
        puzzle_input = [line.strip() for line in input_file.readlines()]

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle."""
    instructions = []
    for line in puzzle_input:
        direction = line.split()[0]
        distance = int(line.split()[1])
        instructions.append((direction, distance))

    trench = get_trench(instructions)

    lava = get_lava(trench)

    print(f"Star 1: {lava}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle."""
    instructions = []
    for line in puzzle_input:
        hex_instruction = line.split()[2][2:-1]
        match hex_instruction[-1]:
            case "0":
                direction = "R"
            case "1":
                direction = "D"
            case "2":
                direction = "L"
            case "3":
                direction = "U"
        distance = int(hex_instruction[:-1], base=16)
        instructions.append((direction, distance))

    trench = get_trench(instructions)

    lava = get_lava(trench)

    print(f"Star 2: {lava}")


def get_lava(trench: list[list[tuple[int, int, str]]]) -> int:
    """Get area of lava in trench."""
    old_y = trench[0][0][1] - 1
    total = 0
    last_area = 0

    for line in trench:
        if line[0][1] - old_y > 1:
            total += (line[0][1] - old_y - 1) * last_area

        in_flag = 0
        f_flag = False
        l_flag = False
        old_in_flag = 0
        old_f_flag = False
        old_l_flag = False

        area = 0
        for i, (x, _, character) in enumerate(line):
            area += 1
            in_flag, f_flag, l_flag = update_flags(
                character,
                in_flag=in_flag,
                f_flag=f_flag,
                l_flag=l_flag,
            )
            if old_in_flag or old_f_flag or old_l_flag:
                area += x - line[i - 1][0] - 1
            old_in_flag = in_flag
            old_f_flag = f_flag
            old_l_flag = l_flag

        old_y = line[0][1]
        last_area = area
        total += area

    return total


def get_trench(
    instructions: list[tuple[str, int]]
) -> list[list[tuple[int, int, str]]]:
    """Get trench coordinates."""
    flat_trench = set()

    x, y = (0, 0)

    for k, (direction, distance) in enumerate(instructions):
        previous_instruction = instructions[k - 1][0]
        match direction:
            case "R":
                flat_trench.add(
                    (x, y, "L" if previous_instruction == "D" else "F")
                )
                x += distance
            case "D":
                flat_trench.add(
                    (x, y, "7" if previous_instruction == "R" else "F")
                )
                flat_trench.add((x, y + 1, "|"))
                flat_trench.add((x, y + distance - 1, "|"))
                y += distance
            case "L":
                flat_trench.add(
                    (x, y, "J" if previous_instruction == "D" else "7")
                )
                x -= distance
            case "U":
                flat_trench.add(
                    (x, y, "J" if previous_instruction == "R" else "L")
                )
                flat_trench.add((x, y - 1, "|"))
                flat_trench.add((x, y - distance + 1, "|"))
                y -= distance

    y_s = set(step[1] for step in flat_trench)

    for k, (direction, distance) in enumerate(instructions):
        previous_instruction = instructions[k - 1][0]
        match direction:
            case "R":
                x += distance
            case "D":
                for j in range(y + 1, y + distance):
                    if j in y_s:
                        flat_trench.add((x, max(j - 1, y + 1), "|"))
                        flat_trench.add((x, j, "|"))
                        flat_trench.add((x, min(j + 1, y + distance - 1), "|"))
                y += distance
            case "L":
                x -= distance
            case "U":
                for j in range(y - distance + 1, y):
                    if j in y_s:
                        flat_trench.add((x, max(j - 1, y - distance + 1), "|"))
                        flat_trench.add((x, j, "|"))
                        flat_trench.add((x, min(j + 1, y - 1), "|"))
                y -= distance

    sorted_trench = sorted(flat_trench, key=lambda step: step[1])

    trench = []

    j = sorted_trench[0][1]
    line = []

    for step in sorted_trench:
        if step[1] == j:
            line.append(step)
        else:
            trench.append(sorted(line, key=lambda step: step[0]))
            j = step[1]
            line = [step]

    trench.append(sorted(line, key=lambda step: step[0]))

    return trench


def update_flags(
    character: str,
    in_flag: int,
    f_flag: bool,
    l_flag: bool,
) -> tuple[int, bool, bool]:
    """Update flags."""
    if not (f_flag or l_flag):
        f_flag = character == "F"
        l_flag = character == "L"
        in_flag = (in_flag + 1) % 2

    elif f_flag:
        f_flag = False
        if character == "7":
            in_flag = (in_flag + 1) % 2

    elif l_flag:
        l_flag = False
        if character == "J":
            in_flag = (in_flag + 1) % 2

    return in_flag, f_flag, l_flag


if __name__ == "__main__":
    main()
