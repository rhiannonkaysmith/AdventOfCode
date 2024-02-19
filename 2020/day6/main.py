import dataclasses
from typing import List
import numpy as np
from collections import Counter


@dataclasses.dataclass(frozen=True)
class Forms:
    @classmethod
    def read_input(cls) -> List['Forms']:
        all_groups = []
        with open('day6input.txt', 'r') as input_file:
            current_group = []
            group_size = 0
            for line in input_file:
                if not line.replace('\n', ''):
                    if answers is not None:
                        all_groups.append((group_size, current_group))

                    current_group = []
                    group_size = 0
                    continue  # next line

                form = line.split()
                for answers in form:
                    group_size += 1
                    for answer in answers:
                        current_group.append(answer)

            if current_group:
                # we have leftover data
                if answers is not None:
                    all_groups.append((group_size, current_group))

            return all_groups


def solution():
    all_groups = Forms.read_input()
    unique_answers = []
    same_answers = 0
    for group in all_groups:
        unique_answers.append(len(np.unique(group[1])))
        answers_count = dict((i, group[1].count(i)) for i in group[1])
        for x in answers_count.values():
            if x == group[0]:
                same_answers += 1

    print(f'solution 1, anyone answered yes: {sum(unique_answers)}')
    print(f'solution 2, everyone had same answers {same_answers}')


if __name__ == '__main__':
    solution()
