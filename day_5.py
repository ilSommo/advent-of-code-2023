"Day 5: If You Give A Seed A Fertilizer"

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2023"
__license__ = "MIT"

STEPS = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def main() -> None:
    """Solve day 5 puzzles."""
    with open("data/day_5_input.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read()

    puzzle_input = puzzle_input.replace("seeds: ", "")
    seeds = list(map(int, puzzle_input.split("\n\n")[0].strip().split(" ")))

    maps = compute_maps(puzzle_input)

    star_1(seeds, maps)

    star_2(seeds, maps)


def star_1(seeds: list[int], maps: dict[str, list[tuple[int, ...]]]) -> None:
    """Solve the first puzzle.

    :param seeds: Input seeds
    :param maps: Dictionary of lists of (destination, source, range) tuples
    """
    locations = set()

    for seed in seeds:
        locations.add(seed_to_location(seed, maps))

    print(f"Star 1: {min(locations)}")


def star_2(seeds: list[int], maps: dict[str, list[tuple[int, ...]]]) -> None:
    """Solve the second puzzle.

    :param seeds: Input seeds
    :param maps: Dictionary of lists of (destination, source, range) tuples
    """
    seed_splits = find_splits(maps, 0)

    seeds_to_check = set()

    for i in range(0, len(seeds), 2):
        seeds_to_check.add(seeds[i])
        for split in seed_splits:
            if split in range(seeds[i], seeds[i] + seeds[i + 1]):
                seeds_to_check.add(split)

    locations = set()

    for seed in seeds_to_check:
        locations.add(seed_to_location(seed, maps))

    print(f"Star 2: {min(locations)}")


def apply_inverse_map(
    input_destination: int, map_: list[tuple[int, ...]]
) -> int:
    """Apply a map.

    :param input_destination: Input destination
    :param map_: List of (destination, source, range) tuples
    :return: Output destination
    """
    for destination, source, range_ in map_:
        if destination <= input_destination < destination + range_:
            return input_destination + source - destination

    return input_destination


def apply_map(input_source: int, map_: list[tuple[int, ...]]) -> int:
    """Apply a map.

    :param input_source: Input source
    :param map_: List of (destination, source, range) tuples
    :return: Output destination
    """
    for destination, source, range_ in map_:
        if source <= input_source < source + range_:
            return input_source + destination - source

    return input_source


def compute_maps(
    puzzle_input: str,
) -> dict[str, list[tuple[int, ...]]]:
    """Compute maps.

    :param puzzle_input: Puzzle input
    :return: Dictionary of lists of (destination, source, range) tuples
    """
    maps: dict[str, list[tuple[int, ...]]] = {}

    for step in STEPS:
        string = (
            puzzle_input.split(f"{step} map:\n")[1].split("\n\n")[0].strip()
        )
        maps[step] = []
        for line in string.split("\n"):
            maps[step].append(tuple(map(int, line.split(" "))))
        maps[step].sort(key=lambda x: x[1])

    return maps


def find_splits(maps: dict[str, list[tuple[int, ...]]], i: int) -> set[int]:
    """Find the splits of the ith level.

    :param maps: Dictionary of lists of (destination, source, range) tuples
    :param i: Index of the level
    :return: Splits
    """
    splits = set()
    for _, source, range_ in maps[STEPS[i]]:
        splits.add(source)
        splits.add(source + range_)
    i += 1
    if i < len(STEPS):
        destination_splits = find_splits(maps, i)
        for destination_split in destination_splits:
            splits.add(
                apply_inverse_map(destination_split, maps[STEPS[i - 1]])
            )
    return splits


def location_to_seed(
    location: int, maps: dict[str, list[tuple[int, ...]]]
) -> int:
    """Convert location to seed.

    :param location: Location
    :param maps: Dictionary of lists of (destination, source, range) tuples
    :return: Seed
    """
    for step in reversed(STEPS):
        location = apply_inverse_map(location, maps[step])

    return location


def seed_to_location(seed: int, maps: dict[str, list[tuple[int, ...]]]) -> int:
    """Convert seed to location.

    :param seed: Seed
    :param maps: Dictionary of lists of (destination, source, range) tuples
    :return: Location
    """
    for step in STEPS:
        seed = apply_map(seed, maps[step])

    return seed


if __name__ == "__main__":
    main()
