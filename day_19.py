"""Day 19: Aplenty."""

from __future__ import annotations

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"


from collections import namedtuple

Part = namedtuple("Part", ["x", "m", "a", "s"])

MIN_VALUE = 1
MAX_VALUE = 4000


def main() -> None:
    """Solve day 19 puzzles."""
    with open("data/day_19_input.txt", encoding="ascii") as input_file:
        puzzle_input = [line.strip() for line in input_file.readlines()]

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle."""
    worflows, parts = get_workflows_parts(puzzle_input)

    total = 0

    for part in parts:
        if is_accepted(part, worflows):
            total += part.x + part.m + part.a + part.s

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle."""

    worflows, _ = get_workflows_parts(puzzle_input)

    ranges = {
        "x": range(MIN_VALUE, MAX_VALUE + 1),
        "m": range(MIN_VALUE, MAX_VALUE + 1),
        "a": range(MIN_VALUE, MAX_VALUE + 1),
        "s": range(MIN_VALUE, MAX_VALUE + 1),
    }

    accepted_ranges = get_accepted_ranges(worflows, "in", ranges)

    total = 0

    for accepted_range in accepted_ranges:
        total += (
            len(accepted_range["x"])
            * len(accepted_range["m"])
            * len(accepted_range["a"])
            * len(accepted_range["s"])
        )

    print(f"Star 2: {total}")


def get_accepted_ranges(
    worflows: dict[str, Workflow], name: str, ranges: dict[str, range]
) -> list[dict[str, range]]:
    """Get all possible accepted ranges."""
    workflow = worflows[name]
    complementary_ranges = ranges.copy()

    splits = []
    for category, category_range, result, else_range in workflow.splits:
        condition_ranges = complementary_ranges.copy()
        condition_range = condition_ranges[category]
        condition_ranges[category] = range(
            max(condition_range[0], category_range[0]),
            min(condition_range[-1], category_range[-1]) + 1,
        )
        splits.append((condition_ranges, result))

        complementary_range = complementary_ranges[category]
        complementary_ranges[category] = range(
            max(complementary_range[0], else_range[0]),
            min(complementary_range[-1], else_range[-1]) + 1,
        )

    splits.append((complementary_ranges, workflow.rules[-1]))

    accepted_ranges = []

    for split in splits:
        if split[1] == "A":
            accepted_ranges.append(split[0])
        elif split[1] != "R":
            accepted_ranges.extend(get_accepted_ranges(worflows, split[1], split[0]))

    return accepted_ranges


def get_part(line: str) -> Part:
    """Get a part tuple."""
    categories = line[1:-1].split(",")
    x = int(categories[0].split("=")[1])
    m = int(categories[1].split("=")[1])
    a = int(categories[2].split("=")[1])
    s = int(categories[3].split("=")[1])

    part = Part(x, m, a, s)

    return part


def get_workflow(line: str) -> tuple[str, Workflow]:
    """Get a workflow object."""
    name, rules = line[:-1].split("{")

    workflow = Workflow(rules)

    return name, workflow


def get_workflows_parts(
    puzzle_input: list[str],
) -> tuple[dict[str, Workflow], list[Part]]:
    """Get workflows and parts."""
    puzzle_copy = puzzle_input.copy()

    workflows = {}
    while puzzle_copy[0]:
        name, workflow = get_workflow(puzzle_copy.pop(0))
        workflows[name] = workflow

    puzzle_copy.pop(0)

    parts = []
    while puzzle_copy:
        part = get_part(puzzle_copy.pop(0))
        parts.append(part)

    return workflows, parts


def is_accepted(part: Part, workflows: dict[str, Workflow]) -> bool:
    """Check if a part is accepted."""
    next_step = "in"

    while next_step not in ["A", "R"]:
        next_step = workflows[next_step].apply(part)

    return next_step == "A"


class Workflow:
    """Workflow representation."""

    def __init__(self, rules: str):
        """Constructor method."""
        self.rules = rules.split(",")

    @property
    def splits(self) -> list[tuple[str, range, str, range]]:
        """Possible value splits."""
        splits = []

        for rule in self.rules[:-1]:
            condition, result = rule.split(":")
            if condition[1] == "<":
                condition_range = range(MIN_VALUE, int(condition[2:]))
                else_range = range(int(condition[2:]), MAX_VALUE + 1)
            else:
                condition_range = range(int(condition[2:]) + 1, MAX_VALUE + 1)
                else_range = range(MIN_VALUE, int(condition[2:]) + 1)
            splits.append((condition[0], condition_range, result, else_range))

        return splits

    def apply(self, part: Part) -> str:
        """Apply workflow to a part."""
        for rule in self.rules[:-1]:
            condition, result = rule.split(":")
            if (
                condition[1] == "<" and getattr(part, condition[0]) < int(condition[2:])
            ) or (
                condition[1] == ">" and getattr(part, condition[0]) > int(condition[2:])
            ):
                return result
        return self.rules[-1]


if __name__ == "__main__":
    main()
