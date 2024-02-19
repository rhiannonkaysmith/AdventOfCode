import dataclasses
from typing import List
import numpy as np
import math


@dataclasses.dataclass(frozen=True)
class DbRow:
    row: str
    column: str

    @classmethod
    def from_line(cls, line: str) -> 'DbRow':
        return cls(
            row=line[:7],
            column=line[7:].strip()
        )

    def find_row(self):
        first_row = 0
        last_row = 127
        for x in self.row:
            if x == 'F':
                last_row = math.floor(np.mean([first_row, last_row]))
            if x == 'B':
                first_row = math.ceil(np.mean([first_row, last_row]))
        return first_row

    def find_column(self):
        first_column = 0
        last_column = 7
        for x in self.column:
            if x == 'L':
                last_column = math.floor(np.mean([first_column, last_column]))
            if x == 'R':
                first_column = math.ceil(np.mean([first_column, last_column]))
        return first_column


def read_input() -> List[DbRow]:
    with open('day5input.txt', 'r') as input_file:
        input_list = []
        for line in input_file:
            input_list.append(DbRow.from_line(line))
        return input_list


def solution():
    loaded_rows = read_input()
    seat_ids = []
    for db_row in loaded_rows:
        seat_ids.append((db_row.find_row() * 8) + db_row.find_column())
    print(f'solution 1 :{max(seat_ids)}')
    my_seat = set(range(min(seat_ids), max(seat_ids))) - set(seat_ids)
    print(f'solution 2:{my_seat}')


if __name__ == '__main__':
    solution()
