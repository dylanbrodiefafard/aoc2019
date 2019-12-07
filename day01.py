from util import get_lines


def fuel_required(mass, count_mass_of_fuel=False):
    fuel = max(int(mass / 3) - 2, 0)

    if not count_mass_of_fuel or fuel <= 0:
        return fuel

    return fuel + fuel_required(fuel, count_mass_of_fuel)


def part1(masses):
    return sum(fuel_required(mass) for mass in masses)


def part2(masses):
    return sum(fuel_required(mass, True) for mass in masses)


if __name__ == '__main__':
    # Part 1 examples
    assert fuel_required(12) == 2
    assert fuel_required(14) == 2
    assert fuel_required(1969) == 654
    assert fuel_required(100756) == 33583
    # Part 2 examples
    assert fuel_required(12, True) == 2
    assert fuel_required(1969, True) == 966
    assert fuel_required(100756, True) == 50346

    formatted_input = [int(line) for line in get_lines('input/day01.txt')]

    print(part1(formatted_input))
    print(part2(formatted_input))
