

def read_input():
    with open('input.txt', 'r') as input_file:
        input_list = []
        for line in input_file:
            input_list.append(line.strip())
        return input_list


# def solution():
#     maps = read_input()
#     position = 0
#     trees = []
#     width = len(maps[0])
#     move_right = 3
#
#     for map in maps:
#         if map[position % width] == '.':
#             trees.append('O')
#         if map[position % width] == '#':
#             trees.append('X')
#         position += move_right
#
#     print(trees.count('X'))


def product(numbers: int):
    answer = 1
    for number in numbers:
        answer = answer * number
    return answer


def find_trees(moves):
    maps = read_input()
    position = 0
    line = 0
    width = len(maps[0])
    move_right = moves[0]
    move_down = moves[1]
    trees = []
    for map in maps:
        if map[position % width] == '.' and line % move_down == 0:
            trees.append('O')
        if map[position % width] == '#' and line % move_down == 0:
            trees.append('X')
        if line % move_down == 0:
            position += move_right
        line += 1
    return trees


def solution():
    trees_count = []
    movement = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    for moves in movement:
        trees_count.append(find_trees(moves).count('X'))

    print(trees_count, product(trees_count))


if __name__ == '__main__':
    solution()
