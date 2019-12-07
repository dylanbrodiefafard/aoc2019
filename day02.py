from util import get_lines


def add(memory, address):
    address_lhs = memory[address + 1]
    address_rhs = memory[address + 2]
    address_store = memory[address + 3]
    memory[address_store] = memory[address_lhs] + memory[address_rhs]
    return 4


def multiply(memory, address):
    address_lhs = memory[address + 1]
    address_rhs = memory[address + 2]
    address_store = memory[address + 3]
    memory[address_store] = memory[address_lhs] * memory[address_rhs]
    return 4


def halt(memory, address):
    raise StopIteration


opcodes = {1: add, 2: multiply, 99: halt}


def run_machine(program, noun=None, verb=None):
    memory = {position: value for position, value in enumerate(program)}

    if noun is not None:
        memory[1] = noun
    if verb is not None:
        memory[2] = verb

    address = 0
    while True:
        opcode = memory[address]  # Will raise a KeyError if we try and access out of bounds memory
        try:
            address += opcodes[opcode](memory, address)  # Will raise a KeyError if opcode is not implemented
        except StopIteration:
            break  # Program has halted
    return memory[0]


def part2(program):
    for noun in range(100):
        for verb in range(100):
            if run_machine(program, noun, verb) == 19690720:
                return 100 * noun + verb


if __name__ == '__main__':
    # Part 1 examples
    assert run_machine([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == 3500
    assert run_machine([1, 0, 0, 0, 99]) == 2
    assert run_machine([2, 3, 0, 3, 99]) == 2
    assert run_machine([2, 4, 4, 5, 99, 0]) == 2
    assert run_machine([1, 1, 1, 4, 99, 5, 6, 0, 99]) == 30

    formatted_input = [int(line) for line in get_lines('input/day02.txt')[0].split(',')]

    # First step is to restore the gravity assist program to the "1202 program alarm" state
    print(run_machine(formatted_input, 12, 2))
    print(part2(formatted_input))
