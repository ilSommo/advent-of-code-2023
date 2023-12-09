"Day 8: Haunted Wasteland"

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


import math


def main() -> None:
    """Solve day 8 puzzles."""
    with open("data/day_8_input.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve first puzzle.

    :param puzzle_input: Puzzle input
    """
    instructions = puzzle_input[0].strip()
    raw_nodes = puzzle_input[2:]
    nodes = get_nodes(raw_nodes)

    step = 0
    node = "AAA"
    while node != "ZZZ":
        instruction = instructions[step % len(instructions)]
        if instruction == "L":
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        step += 1

    print(f"Star 1: {step}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve second puzzle.

    :param puzzle_input: Puzzle input
    """
    instructions = puzzle_input[0].strip()
    raw_nodes = puzzle_input[2:]
    nodes = get_nodes(raw_nodes)

    current_nodes = []
    for node in nodes:
        if node[2] == "A":
            current_nodes.append(node)

    cycle_lengths = []

    for node in current_nodes:
        step = 0
        while node[2] != "Z":
            instruction = instructions[step % len(instructions)]
            if instruction == "L":
                node = nodes[node][0]
            else:
                node = nodes[node][1]
            step += 1
        cycle_lengths.append(step)

    global_step = math.lcm(*cycle_lengths)

    print(f"Star 2: {math.lcm(global_step)}")


def get_nodes(raw_nodes: list[str]) -> dict[str, tuple[str, str]]:
    """Process raw list of nodes.

    :param raw_nodes: Raw list of nodes
    :return: Dictionary of processed nodes
    """
    nodes = {}

    for node in raw_nodes:
        key = node[0:3]
        l = node[7:10]
        r = node[12:15]
        nodes[key] = (l, r)

    return nodes


if __name__ == "__main__":
    main()
