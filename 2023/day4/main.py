import dataclasses
import re
from typing import List, ClassVar


@dataclasses.dataclass(frozen=True)
class Cards:
    winning_numbers: List[str]
    card_numbers: List[str]

    @classmethod
    def from_line(cls, line: str) -> 'Cards':
        line = re.sub(r'Card \d+:', '', line).strip()
        winning_numbers, card_numbers = line.split('|')
        winning_numbers = winning_numbers.split()
        card_numbers = card_numbers.split()
        return cls(
            winning_numbers=winning_numbers,
            card_numbers=card_numbers
        )


def read_input() -> List[Cards]:
    cards = []
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            cards.append(Cards.from_line(line))
    return cards


def solution():
    cards = read_input()
    points = []
    for card in cards:
        overlap = set(card.winning_numbers) & set(card.card_numbers)
        if len(overlap) <= 1:
            points.append(len(overlap))
        elif len(overlap) > 1:
            # an overlap of 4 numbers is 1*2*2*2 which is the same as 2^3
            # 1<<(len(overlap) - 1)
            points.append(2**(len(overlap)-1))  # 2 to the power of the length - 1
    print(f'solution 1: {sum(points)}')


def solution2():
    cards = read_input()
    amount_of_cards = [1] * len(cards)  # set up list of 1 of each card e.g. 6 cards starts like [1, 1, 1, 1, 1, 1]

    for n, card in enumerate(cards):
        overlap = set(card.winning_numbers) & set(card.card_numbers)  # which numbers are winning numbers on the card
        for x in range(len(overlap)):  # range is the next x amount of cards won e.g. overlap is 2 win next two cards
            amount_of_cards[n + x + 1] += amount_of_cards[n]  # for each card in range add the amount of cards won
    print(f'solution 2: {sum(amount_of_cards)}')


if __name__ == '__main__':
    solution()
    solution2()
