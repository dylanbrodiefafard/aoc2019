from util import get_lines


def meets_criteria(password, max_digit_group=None):
    if len(password) != 6:
        return False  # not the correct length

    no_pair = True
    max_digit = float('-inf')
    previous_digit = None
    num_adjacent_digits_same = 1

    for j, digit in enumerate(password):
        last_digit = j == len(password) - 1
        if digit == previous_digit:
            num_adjacent_digits_same += 1
        if digit != previous_digit or last_digit:
            if num_adjacent_digits_same >= 2 and \
                    (max_digit_group is None or num_adjacent_digits_same <= max_digit_group):
                no_pair = False
            previous_digit = digit
            num_adjacent_digits_same = 1
        if int(digit) < max_digit:
            return False  # decreased
        max_digit = max(max_digit, int(digit))

    if no_pair:
        return False  # No pair of digits

    return True


def part1(low, high):
    return sum(1 for i in range(low, high + 1) if meets_criteria(str(i)))


def part2(low, high):
    return sum(1 for i in range(low, high + 1) if meets_criteria(str(i), max_digit_group=2))


if __name__ == '__main__':
    # Part 1 examples
    assert meets_criteria('111111')
    assert not meets_criteria('223450')
    assert not meets_criteria('123789')
    # Part 2 examples
    assert meets_criteria('112233', max_digit_group=2)
    assert not meets_criteria('123444', max_digit_group=2)
    assert meets_criteria('111122', max_digit_group=2)

    formatted_input = [int(number) for number in get_lines('input/day04.txt')[0].split('-')]

    print(part1(*formatted_input))
    print(part2(*formatted_input))
