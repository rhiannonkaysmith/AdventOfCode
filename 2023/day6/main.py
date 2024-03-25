import dataclasses
import re
import numpy as np


@dataclasses.dataclass(frozen=True)
class Races:
    times: list[int]
    distances: list[int]
    time: int
    distance: int

    @classmethod
    def from_file(cls, input_file: str) -> 'Races':
        times = re.sub('Time:', '', input_file.split('\n')[0]).split()
        distances = re.sub('Distance:', '', input_file.split('\n')[1]).split()
        return cls(
            times=list(map(int, times)),
            distances=list(map(int, distances)),
            time=int(''.join(times)),
            distance=int(''.join(distances))
        )


def read_input():
    with open('input.txt', 'r') as input_file:
        return Races.from_file(input_file.read())


def solution():
    races = read_input()
    counter = 0
    no_won = []
    for time in races.times:
        distance = races.distances[counter]
        win = []
        for x in range(time):
            travelled = x*(time-x)
            win.append(travelled > distance)
        counter += 1
        no_won.append(sum(win))
    print(f'solution 1: {np.prod(no_won)}')


def solution2():
    races = read_input()
    time = races.time
    distance = races.distance
    win = []
    for x in range(time):
        travelled = x * (time - x)
        win.append(travelled > distance)
    print(f'solution 2: {sum(win)}')


if __name__ == '__main__':
    solution()
    solution2()
