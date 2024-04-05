from math import comb


def lagrange(nums):
    n = len(nums)
    result = 0
    for i, x in enumerate(nums):
        result += x * comb(n, i) * (-1) ** (n-1-i)
        # lagrange -> x * number of ways to choose * (-1) to the power of n-1-i
    return result


def lagrange_before(nums):
    n = len(nums)
    result = 0
    for i, x in enumerate(nums):
        result += x * comb(n, i + 1) * (-1) ** i
        # lagrange -> x * number of ways to choose (i+1 as we want the first) * (-1) to the power of i
    return result


def read_input():
    next_value = 0
    value_before = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            next_value += lagrange([int(n) for n in line.split()])
            value_before += lagrange_before([int(n) for n in line.split()])

    print(f'solution 1: {next_value}')
    print(f'solution 2: {value_before}')


if __name__ == '__main__':
    read_input()
