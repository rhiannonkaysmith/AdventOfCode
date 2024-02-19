import re


def read_input():
    with open('input.txt', 'r') as input_file:
        input_list = []
        for line in input_file:
            input_list.append(re.sub('[^0-9]', '', line))
        return input_list


def read_input2():
    with open('input.txt', 'r') as input_file:
        input_list = []
        for line in input_file:
            line = line.replace("one", "o1e")
            line = line.replace("two", "t2o")
            line = line.replace("three", "t3e")
            line = line.replace("four", "f4r")
            line = line.replace("five", "f5e")
            line = line.replace("six", "s6x")
            line = line.replace("seven", "s7n")
            line = line.replace("eight", "e8t")
            line = line.replace("nine", "n9e")
            input_list.append(re.sub('[^0-9]', '', line))
        return input_list


def solution1():
    result = read_input()
    calibration_values = []
    for x in result:
        calibration_values.append(int(str(x[0]) + str(x[-1])))

    return sum(calibration_values)


def solution2():
    result = read_input2()

    calibration_values = []
    for x in result:
        calibration_values.append(int(str(x[0]) + str(x[-1])))

    return sum(calibration_values)


if __name__ == '__main__':
    print(f'solution1: {solution1()}')
    print(f'solution2: {solution2()}')
