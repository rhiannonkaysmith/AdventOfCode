import itertools

entries = 3


def read_input():
    with open('input.txt', 'r') as input_file:
        input_list = []
        for line in input_file:
            input_list.append(int(line.strip()))
        return input_list


def product_of_numbers(numbers: int):
    answer = 1
    for number in numbers:
        answer = answer * number
    return answer


def solution():
    list_numbers = read_input()
    for numbers in itertools.combinations(list_numbers, entries):
        if sum(numbers) == 2020:
            print(product_of_numbers(numbers))


if __name__ == '__main__':
    solution()
