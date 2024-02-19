

def read_input():
    with open('day8inputtest.txt', 'r') as input_file:
        input_list = []
        for line in input_file:
            input_list.append((line.strip().split(' ')))
        return input_list


def solution_1():
    operations = read_input()

    accumulator = 0
    position = 0
    visited = []

    while position not in visited:
        visited.append(position)
        operation = operations[position][0]
        amount = int(operations[position][1])

        if operation == 'nop':
            position += 1
        if operation == 'acc':
            accumulator += amount
            position += 1
        if operation == 'jmp':
            position += amount
    else:
        print(f'Solution 1: accumulator value before an instruction executed twice is {accumulator}')


def solution_2():
    operations = read_input()

    accumulator = 0
    position = 0
    visited = []
    operations_made = []
    max_position = len(operations) - 1

    while position not in visited and position <= max_position:
        visited.append(position)
        operation = operations[position][0]
        operations_made.append(operation)
        amount = int(operations[position][1])

        if operation == 'nop':
            if position + 1 not in visited:
                position += 1
            else:
                print('Infinite loop! operation last nop needs to be jmp')
                position += amount
        if operation == 'acc':
            accumulator += amount
            position += 1
        if operation == 'jmp':
            if position + amount not in visited:
                position += amount
            else:
                print('Infinite loop! operation last jmp needs to be nop')
                print(position)
                print(visited)
                print(list(reversed(operations_made)))
                back = -2
    else:
        print(f'Solution 2: accumulator value is {accumulator}')


if __name__ == '__main__':
    solution_2()
