import re
from typing import List, Tuple

import numpy as np


def read_input() -> List[str]:
    with open('input.txt', 'r') as input_file:
        return [line.strip() for line in input_file]


def find_surrounding_points(input, row, start, end) -> List[str]:
    # find the surrounding points that are not a number or .
    current = re.sub(r'\d+', '', input[row][start:end]).strip('.')
    row_before = re.sub(r'\d+', '', input[row - 1][start:end]).strip('.') if row != 0 else ''
    next_row = re.sub(r'\d+', '', input[row + 1][start:end]).strip('.') if row != len(input) - 1 else ''
    return [current, row_before, next_row]


def part_numbers(input, row, start, end) -> bool:
    # count surrounding points not a number or . to see if it's a part number
    return len(''.join(find_surrounding_points(input, row, start, end))) > 0


def find_gears(input, row, start, end) -> List[Tuple[int, int]]:  # returns a list of the positions of *
    rows = find_surrounding_points(input, row, start, end)

    potential_gear = []  # tuple of the row the * is and the position

    if rows[0].find('*') != -1:  # look at the current row for a *
        index_of_gear = input[row][start:end].index('*')
        position = start + index_of_gear
        potential_gear.append((row, position))
    if rows[1].find('*') != -1:  # look at the row before for a *
        index_of_gear = input[row - 1][start:end].index('*')
        position = start + index_of_gear
        potential_gear.append((row - 1, position))
    if rows[2].find('*') != -1:  # look at the next row for a *
        index_of_gear = input[row + 1][start:end].index('*')
        position = start + index_of_gear
        potential_gear.append((row + 1, position))

    return potential_gear


def solution():
    input = read_input()
    parts = []  # list of all the part numbers that are parts - part 1
    parts_with_gears = {}  # dict of the position (row, column): part numbers

    for r, line in enumerate(input):  # row number, line
        for n in re.finditer(r'\d+', line):  # find match for number patterns
            start = n.start() - 1 if n.start() > 0 else 0  # start point of search, 1 before the number unless start
            end = n.end() + 1 if n.end() < len(line) else n.end()  # end point of search, 1 after the number unless end

            if part_numbers(input, r, start, end) is True:  # part 1
                parts.append(int(n.group()))  # if it is a part number append the part number to parts

            gears = find_gears(input, r, start, end)

            for gear in gears:
                if gear in parts_with_gears.keys():  # check if the gear position exists
                    parts_with_gears[gear] += [int(n.group())]
                else:
                    parts_with_gears[gear] = [int(n.group())]

    gear_ratios = []
    for x in parts_with_gears:
        # look at each position if there are multiple part numbers then multiply and add to gear_ratios
        gear_ratios.append(np.prod(parts_with_gears[x]) if len(parts_with_gears[x]) > 1 else 0)

    print(f'solution part 1: {sum(parts)}')
    print(f'solution part 2: {sum(gear_ratios)}')


if __name__ == '__main__':
    solution()
