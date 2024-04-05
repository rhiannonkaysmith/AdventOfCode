import dataclasses
from typing import List, Dict
import re


@dataclasses.dataclass(frozen=True)
class Network:
    instructions: List
    maps: Dict

    @classmethod
    def from_file(cls, input_file):
        instructions = [i for i in input_file.split('\n')[0]]
        look_up = input_file.split('\n')[2:]
        maps = {}
        for x in look_up:
            index = x.split(' = ')[0]
            mapping = tuple(re.findall(r'\w+', x.split(' = ')[1]))
            maps[index] = mapping
        return cls(
            instructions=instructions,
            maps=maps
        )


def read_input():
    with open('input.txt', 'r') as input_file:
        return Network.from_file(input_file.read())


def solution():
    network = read_input()
    steps = 0
    element = list(network.maps.keys())[0]

    while element != 'ZZZ':
        instruction = network.instructions[steps % len(network.instructions)]
        element = network.maps[element][1] if instruction == 'R' else network.maps[element][0]
        # print(steps)
        steps += 1
    print(f'Solution 1: {steps}')


if __name__ == '__main__':
    solution()
