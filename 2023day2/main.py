from typing import List, Tuple, Dict

import numpy as np


def read_input():
    with open('input.txt', 'r') as input_file:
        input_list = {}
        for line in input_file:
            line = line.strip().split(':')
            game = line[0].strip('Game ')
            cubes = line[1].strip().split(';')
            input_list[game] = cubes
        return input_list


def game_possible(sets: List[str]) -> Tuple[List[bool], Dict[str, int]]:
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    minimum_cubes = {'red': 0, 'green': 0, 'blue': 0}  # minimum number of cubes for game to be possible
    possible = []
    for cubes in sets:
        for x in cubes.split(','):
            count, colour = x.split()
            possible.append(int(count) <= max_cubes[colour])
            if int(count) > minimum_cubes[colour]:
                minimum_cubes[colour] = int(count)
    return possible, minimum_cubes


def solution():
    games = read_input()
    ids = []
    powers = []

    for game, sets in games.items():
        possible, minimum_cubes = game_possible(sets)
        if all(possible) is True:
            ids.append(int(game))
        powers.append((np.prod(list(minimum_cubes.values()))))

    print(f'solution 1 : {sum(ids)}')
    print(f'solution 2: {sum(powers)}')


if __name__ == '__main__':
    solution()
