import re

with open('input.txt', 'r') as input_file:
    seeds, *mappings = input_file.read().split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))


def new_position(s, mapping):
    for m in mapping:
        for conversions in re.findall(r'(\d+) (\d+) (\d+)', m):
            destination, start, length = map(int, conversions)
            if s in range(start, start + length):
                s += destination - start
                break
    return s


def solution():
    end_positions = [new_position(s, mappings) for s in seeds]
    print(f'solution 1: {min(end_positions)}')


if __name__ == '__main__':
    solution()
