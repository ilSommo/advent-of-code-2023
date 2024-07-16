"""Day 20: Pulse Propagation."""

from __future__ import annotations

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"

from abc import ABC, abstractmethod
from collections import deque
from math import lcm
from itertools import count


def main() -> None:
    """Solve day 20 puzzles."""
    with open("data/day_20_input.txt", encoding="ascii") as input_file:
        puzzle_input = [line.strip() for line in input_file.readlines()]

    star_1(puzzle_input)

    star_2(puzzle_input)


def star_1(puzzle_input: list[str]) -> None:
    """Solve the first puzzle."""
    modules = input_2_modules(puzzle_input)

    total_low_pulses = total_high_pulses = 0

    for _ in range(1000):
        low_pulses, high_pulses = press_button(modules)
        total_low_pulses += low_pulses
        total_high_pulses += high_pulses

    total = total_low_pulses * total_high_pulses

    print(f"Star 1: {total}")


def star_2(puzzle_input: list[str]) -> None:
    """Solve the second puzzle."""
    modules = input_2_modules(puzzle_input)

    required_trues = modules[modules["rx"].input_modules[0]].input_modules

    cycle_lengths = []

    for module in required_trues:
        modules = input_2_modules(puzzle_input)
        for i in count(1):
            if press_button_check(modules, module):
                cycle_lengths.append(i)
                break

    total_cycles = lcm(*cycle_lengths)

    print(f"Star 2: {total_cycles}")


class Module(ABC):
    """Generic module."""

    def __init__(self, output_modules: list[str]) -> None:
        self.output_modules = output_modules
        self.input_modules: list[str] = []
        self.states: dict[str, bool] = {}

    @abstractmethod
    def __call__(
        self, input_module: str, input_value: bool
    ) -> dict[str, bool | None]:
        pass

    def output_2_outputs(self, output: bool | None) -> dict[str, bool | None]:
        """Convert output value to dictionary."""
        outputs = {}
        for module in self.output_modules:
            outputs[module] = output
        return outputs


class FlipFlop(Module):
    """Flip-flop module."""

    def __init__(self, output_modules: list[str]) -> None:
        super().__init__(output_modules)
        self.status = False

    def __call__(
        self, input_module: str, input_value: bool
    ) -> dict[str, bool | None]:
        output = None
        if input_value is False:
            output = self.status = not self.status
        return self.output_2_outputs(output)


class Conjunction(Module):
    """Conjunction module."""

    def __call__(
        self, input_module: str, input_value: bool
    ) -> dict[str, bool | None]:
        if not self.states:
            for module in self.input_modules:
                self.states[module] = False

        self.states[input_module] = input_value

        output = not all(list(self.states.values()))

        return self.output_2_outputs(output)


class Broadcaster(Module):
    """Broadcaster module."""

    def __init__(self, output_modules: list[str]) -> None:
        super().__init__(output_modules)
        self.input_modules = ["button"]

    def __call__(
        self, input_module: str, input_value: bool
    ) -> dict[str, bool | None]:
        output = input_value
        return self.output_2_outputs(output)


class Output(Module):
    """Output module."""

    def __init__(self) -> None:
        super().__init__([])

    def __call__(
        self, input_module: str, input_value: bool
    ) -> dict[str, bool | None]:
        return self.output_2_outputs(None)


def input_2_modules(input_value: list[str]) -> dict[str, Module]:
    """Convert input to modules dictionary."""
    modules: dict[str, Module] = {}

    for line in input_value:
        module, outputs_str = line.split(" -> ")
        outputs = outputs_str.split(", ")
        if module == "broadcaster":
            modules[module] = Broadcaster(outputs)
        elif module[0] == "%":
            modules[module[1:]] = FlipFlop(outputs)
        elif module[0] == "&":
            modules[module[1:]] = Conjunction(outputs)

        for output in outputs:
            if output not in modules:
                modules[output] = Output()

    for line in input_value:
        module, outputs_str = line.split(" -> ")
        outputs = outputs_str.split(", ")
        for output in outputs:
            modules[output].input_modules.append(module.strip("%").strip("&"))
            modules[output].states[module.strip("%").strip("&")] = False

    return modules


def press_button(modules: dict[str, Module]) -> tuple[int, int]:
    """Execute one button press cycle."""
    low_pulses = 1
    high_pulses = 0

    queue = deque([("button", "broadcaster", False)])

    while queue:
        source, module, input_value = queue.popleft()
        output = modules[module](source, input_value)
        for output_module, output_value in output.items():
            if output_value is not None:
                queue.append((module, output_module, output_value))
            if output_value is False:
                low_pulses += 1
            if output_value is True:
                high_pulses += 1

    return low_pulses, high_pulses


def press_button_check(
    modules: dict[str, Module], required_module: str
) -> bool:
    """Execute one button press cycle and check for required module value."""
    queue = deque([("button", "broadcaster", False)])

    while queue:
        source, module, input_value = queue.popleft()
        output = modules[module](source, input_value)
        for output_module, output_value in output.items():
            if output_module == required_module and output_value is False:
                return True
            if output_value is not None:
                queue.append((module, output_module, output_value))

    return False


if __name__ == "__main__":
    main()
