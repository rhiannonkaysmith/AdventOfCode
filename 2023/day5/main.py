import re

with open('input.txt', 'r') as input_file:
    mappings = input_file.read().split('\n\n')


def solution():
    seeds = re.findall(r'\d+', mappings[0])

    locations = []
    for s in map(int, seeds):
        # gets the seeds from seeds: 79 14 55 13 -> 79, 14, 55, 13
        for m in mappings[1:]:
            for conversions in re.findall(r'(\d+) (\d+) (\d+)', m):
                destination, start, length = map(int, conversions)
                if s in range(start, start + length):
                    s += destination - start
                    break
        locations.append(s)
    print(f'lowest location:{min(locations)}')


def solution_2():
    seeds = re.findall(r'(\d+) (\d+)', mappings[0])

    new_seeds = []
    for seed, length in seeds:
        for s in list(range(int(seed), int(seed) + int(length))):
            new_seeds.append(s)

    # locations = []
    # for s in new_seeds:
    #     for m in mappings[1:]:
    #         for conversions in re.findall(r'(\d+) (\d+) (\d+)', m):
    #             destination, start, length = map(int, conversions)
    #             if s in range(start, start + length):
    #                 s += destination - start
    #                 break
    #     locations.append(s)
    # print(f'solution 2 lowest location:{min(locations)}')


if __name__ == '__main__':
    solution()
    # solution_2()
