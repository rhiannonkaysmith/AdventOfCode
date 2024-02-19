import dataclasses
from typing import List


@dataclasses.dataclass(frozen=True)
class DbRow:
    position1: int
    position2: int
    letter: str
    password: str

    @classmethod
    def from_line(cls, line: str) -> 'DbRow':
        parts = line.strip().split(' ')
        appears = parts[0].split('-')
        letter = parts[1].strip(':')
        password = parts[2]
        return cls(
            position1=int(appears[0]),
            position2=int(appears[1]),
            letter=letter,
            password=password
        )

    def valid_part1(self) -> bool:
        letter_count = self.password.count(self.letter)
        return self.position1 <= letter_count <= self.position2

    def valid_part2(self) -> bool:
        if self.position1 > len(self.password) or self.position2 > len(self.password):
            return False
        first_rule = self.password[self.position1 - 1] == self.letter
        second_rule = self.password[self.position2 - 1] == self.letter
        return first_rule or second_rule  # XOR


def read_input() -> List[DbRow]:
    with open('input.txt', 'r') as input_file:
        input_list = []
        for line in input_file:
            input_list.append(DbRow.from_line(line))
        return input_list


def solution():
    loaded_rows = read_input()
    # valid_passwords = []
    valid_q1_password = 0
    valid_q2_password = 0
    for db_row in loaded_rows:
        if db_row.valid_part1():
            valid_q1_password += 1
        if db_row.valid_part2():
            valid_q2_password += 1

    print(f'Q1: valid {valid_q1_password}')
    print(f'Q2: valid {valid_q2_password}')


if __name__ == '__main__':
    solution()
