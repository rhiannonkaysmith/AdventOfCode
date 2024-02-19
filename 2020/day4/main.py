import argparse
import dataclasses
from typing import List, Optional


@dataclasses.dataclass(frozen=True)
class Passport:
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: str = None

    @property
    def is_valid(self) -> bool:
        if not 1920 <= self.byr <= 2002:
            return False
        if not 2010 <= self.iyr <= 2020:
            return False
        if not 2020 <= self.eyr <= 2030:
            return False
        if not ((self.hgt[-2:] == 'cm' and 150 <= int(self.hgt[:-2]) <= 193) or
                (self.hgt[-2:] == 'in' and 59 <= int(self.hgt[:-2]) <= 76)):
            return False
        if not (self.hcl[0] == '#' and len(self.hcl) == 7):
            return False
        if self.ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False
        if len(self.pid) != 9:
            return False

        return True

    @classmethod
    def make_passport(cls, **kwargs) -> Optional['Passport']:
        try:
            formatted_kwargs = {}
            for field in dataclasses.fields(cls):
                if field.name in kwargs:
                    formatted_kwargs[field.name] = field.type(kwargs[field.name])

            passport = cls(**formatted_kwargs)
        except TypeError as e:
            print(f'Invalid passport found: {kwargs}: {e}')
        except ValueError:
            print(f'Invalid type found: {kwargs}')
            pass  # consider bad types are missing
        else:
            return passport
        return None

    @classmethod
    def read_input(cls, filename: str) -> List['Passport']:
        all_passports = []
        print(f'Loading {filename}')
        with open(filename, 'r') as input_file:
            current_passport = {}
            for line in input_file:
                if not line.replace('\n', ''):
                    # passport read completed
                    passport = cls.make_passport(**current_passport)
                    if passport is not None:
                        all_passports.append(passport)

                    current_passport = {}
                    continue  # next line

                elements = line.split()
                for elem in elements:
                    key, value = elem.split(':')
                    current_passport[key] = value

        if current_passport:
            # we have leftover data
            passport = cls.make_passport(**current_passport)
            if passport is not None:
                all_passports.append(passport)

        return all_passports


def solution():
    parser = argparse.ArgumentParser(description='aoc 2020 day 4')
    parser.add_argument('--input', type=str, default='input.txt', help='file to load, default=%(default)s')
    args = parser.parse_args()

    all_passports = Passport.read_input(args.input)
    print(f'Q1: Found {len(all_passports)} passports with mandatory fields')

    valid_passports = sum((1 if p.is_valid else 0 for p in all_passports))
    print(f'Q2: Found {valid_passports} valid passports')


if __name__ == '__main__':
    solution()
